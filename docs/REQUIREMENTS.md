# NeuroOps – Requirements Specification

Multi-tenant AI-native SaaS for SMEs: CRM, inventory, accounting, analytics, and AI automation. This document defines functional and non-functional requirements.

---

## 1. Scope and Goals

- **Product:** NeuroOps – all-in-one business infrastructure for SMEs.
- **Users:** Super Admin (platform-wide), Tenant Admin (organization), End User (daily use).
- **Outcomes:** Single place to manage customers, products, finances, analytics, and AI-driven insights with subscription billing and security/compliance baseline.

---

## 2. User Roles and Capabilities

| Role | Scope | Key capabilities |
|------|--------|------------------|
| **Super Admin** | All tenants, global config | Tenant CRUD, global feature flags, billing/usage oversight, platform config, audit view |
| **Tenant Admin** | Single tenant | User CRUD, subscription management, tenant settings, analytics, invite users |
| **End User** | Single tenant, assigned permissions | CRM, inventory, accounting (as permitted), dashboards, AI chat, reports |

Role hierarchy: Super Admin > Tenant Admin > End User. Permissions are additive within tenant.

---

## 3. Functional Requirements

### 3.1 Authentication and Identity

- **FR-AUTH-01** User registration with email verification (tenant-aware: org/slug or invite).
- **FR-AUTH-02** Login (email/password); optional SSO placeholder for future.
- **FR-AUTH-03** JWT access + refresh; configurable expiry (e.g. 7-day access, refresh rotation).
- **FR-AUTH-04** Password reset via email with time-limited token.
- **FR-AUTH-05** Session invalidation on logout and optional “revoke all” for tenant admin.
- **FR-AUTH-06** Multi-tenant context: every request scoped by tenant (header or JWT claim); reject cross-tenant access.

### 3.2 Authorization (RBAC)

- **FR-RBAC-01** Permissions defined per resource/action (e.g. crm:read, inventory:write, billing:manage).
- **FR-RBAC-02** Roles group permissions; users get one or more roles per tenant.
- **FR-RBAC-03** Every API enforces permission checks; 403 when lacking permission.
- **FR-RBAC-04** Super Admin bypasses tenant-scoped checks for platform operations only.

### 3.3 Multi-Tenancy and Data Isolation

- **FR-TENANT-01** Tenant identified by stable ID (UUID); all tenant data tagged with `tenant_id`.
- **FR-TENANT-02** Row-level security (RLS) in PostgreSQL so queries never return other tenants’ rows.
- **FR-TENANT-03** Tenant creation by Super Admin; Tenant Admin cannot create sibling tenants.
- **FR-TENANT-04** Tenant suspension/archival without deleting data; suspended tenants cannot log in.

### 3.4 Subscription and Billing (Stripe)

- **FR-BILL-01** Subscription tiers (e.g. Starter, Growth, Enterprise) with defined feature sets.
- **FR-BILL-02** 7-day free trial per tenant (no card required or optional card); trial end triggers upgrade or restrict.
- **FR-BILL-03** Stripe Customer and Subscription creation; sync subscription status to platform DB.
- **FR-BILL-04** Webhooks for subscription created/updated/canceled/payment_failed; idempotent handling.
- **FR-BILL-05** Feature gating: restrict modules (e.g. AI, advanced analytics) by plan; enforce in API and UI.
- **FR-BILL-06** Tenant Admin can view current plan and upgrade/downgrade (Stripe Checkout or Customer Portal).

### 3.5 CRM

- **FR-CRM-01** Contacts: create, read, update, delete; list with filters and pagination.
- **FR-CRM-02** Deals/opportunities with stage and value; link to contacts.
- **FR-CRM-03** Activities: notes, tasks, timeline; linked to contact/deal.
- **FR-CRM-04** Search and simple reporting (e.g. pipeline by stage, win rate).

### 3.6 Inventory

- **FR-INV-01** Products/SKUs: name, SKU, quantity, reorder level, unit.
- **FR-INV-02** Stock movements: in/out/adjust; audit trail.
- **FR-INV-03** Low-stock alerts (configurable threshold); optional notifications.
- **FR-INV-04** Optional linkage to orders or accounting (placeholders for later).

### 3.7 Accounting

- **FR-ACC-01** Chart of accounts (tenant-specific); income, expense, asset, liability, equity.
- **FR-ACC-02** Journal entries: debits/credits, date, description; immutable once posted.
- **FR-ACC-03** Invoices: create, send, record payment; link to Stripe if used for invoicing.
- **FR-ACC-04** Basic P&amp;L and balance sheet reports (computed from journals).

### 3.8 Analytics and Reporting

- **FR-ANAL-01** Dashboards: configurable widgets (KPIs, charts) per tenant; role-based visibility.
- **FR-ANAL-02** Anomaly detection: run XGBoost (or equivalent) on time-series metrics; expose alerts.
- **FR-ANAL-03** Demand forecasting: Prophet (or equivalent) for selected series; expose via API and dashboard.
- **FR-ANAL-04** Export: CSV/PDF for reports (placeholder or basic implementation).

### 3.9 AI Features

- **FR-AI-01** RAG over tenant documents: ingest (chunk, embed), store in FAISS (or equivalent); query via API.
- **FR-AI-02** Chatbot: conversational interface; optional RAG context; tenant-scoped history.
- **FR-AI-03** Voice agent: placeholder for speech-in/text-out or full voice; configurable endpoint.
- **FR-AI-04** Fraud risk: scoring endpoint and alerts (model placeholder); configurable thresholds.
- **FR-AI-05** All AI endpoints tenant-scoped and permission-gated.

### 3.10 Feature Flags and Canary

- **FR-FF-01** Feature flags per tenant and/or globally (e.g. enable new UI, beta modules).
- **FR-FF-02** Canary deployment: route subset of traffic to new version (placeholder in gateway/ingress).

### 3.11 Audit and Compliance

- **FR-AUDIT-01** Audit log: who, when, resource, action, outcome, IP; immutable append-only store.
- **FR-AUDIT-02** Log sensitive actions: login, permission change, billing change, data export, tenant config.
- **FR-AUDIT-03** Retention policy (configurable); GDPR/SOC2-aligned: access, deletion, retention docs (placeholders).
- **FR-AUDIT-04** Data export and deletion workflows for GDPR (placeholders with clear TODOs).

---

## 4. Non-Functional Requirements

### 4.1 Security

- **NFR-SEC-01** No secrets in code or repo; use env vars or secret manager (placeholders in .env.example).
- **NFR-SEC-02** HTTPS only in production; TLS for service-to-service where applicable.
- **NFR-SEC-03** Input validation and output encoding; parameterized queries; no raw SQL from user input.
- **NFR-SEC-04** Rate limiting on auth and public APIs; optional per-tenant quotas.
- **NFR-SEC-05** Security headers (CSP, HSTS, etc.) on web app.
- **NFR-SEC-06** SOC2/GDPR alignment: document controls and data handling; implement access control and audit as above.

### 4.2 Performance and Scalability

- **NFR-PERF-01** API p95 latency target (e.g. &lt; 500 ms for non-AI endpoints); document and monitor.
- **NFR-PERF-02** AI endpoints may be async; return job ID and poll or webhook for result.
- **NFR-PERF-03** Horizontal scaling of stateless services; DB connection pooling.
- **NFR-PERF-04** Caching (e.g. Redis) for sessions and hot read data where appropriate.

### 4.3 Availability and Reliability

- **NFR-AVL-01** Target uptime (e.g. 99.5%); health checks and graceful degradation.
- **NFR-AVL-02** Idempotent handling of webhooks and critical writes where possible.
- **NFR-AVL-03** Database migrations backward-compatible; no destructive changes without backup/restore procedure.

### 4.4 Observability

- **NFR-OBS-01** Structured logging; correlation ID across services.
- **NFR-OBS-02** Metrics: request rate, latency, error rate, queue depth (Celery/Kafka).
- **NFR-OBS-03** Dashboards: service health, API latency, queue health, AI service performance, errors.
- **NFR-OBS-04** Alerts for failure thresholds; optional Slack/email scripts (placeholders).

### 4.5 Operability

- **NFR-OPS-01** Single-command local run (e.g. Docker Compose); documented env vars.
- **NFR-OPS-02** CI: unit and integration tests; E2E scaffold; no live AWS required for tests.
- **NFR-OPS-03** Deploy via Terraform/K8s with placeholders; no automatic apply without user confirmation.
- **NFR-OPS-04** Database migration scripts; dependency update and load-test scripts (Phase 6).

---

## 5. Out of Scope (Current Phase)

- Full SSO/SAML/OIDC (placeholder only).
- Native mobile apps (responsive web only).
- Real-time collaboration (e.g. live co-editing).
- Custom report builder (fixed set of reports/dashboards first).
- SageMaker or other cloud ML training (local/containerized models first; cloud on request).

---

## 6. Assumptions and Open Points

- Stripe is the payment provider; webhook signing secret required.
- One primary region for AWS; multi-region is future work.
- SME scale: hundreds of tenants, thousands of users; design for growth but validate limits.
- AI models (RAG, anomaly, forecast) run in-platform or in-cluster; optional cloud ML later with user approval.

Document version: 1.0. Placeholders for secrets and cloud resources; no credentials in repo.

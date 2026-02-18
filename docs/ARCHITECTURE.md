# NeuroOps – System Architecture

High-level architecture for the multi-tenant SaaS platform: frontend, backend microservices, AI services, data stores, queues, and observability. All environment variables and cloud resources are placeholders; ask the user for any real secrets or cloud access.

---

## 1. Architecture Overview

```
                                    +------------------+
                                    |   Load Balancer  |
                                    |  (ALB / Ingress) |
                                    +--------+---------+
                                             |
         +-----------------------------------+-----------------------------------+
         |                                   |                                   |
         v                                   v                                   v
+----------------+                 +----------------+                 +----------------+
|   Next.js      |                 |   Next.js      |                 |   Next.js      |
|   (SSR/API     |                 |   (static      |                 |   (API routes  |
|   routes)      |                 |   export opt)  |                 |   proxy)       |
+--------+-------+                 +----------------+                 +--------+-------+
         |                                                                     |
         |  HTTPS                                                                |
         v                                                                      v
+----------------------------------------------------------------------------------------+
|                              API Gateway / BFF (optional)                              |
|                         (tenant resolution, rate limit, auth)                          |
+----------------------------------------------------------------------------------------+
         |
         |  Internal HTTP / service mesh
         v
+--------+--------+--------+--------+--------+--------+--------+--------+
| Auth   | Tenant | CRM    | Inv    | Acct   | Billing| Analytics| AI     |
| (Django| (FastAPI)|(FastAPI)|(FastAPI)|(FastAPI)|(Stripe)|(FastAPI) |(FastAPI|
| /FastAPI)|       |        |        |        | sync)  |         |+ workers)|
+--------+--------+--------+--------+--------+--------+--------+--------+
         |         |        |        |        |         |         |
         v         v        v        v        v         v         v
+------------------+  +------------------+  +------------------+  +------------------+
| PostgreSQL       |  | Redis            |  | Kafka             |  | Celery (Redis)   |
| (per-svc or      |  | (sessions,       |  | (events, async    |  | (tasks, AI jobs)  |
|  shared RDS)     |  |  cache)          |  |  workflows)       |  |                  |
+------------------+  +------------------+  +------------------+  +------------------+
                                                      |
         +--------------------------------------------+--------------------------------------------+
         |                                            |                                            |
         v                                            v                                            v
+------------------+                        +------------------+                        +------------------+
| Prometheus       |                        | Grafana          |                        | CloudWatch /     |
| (metrics)        |<---------------------->| (dashboards)     |                        | logging (AWS)   |
+------------------+                        +------------------+                        +------------------+
```

---

## 2. Component Responsibilities

| Component | Responsibility | Stack |
|-----------|----------------|--------|
| **Frontend** | SSR, dashboards, auth UI, subscription UI, AI chat UI | Next.js, React |
| **Auth service** | Registration, login, JWT, password reset, tenant resolution | Django or FastAPI |
| **Tenant service** | Tenant CRUD, org settings, user-tenant-role mapping | FastAPI |
| **CRM service** | Contacts, deals, activities | FastAPI |
| **Inventory service** | Products, stock, movements | FastAPI |
| **Accounting service** | Chart of accounts, journals, invoices, reports | FastAPI |
| **Billing service** | Stripe sync, webhooks, plan/feature gating | FastAPI |
| **Analytics service** | Dashboards, anomaly, forecasting APIs | FastAPI |
| **AI service** | RAG (FAISS + LLM), chatbot, voice placeholder, fraud score, Celery tasks | FastAPI, PyTorch, FAISS, XGBoost, Prophet |

---

## 3. Data Flow

- **Read path:** Client -> Next.js or direct API -> Auth (JWT + tenant) -> Service -> PostgreSQL (with RLS); cache via Redis where defined.
- **Write path:** Client -> API -> validate & authorize -> PostgreSQL (audit log entry where required); async side-effects via Celery or Kafka.
- **Events:** Billing events, audit events, and optional analytics events published to Kafka; consumers update caches or downstream DBs.
- **AI:** Sync request -> AI API -> quick response or job ID; heavy work in Celery; result stored or streamed; RAG reads from FAISS + tenant doc store.

---

## 4. Multi-Tenant Data Isolation

- **Tenant ID** in JWT and/or header (`X-Tenant-ID` or `tenant_id` claim); resolved once per request.
- **PostgreSQL:** RLS policies on all tenant tables: `WHERE tenant_id = current_setting('app.tenant_id')::uuid`.
- **Redis:** Key prefix per tenant for tenant-scoped cache (e.g. `tenant:{id}:*`).
- **Kafka:** Topics can be shared with tenant key in message; or separate topic per tenant for high isolation (optional).
- **AI/FAISS:** Index per tenant or namespace; queries filtered by tenant.

---

## 5. Environment Variables and Placeholders

Use `.env` and `.env.example` only; never commit real values. Required placeholders:

| Variable | Used by | Description |
|----------|---------|-------------|
| `DATABASE_URL` | All backend services | PostgreSQL connection string (placeholder) |
| `REDIS_URL` | Auth, Celery, cache | Redis connection (placeholder) |
| `JWT_SECRET_KEY` | Auth | Signing key for JWTs (placeholder) |
| `JWT_ACCESS_EXPIRY_DAYS` | Auth | e.g. 7 (placeholder) |
| `STRIPE_SECRET_KEY` | Billing | Stripe API key (ask user) |
| `STRIPE_WEBHOOK_SECRET` | Billing | Webhook signing secret (ask user) |
| `STRIPE_PRICE_*` | Billing | Price IDs per tier (placeholder) |
| `OPENAI_API_KEY` or `LLM_API_KEY` | AI service | LLM for RAG/chat (ask user if used) |
| `KAFKA_BOOTSTRAP_SERVERS` | Services, workers | Kafka brokers (placeholder) |
| `AWS_ACCESS_KEY_ID` | Infra / optional AI | (ask user before use) |
| `AWS_SECRET_ACCESS_KEY` | Infra / optional AI | (ask user before use) |
| `AWS_REGION` | Infra | e.g. us-east-1 (placeholder) |
| `S3_BUCKET_*` | Optional uploads/AI | Bucket names (placeholder) |
| `FRONTEND_URL` | Auth, Billing | Next.js origin for redirects (placeholder) |
| `SUPER_ADMIN_EMAIL` | Auth | Initial super user (placeholder) |

---

## 6. API Keys and Cloud Resources (Placeholders)

- **Stripe:** API key and webhook secret required for live billing; use test keys and placeholder webhook secret for local.
- **LLM (RAG/Chat):** API key required for real RAG/chat; placeholder for local with mock responses.
- **AWS:** EKS/ECS, RDS, S3, IAM, CloudWatch – all via Terraform with placeholder vars; do not apply without user confirmation.
- **Container registry:** ECR or other; URL and credentials as placeholders; ask user before push.

---

## 7. Deployment Topology (Target)

- **Local:** Docker Compose: one container per service + Postgres, Redis, Kafka (or Redpanda), optional in-memory FAISS.
- **AWS:** EKS or ECS; RDS PostgreSQL; ElastiCache Redis; MSK or self-managed Kafka; S3 for artifacts; Prometheus/Grafana in-cluster or managed; Terraform to create all; no automatic apply.

---

## 8. Failure Modes and Mitigations

- **DB down:** Services return 503; retry and circuit breaker on client; RDS multi-AZ for production.
- **Redis down:** Session and cache miss; auth can fall back to DB (slower); Celery backend optional Redis.
- **Kafka down:** Event publishing fails; buffer or queue in app or degrade to sync path; document recovery.
- **Stripe webhook delay/failure:** Idempotent handler; retry; manual sync script for subscription status.
- **AI model slow/fail:** Timeout and return error or job ID; queue depth monitored; alert on high failure rate.

Document version: 1.0. All secrets and cloud resources are placeholders; request user input before using real credentials or creating cloud resources.

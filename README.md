# NeuroOps

AI-native multi-tenant SaaS for SMEs: CRM, inventory, accounting, analytics, and AI automation.

## Purpose and Product Context

NeuroOps gives small and medium businesses one place to manage customers, products, finances, and analytics with AI-driven insights. Target users are SMEs; roles include Super Admin (platform-wide), Tenant Admin (organization), and End User (daily use). The platform combines subscription billing (Stripe, 7-day trial), RBAC, row-level security, audit logging, and SOC2/GDPR-aligned security goals.

## Architecture Overview

- **Frontend:** Next.js 14 + React (landing, login/signup, dashboards, AI chat, subscription).
- **Backend:** FastAPI microservices for auth, tenant, CRM, inventory, accounting, billing, analytics, and AI. Each service has its own API and optional shared DB; tenant isolation via `tenant_id` and PostgreSQL RLS.
- **Data:** PostgreSQL (primary), Redis (sessions/cache), Kafka (events). Celery for async AI tasks.
- **AI:** RAG (FAISS + LLM), chatbot, voice placeholder, XGBoost anomaly, Prophet forecasting. Endpoints and placeholders for local testing; cloud resources only with user-provided keys.
- **Infra:** Docker Compose for local; Kubernetes and Terraform for AWS (EKS/ECS, RDS, S3, Prometheus/Grafana). No automatic cloud deploy; all secrets and credentials are placeholders until you provide them.

See `docs/ARCHITECTURE.md` and `docs/DEPENDENCY_MAPPING.md` for details.

## Key Workflows

1. **Signup / trial:** User signs up with email and optional org slug; 7-day trial starts; backend creates tenant and user (when implemented).
2. **Login:** Email/password; JWT with tenant and roles; frontend stores token and uses it for API calls.
3. **Dashboard:** User sees links to CRM, analytics, AI chat, subscription; role determines visibility (super admin, tenant admin, end user).
4. **Subscription:** Tenant Admin views plan and trial end; upgrade via Stripe Checkout (backend placeholder).
5. **AI chat:** User sends messages; frontend calls AI service; RAG/LLM behind feature (placeholder until keys set).
6. **Billing webhooks:** Stripe sends events; billing service verifies signature and updates subscription state (idempotent).

## Setup Instructions

**Prerequisites:** Docker and Docker Compose, Node 20+, Python 3.11+ (for local tests).

1. Clone the repo and open the project root.
2. **Backend (Docker):**
   - From repo root: `docker compose build && docker compose up -d`
   - Health checks: `curl http://localhost:8000/health` (auth), `http://localhost:8001/health` (tenant), etc.
3. **Frontend:**
   - `cd frontend && npm install && npm run dev`
   - Open http://localhost:3000 (landing, login, signup, dashboard).
4. **Env:** Copy `.env.example` to `.env` and `frontend/.env.example` to `frontend/.env.local`. Leave placeholders unless you add Stripe/LLM keys; backend will return 501 for unimplemented endpoints.
5. **Tests:**
   - Backend unit: `./scripts/local/run_tests.sh` or `cd services/auth && pytest tests/ -v`
   - E2E: `cd frontend && npm run test:e2e` (Playwright; starts Next.js automatically).

## Configuration

- **Root / Compose:** `.env` can set `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`, `OPENAI_API_KEY`, `AWS_*` for local overrides. Never commit `.env`.
- **Per-service:** Each service has a `.env.example` in its directory (e.g. `services/auth/.env.example`). Documented vars: `DATABASE_URL`, `REDIS_URL`, `JWT_SECRET_KEY`, `STRIPE_*`, `OPENAI_API_KEY`, `KAFKA_BOOTSTRAP_SERVERS`, etc. See `docs/ARCHITECTURE.md` and `docs/DEPENDENCY_MAPPING.md`.
- **Frontend:** `NEXT_PUBLIC_API_URL`, `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY`, optional `NEXT_PUBLIC_AI_API_URL`.

## Failure Modes

- **DB down:** Services return 503; retry and backoff on client; use RDS multi-AZ in production.
- **Redis down:** Session/cache miss; auth may fall back to DB; Celery backend may fail.
- **Stripe webhook delayed/failed:** Idempotent handler; retry; manual sync script for subscription status.
- **AI service slow/fail:** Timeout or 501; return job ID for async; monitor queue depth and errors.
- **Missing secrets:** Auth and billing return 501 or 503 until `JWT_SECRET_KEY` and Stripe keys are set; ask user for any production secret.

## Debugging Tips

- Backend logs: `docker compose logs -f auth` (or tenant, crm, etc.).
- Frontend: browser devtools and `npm run dev` terminal output.
- DB: connect with `psql` to the Compose Postgres (user `neuroops`, password `neuroops_local`, db `neuroops`) or use the URL from Compose env.
- E2E: `cd frontend && npx playwright test --debug` for headed mode.
- Health: hit `/health` on each service to confirm it is up.

## Explicit Non-Goals

- Full SSO/SAML (placeholder only).
- Native mobile apps (responsive web only).
- Real-time collaboration.
- Custom report builder in first release.
- Automatic AWS deploy or Terraform apply without user approval.

## Known Debt

- Auth and billing endpoints return 501 until JWT and Stripe are implemented and secrets provided.
- RLS and audit log SQL are in `infra/sql/`; apply manually after creating tables.
- Migrations and seed data are placeholder scripts; add Alembic or Django migrations per service.
- Helm chart has only auth/tenant example; extend for all services and inject secrets from external secret store.

## Screenshots

- Landing: `![Landing](./screenshots/landing.png)`
- Dashboard: `![Dashboard](./screenshots/dashboard.png)`
- AI Chat: `![AI Chat](./screenshots/chat.png)`

Add real screenshots under `screenshots/` when available.

# NeuroOps – Dependency Mapping

Modules listed in dependency order with required libraries, environment variables, AWS resources, and AI model dependencies. **If any secret, key, or permission is required for execution, the implementer must ask the user explicitly before proceeding.**

---

## 1. Dependency Order (Build and Run)

1. **Infrastructure and data stores** (PostgreSQL, Redis, Kafka) – no app code dependency.
2. **Shared libraries / contracts** – API schemas, shared DTOs, tenant/audit helpers (if extracted).
3. **Auth service** – depends on DB, Redis; no other app service.
4. **Tenant service** – depends on DB, Auth (for JWT validation).
5. **CRM, Inventory, Accounting** – depend on DB, Auth/Tenant (tenant resolution, RBAC).
6. **Billing service** – depends on DB, Auth, Stripe; optional Kafka.
7. **Analytics service** – depends on DB, Auth; optional Kafka/Redis.
8. **AI service** – depends on DB, Redis, Celery, optional Kafka; FAISS, PyTorch, XGBoost, Prophet.
9. **Frontend** – depends on Auth and all backend APIs (via env base URLs).
10. **Workers (Celery)** – depend on Redis/Kafka, same env as AI and billing.

---

## 2. Per-Module Details

### 2.1 PostgreSQL (shared or per-service)

| Item | Details |
|------|--------|
| Libraries | Driver: `psycopg2-binary` or `asyncpg` (Python); migrations: Alembic or Django migrations |
| Env vars | `DATABASE_URL` (placeholder) |
| AWS | RDS instance; subnet, security group; optional read replica (placeholder) |
| Secrets | DB password – ask user for production |

### 2.2 Redis

| Item | Details |
|------|--------|
| Libraries | `redis`, `celery[redis]` |
| Env vars | `REDIS_URL` (placeholder) |
| AWS | ElastiCache Redis (placeholder) |
| Secrets | None for local; optional AUTH for managed Redis – ask user |

### 2.3 Kafka

| Item | Details |
|------|--------|
| Libraries | `aiokafka` or `confluent-kafka-python` |
| Env vars | `KAFKA_BOOTSTRAP_SERVERS`, `KAFKA_*_TOPIC` (placeholders) |
| AWS | MSK or self-managed on EC2 (placeholder) |
| Secrets | SASL/SSL if required – ask user |

### 2.4 Auth service

| Item | Details |
|------|--------|
| Libraries | Django or FastAPI, `PyJWT`, `passlib`, `python-multipart` |
| Env vars | `DATABASE_URL`, `REDIS_URL`, `JWT_SECRET_KEY`, `JWT_ACCESS_EXPIRY_DAYS`, `FRONTEND_URL`, `SUPER_ADMIN_EMAIL` (placeholders) |
| AWS | EKS/ECS task; IAM for secrets (optional) – placeholder |
| Secrets | `JWT_SECRET_KEY` – ask user for production |

### 2.5 Tenant service

| Item | Details |
|------|--------|
| Libraries | FastAPI, SQLAlchemy or Django ORM, same DB driver |
| Env vars | `DATABASE_URL`, `AUTH_SERVICE_URL` or shared JWT validation |
| AWS | EKS/ECS task – placeholder |
| Secrets | None beyond DB and JWT |

### 2.6 CRM / Inventory / Accounting services

| Item | Details |
|------|--------|
| Libraries | FastAPI, SQLAlchemy or Django ORM, Pydantic |
| Env vars | `DATABASE_URL`, `REDIS_URL` (optional), auth/tenant URL or shared JWT |
| AWS | EKS/ECS tasks – placeholder |
| Secrets | None beyond DB |

### 2.7 Billing service (Stripe)

| Item | Details |
|------|--------|
| Libraries | FastAPI, `stripe`, SQLAlchemy |
| Env vars | `DATABASE_URL`, `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`, `STRIPE_PRICE_STARTER`, `STRIPE_PRICE_GROWTH`, `STRIPE_PRICE_ENTERPRISE`, `FRONTEND_URL` (placeholders) |
| AWS | EKS/ECS task – placeholder |
| Secrets | `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET` – ask user |

### 2.8 Analytics service

| Item | Details |
|------|--------|
| Libraries | FastAPI, SQLAlchemy, Pandas, `xgboost`, `prophet` (or fbprophet), optional Kafka client |
| Env vars | `DATABASE_URL`, `REDIS_URL`, `KAFKA_*` (optional) |
| AWS | EKS/ECS; optional S3 for report artifacts – placeholder |
| AI models | XGBoost (serialized model file or train on ingest); Prophet (library) – no external API |

### 2.9 AI service (RAG, chatbot, voice, fraud)

| Item | Details |
|------|--------|
| Libraries | FastAPI, `faiss-cpu` or `faiss-gpu`, `sentence-transformers` or embedding API client, PyTorch (optional), Celery |
| Env vars | `DATABASE_URL`, `REDIS_URL`, `CELERY_BROKER_URL`, `OPENAI_API_KEY` or `LLM_API_KEY`, `EMBEDDING_MODEL`, `LLM_MODEL` (placeholders) |
| AWS | EKS/ECS; optional S3 for FAISS indices and document store – placeholder; SageMaker only if user approves |
| AI models | FAISS index per tenant; embedding model (local or API); LLM (API or local); fraud model (XGBoost or placeholder) – ask user for any paid API keys |

### 2.10 Celery workers

| Item | Details |
|------|--------|
| Libraries | Celery, same as AI and billing app code |
| Env vars | Same as AI/Billing: `REDIS_URL`, `DATABASE_URL`, `KAFKA_*`, `OPENAI_API_KEY` (placeholders) |
| AWS | EKS/ECS worker deployment – placeholder |
| Secrets | Same as AI/Billing – ask user for LLM/Stripe if workers need them |

### 2.11 Frontend (Next.js)

| Item | Details |
|------|--------|
| Libraries | Next.js, React, fetch/axios for API, Stripe.js for checkout |
| Env vars | `NEXT_PUBLIC_API_URL`, `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY`, optional `NEXT_PUBLIC_WS_URL` (placeholders) |
| AWS | S3 + CloudFront or EKS Ingress – placeholder |
| Secrets | Stripe publishable key is public; no secret keys in frontend |

### 2.12 CI/CD

| Item | Details |
|------|--------|
| Libraries | GitHub Actions or GitLab CI; Docker; Terraform |
| Env vars | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`, registry credentials (placeholders) |
| AWS | ECR, EKS/ECS, IAM role for pipeline – placeholder |
| Secrets | AWS and registry credentials – ask user before any cloud run |

### 2.13 Terraform / K8s / Helm

| Item | Details |
|------|--------|
| Libraries | Terraform AWS provider, Kubernetes provider; Helm charts |
| Env vars | `TF_VAR_*` for region, account, cluster name; no secrets in repo |
| AWS | EKS or ECS, RDS, ElastiCache, S3, IAM, CloudWatch – all placeholders; do not apply without user confirmation |
| Secrets | Injected via K8s secrets or AWS Secrets Manager – ask user |

---

## 3. AI Model Dependencies Summary

| Model / Component | Type | Where it runs | Secret/Key |
|-------------------|------|----------------|------------|
| FAISS index | Vector index | AI service / worker | None for local; S3 if persisting – placeholder |
| Embeddings | sentence-transformers or API | AI service | API key if using OpenAI/other – ask user |
| LLM (RAG, chat) | API or local model | AI service / Celery | `OPENAI_API_KEY` or equivalent – ask user |
| XGBoost (anomaly/fraud) | Serialized model | Analytics / AI service | None |
| Prophet | Library | Analytics service | None |

---

## 4. Rule for Implementers

**Before using any secret, API key, or cloud permission:** pause and ask the user to provide or approve it. Do not hardcode credentials or run `terraform apply` / `kubectl apply` against real AWS without explicit user confirmation.

Document version: 1.0.

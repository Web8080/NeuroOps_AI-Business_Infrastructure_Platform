# AWS Deployment

Do not run Terraform or deploy containers without explicit user approval. This doc describes the steps; you must provide credentials and confirm each destructive or cloud-modifying action.

## Prerequisites

- AWS account and CLI configured (or use CI with stored credentials).
- Terraform >= 1.0.
- kubectl and Helm 3 (if using EKS).
- Docker and access to a container registry (ECR or other).

## Required from you

1. **AWS credentials**
   - Access Key ID and Secret Access Key, or IAM role for EC2/ECS.
   - Region (e.g. `us-east-1`).

2. **Database**
   - RDS master username and password (will be stored in Terraform state or Secrets Manager; do not commit).

3. **Secrets**
   - `JWT_SECRET_KEY` for auth service.
   - `STRIPE_SECRET_KEY` and `STRIPE_WEBHOOK_SECRET` for billing (if using Stripe).
   - `OPENAI_API_KEY` or equivalent for AI (if using external LLM).

4. **Confirmation**
   - Explicit "yes" before any `terraform apply`, `kubectl apply`, or push to production registry.

## Steps (manual, with approval)

1. **Terraform**
   - Copy `infra/terraform/terraform.tfvars.example` to `terraform.tfvars` and fill (do not commit).
   - Run `terraform init` and `terraform plan`. Review plan.
   - Run `terraform apply` only after you approve.

2. **Container images**
   - Build images (e.g. from repo root):  
     `docker build -f services/auth/Dockerfile -t YOUR_ECR_URL/auth:tag .`
   - Push to ECR after logging in: `aws ecr get-login-password --region REGION | docker login ...`

3. **Kubernetes**
   - Apply namespace and secrets:  
     `kubectl apply -f infra/k8s/namespace.yaml`  
     Create Secret `neuroops-db` and `neuroops-secrets` with env values.
   - Deploy services (or use Helm):  
     `helm install neuroops infra/helm/neuroops -f values-prod.yaml`

4. **Monitoring**
   - Deploy Prometheus and Grafana (see Phase 6). Configure scrape targets and dashboards.

5. **Frontend**
   - Build Next.js: `cd frontend && npm run build`. Serve via S3 + CloudFront or Ingress.

## Pause points

- Before `terraform apply`: confirm with user.
- Before pushing images to a production registry: confirm with user.
- Before changing live K8s/ECS: confirm with user.

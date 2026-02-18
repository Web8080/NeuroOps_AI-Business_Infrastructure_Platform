-- Row-level security for multi-tenant isolation.
-- Run after creating tables that have tenant_id. Set app.tenant_id per request in app code.

-- Enable RLS on tenant-scoped tables (example: adjust table names to match your schema).
-- ALTER TABLE tenants ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE users ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE contacts ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE deals ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE products ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE movements ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE accounts ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE journals ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE invoices ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE subscriptions ENABLE ROW LEVEL SECURITY;

-- Example policy: restrict rows to current tenant (app sets app.tenant_id in session).
-- CREATE POLICY tenant_isolation ON contacts
--   FOR ALL
--   USING (tenant_id = current_setting('app.tenant_id', true)::uuid)
--   WITH CHECK (tenant_id = current_setting('app.tenant_id', true)::uuid);

-- Super Admin bypass: use a role or session variable (e.g. app.is_super_admin = true)
-- and add a policy that allows all when that is set. Prefer application-level check
-- for super admin to avoid leaking data in shared connection pools.

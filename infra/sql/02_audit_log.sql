-- Audit log table: append-only. Services insert; never update/delete from application.

-- CREATE TABLE IF NOT EXISTS audit_log (
--   id BIGSERIAL PRIMARY KEY,
--   created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
--   tenant_id UUID,
--   user_id UUID,
--   action VARCHAR(128) NOT NULL,
--   resource_type VARCHAR(64) NOT NULL,
--   resource_id VARCHAR(256),
--   outcome VARCHAR(32) NOT NULL DEFAULT 'success',
--   details JSONB,
--   ip INET,
--   correlation_id VARCHAR(64)
-- );

-- Index for tenant + time range queries.
-- CREATE INDEX idx_audit_tenant_created ON audit_log (tenant_id, created_at DESC);
-- CREATE INDEX idx_audit_resource ON audit_log (resource_type, resource_id);

-- RLS: tenants see only their rows; super admin sees all (handled in app or policy).
-- ALTER TABLE audit_log ENABLE ROW LEVEL SECURITY;

'use client';

import Link from 'next/link';

export default function TenantAdminPage() {
  return (
    <main style={{ padding: '2rem', maxWidth: '900px', margin: '0 auto' }}>
      <p><Link href="/dashboard">Back to Dashboard</Link></p>
      <h1 style={{ marginTop: '1rem', marginBottom: '1rem' }}>Tenant Admin</h1>
      <p style={{ color: '#666' }}>Users, subscription, org settings, analytics. Role: tenant_admin.</p>
    </main>
  );
}

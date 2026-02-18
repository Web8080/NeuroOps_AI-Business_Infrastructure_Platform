'use client';

import Link from 'next/link';

export default function SuperAdminPage() {
  return (
    <main style={{ padding: '2rem', maxWidth: '900px', margin: '0 auto' }}>
      <p><Link href="/dashboard">Back to Dashboard</Link></p>
      <h1 style={{ marginTop: '1rem', marginBottom: '1rem' }}>Super Admin</h1>
      <p style={{ color: '#666' }}>Tenant list, global feature flags, platform config. Backend: /api/v1/tenants (super-admin only).</p>
    </main>
  );
}

'use client';

import Link from 'next/link';

export default function AnalyticsDashboardPage() {
  return (
    <main style={{ padding: '2rem', maxWidth: '900px', margin: '0 auto' }}>
      <p><Link href="/dashboard">Back to Dashboard</Link></p>
      <h1 style={{ marginTop: '1rem', marginBottom: '1rem' }}>Analytics</h1>
      <p style={{ color: '#666' }}>Charts and KPIs will load here. Backend: GET /api/v1/dashboards</p>
    </main>
  );
}

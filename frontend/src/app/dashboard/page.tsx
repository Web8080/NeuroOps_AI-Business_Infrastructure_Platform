'use client';

import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { useEffect, useState } from 'react';

export default function DashboardPage() {
  const router = useRouter();
  const [role, setRole] = useState<string | null>(null);

  useEffect(() => {
    const token = typeof window !== 'undefined' ? localStorage.getItem('access_token') : null;
    if (!token) {
      router.replace('/login');
      return;
    }
    setRole('end_user');
  }, [router]);

  return (
    <main style={{ padding: '2rem', maxWidth: '900px', margin: '0 auto' }}>
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <h1>Dashboard</h1>
        <nav style={{ display: 'flex', gap: '1rem' }}>
          <Link href="/dashboard/analytics">Analytics</Link>
          <Link href="/dashboard/chat">AI Chat</Link>
          <Link href="/dashboard/subscription">Subscription</Link>
          {role === 'super_admin' && <Link href="/admin">Super Admin</Link>}
          {role === 'tenant_admin' && <Link href="/admin/tenant">Tenant Admin</Link>}
          <button
            type="button"
            onClick={() => {
              localStorage.removeItem('access_token');
              localStorage.removeItem('refresh_token');
              router.push('/login');
            }}
          >
            Log out
          </button>
        </nav>
      </header>
      <section>
        <h2 style={{ marginBottom: '0.5rem' }}>Welcome</h2>
        <p style={{ color: '#666' }}>Use the links above for CRM, analytics, AI chat, and subscription.</p>
      </section>
    </main>
  );
}

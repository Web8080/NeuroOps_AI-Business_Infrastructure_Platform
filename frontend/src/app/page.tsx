'use client';

import Link from 'next/link';

export default function LandingPage() {
  return (
    <main style={{ padding: '2rem', maxWidth: '800px', margin: '0 auto' }}>
      <h1 style={{ marginBottom: '1rem' }}>NeuroOps</h1>
      <p style={{ marginBottom: '1.5rem', color: '#444' }}>
        All-in-one business infrastructure for SMEs: CRM, inventory, accounting, analytics, and AI.
      </p>
      <nav style={{ display: 'flex', gap: '1rem' }}>
        <Link href="/login" style={{ padding: '0.5rem 1rem', background: '#333', color: '#fff', borderRadius: '4px' }}>
          Log in
        </Link>
        <Link href="/signup" style={{ padding: '0.5rem 1rem', border: '1px solid #333', borderRadius: '4px' }}>
          Sign up
        </Link>
      </nav>
    </main>
  );
}

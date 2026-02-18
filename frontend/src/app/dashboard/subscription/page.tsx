'use client';

import Link from 'next/link';
import { useState, useEffect } from 'react';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export default function SubscriptionPage() {
  const [plan, setPlan] = useState<string | null>(null);
  const [trialEnd, setTrialEnd] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = typeof window !== 'undefined' ? localStorage.getItem('access_token') : null;
    if (!token) return;
    const billingUrl = (process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000').replace('8000', '8005').replace(/\/$/, '');
    fetch(`${billingUrl}/api/v1/subscription`, {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((r) => r.json())
      .then((d) => {
        setPlan(d.plan || 'trial');
        setTrialEnd(d.trial_end || null);
      })
      .catch(() => setPlan('unknown'))
      .finally(() => setLoading(false));
  }, []);

  return (
    <main style={{ padding: '2rem', maxWidth: '600px', margin: '0 auto' }}>
      <p><Link href="/dashboard">Back to Dashboard</Link></p>
      <h1 style={{ marginTop: '1rem', marginBottom: '1rem' }}>Subscription</h1>
      {loading && <p>Loading...</p>}
      {!loading && (
        <>
          <p>Plan: {plan}</p>
          {trialEnd && <p>Trial ends: {trialEnd}</p>}
          <p style={{ marginTop: '1rem' }}>Upgrade or manage billing via Stripe (backend not implemented yet).</p>
        </>
      )}
    </main>
  );
}

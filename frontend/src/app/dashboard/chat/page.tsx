'use client';

import { useState } from 'react';
import Link from 'next/link';

const AI_API_URL = process.env.NEXT_PUBLIC_AI_API_URL || process.env.NEXT_PUBLIC_API_URL?.replace('8000', '8007') || 'http://localhost:8007';

export default function AIChatPage() {
  const [message, setMessage] = useState('');
  const [messages, setMessages] = useState<{ role: string; content: string }[]>([]);
  const [loading, setLoading] = useState(false);

  async function sendMessage(e: React.FormEvent) {
    e.preventDefault();
    if (!message.trim() || loading) return;
    const userMsg = { role: 'user', content: message };
    setMessages((prev) => [...prev, userMsg]);
    setMessage('');
    setLoading(true);
    try {
      const token = typeof window !== 'undefined' ? localStorage.getItem('access_token') : null;
      const res = await fetch(`${AI_API_URL.replace(/\/$/, '')}/api/v1/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...(token ? { Authorization: `Bearer ${token}` } : {}),
        },
        body: JSON.stringify({ messages: [...messages, userMsg], use_rag: true }),
      });
      const data = await res.json().catch(() => ({}));
      if (res.ok && data.content) {
        setMessages((prev) => [...prev, { role: 'assistant', content: data.content }]);
      } else {
        setMessages((prev) => [...prev, { role: 'assistant', content: data.detail || 'AI service not configured.' }]);
      }
    } catch {
      setMessages((prev) => [...prev, { role: 'assistant', content: 'Network error.' }]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <main style={{ padding: '2rem', maxWidth: '600px', margin: '0 auto' }}>
      <p><Link href="/dashboard">Back to Dashboard</Link></p>
      <h1 style={{ marginTop: '1rem', marginBottom: '1rem' }}>AI Chat</h1>
      <div style={{ border: '1px solid #ccc', minHeight: '200px', padding: '1rem', marginBottom: '1rem' }}>
        {messages.length === 0 && <p style={{ color: '#888' }}>Send a message to start.</p>}
        {messages.map((m, i) => (
          <p key={i} style={{ marginBottom: '0.5rem' }}><strong>{m.role}:</strong> {m.content}</p>
        ))}
      </div>
      <form onSubmit={sendMessage} style={{ display: 'flex', gap: '0.5rem' }}>
        <input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type a message..."
          style={{ flex: 1, padding: '0.5rem' }}
        />
        <button type="submit" disabled={loading}>Send</button>
      </form>
    </main>
  );
}

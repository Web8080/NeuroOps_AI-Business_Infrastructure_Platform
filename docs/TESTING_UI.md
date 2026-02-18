# Testing the NeuroOps UI

Backend must be up first. Then run the frontend and open the app in a browser.

## 1. Start backend (if not already running)

From repo root:

```bash
docker compose up -d
```

Check health: `curl -s http://localhost:8000/health` should return `{"status":"ok"}`.

## 2. Start the frontend

```bash
cd frontend
npm install
npm run dev
```

Wait until you see: `Ready on http://localhost:3000` (or similar). Then open **http://localhost:3000** in your browser.

## 3. What to test

- **Landing (/**): Log in and Sign up links.
- **Sign up (/signup):** Form with email, password, org slug. Submitting will call the auth API (returns 501 until auth is implemented).
- **Log in (/login):** Email/password. Same 501 from backend for now.
- **Dashboard (/dashboard):** Redirects to login if not authenticated. After “logging in” (or if you bypass), you see links to Analytics, AI Chat, Subscription, and role-based admin links.
- **Analytics (/dashboard/analytics):** Placeholder copy.
- **AI Chat (/dashboard/chat):** Input and Send; calling AI service returns 501 or “not configured” until LLM is set up.
- **Subscription (/dashboard/subscription):** Placeholder; calls billing service (501 until Stripe is configured).

Backend endpoints are stubs (501). UI flows and navigation are what to verify.

## 4. Optional: E2E tests

```bash
cd frontend
npm install
npx playwright install --with-deps chromium
npm run test:e2e
```

Tests expect the frontend to run (or start it via Playwright config) and hit the pages above; backend 501 is acceptable.

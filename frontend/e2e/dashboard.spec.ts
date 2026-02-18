import { test, expect } from '@playwright/test';

test('dashboard redirects to login when not authenticated', async ({ page }) => {
  await page.goto('/dashboard');
  await expect(page).toHaveURL(/\/login/);
});

test('analytics page shows placeholder when accessed directly', async ({ page }) => {
  await page.goto('/dashboard/analytics');
  await expect(page.getByText(/analytics|charts|dashboards/i)).toBeVisible({ timeout: 5000 });
});

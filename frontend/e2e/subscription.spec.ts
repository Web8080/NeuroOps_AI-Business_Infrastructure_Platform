import { test, expect } from '@playwright/test';

test('subscription page shows plan or loading', async ({ page }) => {
  await page.goto('/dashboard/subscription');
  await expect(page.getByText(/subscription|plan|loading/i)).toBeVisible({ timeout: 5000 });
});

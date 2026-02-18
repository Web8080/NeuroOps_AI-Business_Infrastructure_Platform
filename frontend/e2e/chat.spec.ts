import { test, expect } from '@playwright/test';

test('AI chat page has input and send button', async ({ page }) => {
  await page.goto('/dashboard/chat');
  await expect(page.getByPlaceholder(/type a message/i)).toBeVisible();
  await expect(page.getByRole('button', { name: /send/i })).toBeVisible();
});

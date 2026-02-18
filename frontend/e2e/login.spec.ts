import { test, expect } from '@playwright/test';

test('landing page has login and signup links', async ({ page }) => {
  await page.goto('/');
  await expect(page.getByRole('link', { name: /log in/i })).toBeVisible();
  await expect(page.getByRole('link', { name: /sign up/i })).toBeVisible();
});

test('login page submits and redirects or shows error', async ({ page }) => {
  await page.goto('/login');
  await page.getByPlaceholder('Email').fill('test@example.com');
  await page.getByPlaceholder('Password').fill('password');
  await page.getByRole('button', { name: /sign in/i }).click();
  await expect(page.getByText(/login failed|signing in|network error/i)).toBeVisible({ timeout: 10000 });
});

test('signup page has trial message', async ({ page }) => {
  await page.goto('/signup');
  await expect(page.getByText(/7-day|trial/i)).toBeVisible();
});

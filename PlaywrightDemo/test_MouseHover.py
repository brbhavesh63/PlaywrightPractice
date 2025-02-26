

import time

from playwright.sync_api import Playwright, expect


def test_UIAlerts1(playwright : Playwright):

    browser = playwright.chromium.launch(headless=False,args = ["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role("link",name='Top').click()
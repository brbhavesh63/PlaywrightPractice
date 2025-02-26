import time

from playwright.sync_api import Playwright


def test_UIAlerts(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    new_context = browser.new_context(no_viewport=True)
    page = new_context.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dialog : dialog.accept())
    page.locator("#confirmbtn").click()
    time.sleep(2)
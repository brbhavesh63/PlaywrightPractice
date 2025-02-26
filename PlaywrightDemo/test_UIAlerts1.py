import time

from playwright.sync_api import Playwright


def test_UIAlerts1(playwright : Playwright):

    browser = playwright.chromium.launch(headless=False,args = ["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog",lambda dialog:dialog.accept())
    page.locator("#alertbtn").click()
    time.sleep(3)
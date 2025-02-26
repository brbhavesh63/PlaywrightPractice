import time

from playwright.sync_api import Playwright, expect


def test_UIAlerts1(playwright : Playwright):

    browser = playwright.chromium.launch(headless=False,args = ["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    pageframe = page.frame_locator("#courses-iframe")
    pageframe.get_by_role("link",name="All Access plan").click()
    expect(pageframe.locator("body")).to_contain_text("Happy Subscibers!")
    time.sleep(2)
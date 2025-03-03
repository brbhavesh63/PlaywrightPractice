import time

from playwright.sync_api import Playwright, expect


def interceptRoute(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=67c5cc1ec019fb1ad614a48b")


def test_intercept_response(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",interceptRoute)
    page.locator("#userEmail").fill("bhavesh.rana@mail.com")
    page.locator("#userPassword").fill("Bhavesh@8238")
    page.locator("#login").click()
    page.locator("[routerlink='/dashboard/myorders']").click()
    page.get_by_role("button",name='View').first.click()
    time.sleep(5)
    expect(page.locator(".blink_me")).to_have_text("You are not authorize to view this order")

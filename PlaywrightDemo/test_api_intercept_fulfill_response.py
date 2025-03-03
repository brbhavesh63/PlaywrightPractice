from playwright.sync_api import Playwright, expect

noOrderOfCustomer = {"data":[],"message":"No Orders"}

def intercept_response(route):
    route.fulfill(
        json = noOrderOfCustomer
    )

def test_intercept_response(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",intercept_response)
    page.locator("#userEmail").fill("bhavesh.rana@mail.com")
    page.locator("#userPassword").fill("Bhavesh@8238")
    page.locator("#login").click()
    page.locator("[routerlink='/dashboard/myorders']").click()
    expect(page.locator(".mt-4")).to_have_text(" You have No Orders to show at this time. Please Visit Back Us ")
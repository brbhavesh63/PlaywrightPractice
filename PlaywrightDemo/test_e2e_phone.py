import time

from playwright.sync_api import Playwright, expect

from PlaywrightDemo.Utils.api_utils_phone import APIUtils_Phone


def test_e2e_shoes(playwright:Playwright):

    browser = playwright.chromium.launch(headless=False , args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill("bhavesh.rana@mail.com")
    page.locator("#userPassword").fill("Bhavesh@8238")
    page.locator("#login").click()

    api_utils = APIUtils_Phone()
    order_id  = api_utils.createOrder(playwright)

    page.locator("[routerlink='/dashboard/myorders']").click()
    totalNoOfColumn = page.locator("th[scope='col']").count()
    myorder_column = 0
    for i in range(totalNoOfColumn):
        order_column = page.locator("th[scope='col']").nth(i).filter(has_text="Order Id").count()
        if order_column > 0:
            myorder_column = i
            print(myorder_column)
            break

    order_row = page.locator("tr[class='ng-star-inserted']").filter(has_text=order_id)
    order_row.get_by_role("button",name= 'View').click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    time.sleep(3)


import time

from playwright.sync_api import Playwright, expect

from PlaywrightDemo.Utils.api_utils_shoes import APIUtils_Shoes


def test_e2e_shoes(playwright:Playwright):

    browser = playwright.chromium.launch(headless=False , args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill("bhavesh.rana@mail.com")
    page.locator("#userPassword").fill("Bhavesh@8238")
    page.locator("#login").click()

#     Get OerderID from the API Utlils Shoes

    api_utils = APIUtils_Shoes()
    order_id = api_utils.createShoesOrder(playwright)


#     Now verification process of the shoes take place

    page.locator("[routerlink='/dashboard/myorders']").click()
    totalNoOfColumns = page.locator("th[scope='col']").count()
    myorderid_column = 0
    for i in range(totalNoOfColumns):
        orderid_column = page.locator("th[scope='col']").nth(i).filter(has_text="Order Id").count()
        if orderid_column > 0 :
            myorderid_column = i
            print(myorderid_column)

    order_row = page.locator("tr[class='ng-star-inserted']").filter(has_text=order_id)
    order_row.get_by_role("button",name= 'View').click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    time.sleep(3)

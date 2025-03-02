import time

from playwright.sync_api import Playwright, expect

from PlaywrightDemo.Utils.api_utils import APIUtils


def test_e2e_web_api(playwright :Playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill("bhavesh.rana@mail.com")
    page.locator("#userPassword").fill("Bhavesh@8238")
    page.locator("#login").click()

    # Retrive ORDER_ID from the api_utils
    apiutils = APIUtils()
    order_id = apiutils.CreateOrder(playwright)

    # Order Histroy Page -> Order ID is present or not

    page.locator("[routerlink='/dashboard/myorders']").click()
    totalNoOfColumn = page.locator("th[scope='col']").count()
    myorderIdColumn = 0
    for i in range(totalNoOfColumn):
        orderIdColumn = page.locator("th[scope='col']").nth(i).filter(has_text="Order Id").count()
        if orderIdColumn > 0 :
            myorderIdColumn = i
            print(myorderIdColumn)
            break

    orderId_Row = page.locator("tr[class=ng-star-inserted]").nth(myorderIdColumn).filter(has_text=order_id)
    orderId_Row.get_by_role("button",name='View').click()
    expect(page.locator("[class='tagline']")).to_have_text("Thank you for Shopping With Us")


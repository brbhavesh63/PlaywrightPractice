import time

from playwright.sync_api import Playwright, expect


def test_webTables(playwright : Playwright):

    browser = playwright.chromium.launch(headless=False ,args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")

    with page.expect_popup() as page_info:
        page.get_by_role("link",name="Top Deals").click()
        deal_page = page_info.value
    totalNoofColumn = deal_page.locator("th").count()

    for i in range(totalNoofColumn):
        priceColumn  = deal_page.locator("th").nth(i).filter(has_text="Price").count()
        if priceColumn > 0:
            mypriceColumn = i
            print(f"price coloumn value is {mypriceColumn}")
            break

    time.sleep(2)
    riceRow = deal_page.locator("tr").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(mypriceColumn)).to_have_text("37")

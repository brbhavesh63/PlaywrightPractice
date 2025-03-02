from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import new_context


def test_webtables1(playwright:Playwright):

    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
    with page.expect_popup() as page_info:
        page.get_by_role("link",name='Top Deals').click()
        deal_page = page_info.value

    total_column = deal_page.locator('th').count()
    priceColumn=0
    for i in range(total_column):
        column_header = deal_page.locator("th").nth(i).text_content()
        if column_header == 'Price':
            priceColumn = i
            print(f"The price column is {priceColumn}")

    rice_row = deal_page.locator("tr").filter(has_text="Rice")
    expect(rice_row.locator("td").nth(priceColumn)).to_have_text("37")
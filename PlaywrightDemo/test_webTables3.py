from playwright.sync_api import Playwright


def test_webTables3(playwright:Playwright):

    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://cosmocode.io/automation-practice-webtable/")
    totalColumn = page.locator("h3").count()

    for i in range(totalColumn):
        column_header = page.locator("h3").nth(i).text_content()
        if column_header == 'Country':
            country_column = i
            break
    #
    # myCountry = page.locator("td").filter(has_text="India")
    # myCountry.locator("")
    # print(myCountry)
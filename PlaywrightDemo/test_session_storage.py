from playwright.sync_api import Playwright, expect

from PlaywrightDemo.Utils.api_utils import APIUtils


def test_inject_token(playwright : Playwright):

    api_utils = APIUtils()
    gettoken = api_utils.GetToken(playwright)

    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.add_init_script(f"""localStorage.setItem('token','{gettoken}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("[routerlink='/dashboard/myorders']").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()

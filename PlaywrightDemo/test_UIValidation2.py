from playwright.sync_api import expect


def test_hideShowValidation(playwright):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    new_context = browser.new_context(no_viewport=True)
    page = new_context.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
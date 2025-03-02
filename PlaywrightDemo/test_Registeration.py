from playwright.sync_api import Playwright, expect


def test_Register(playwright : Playwright):

    browser = playwright.chromium.launch(headless=False ,args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/")
    page.locator(".text-reset").click()
    page.locator("#firstName").fill("Bhavesh")
    page.locator("#lastName").fill("Rana")
    page.locator("#userEmail").fill("bhavesh.rana@mail.com")
    page.locator("#userMobile").fill("6546531465")
    page.locator(".custom-select").select_option("Engineer")
    page.locator("input[value='Male']").click()
    page.locator("#userPassword").fill("Bhavesh@8238")
    page.locator("#confirmPassword").fill("Bhavesh@8238")
    page.locator("input[type='checkbox']").click()
    page.locator("#login").click()
    expect(page.locator("h1[class='headcolor']")).to_have_text("Account Created Successfully")
import time

from playwright.sync_api import Page, expect, Playwright


def test_PlaywrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")

def test_PlaywrightShortcuts(page:Page):
    page.goto("https://www.google.com")


def test_CoreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.locator("#terms").check()
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("link",name="terms and conditions").click()
    page.get_by_role("button",name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_PracticeLocators(page:Page):
    page.goto("https://tutorialsninja.com/demo/index.php?route=account/register")
    page.locator("#input-firstname").fill("Bhavesh")
    page.locator("#input-lastname").fill("Rana")
    page.locator("#input-email").fill("brbhavesh63@gmail.com")
    page.locator("#input-telephone").fill("9884654421")
    page.locator("#input-password").fill("9886454698456")
    page.locator("#input-confirm").fill("9886454698456")
    page.get_by_label("Yes").click()
    page.locator("input[type='checkbox']").click()
    page.get_by_role("button",name="Continue").click()
    time.sleep(5)

def test_OpenFireFox(playwright:Playwright):
    firefoxBroswer = playwright.firefox.launch(headless=False)
    context = firefoxBroswer.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")


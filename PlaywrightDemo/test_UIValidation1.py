import time
import pytest
from playwright.sync_api import Page, expect


def test_UIValidationDynamicScript(playwright,page:Page):
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.locator("#password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.locator("#signInBtn").click()
    time.sleep(5)
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.locator("button").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.locator("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    time.sleep(2)
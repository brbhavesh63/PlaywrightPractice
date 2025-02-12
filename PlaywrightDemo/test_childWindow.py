from playwright.sync_api import Page


def test_childWindow(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")

    with page.expect_popup() as page_info:
        page.locator(".blinkingText").click()
        child_page = page_info.value
        text = child_page.locator(".red").text_content()
        print(text) #Please email us at mentor@rahulshettyacademy.com with below template to receive response
        words = text.split("at") # It will split the string in to two parts left side of 'at' and right side of 'at'
        # words[0] = #Please email us
        # words[1] = mentor@rahulshettyacademy.com with below template to receive response
        raw_emailContent = words[1].strip().split(" ") #it will split string to two parts left side of '{space}' and right side of '{space}'
        print(raw_emailContent)
        # we want left side of space means [0] index we want
        email = raw_emailContent[0] # strip() is used to trim begining and trailing space
        print(email)
        assert email == "mentor@rahulshettyacademy.com"

def test_childWindow2(page:Page):
    page.goto("https://the-internet.herokuapp.com/windows")

    with page.expect_popup() as page_info:
        page.locator("a[href='http://elementalselenium.com/']").click()
        child_page = page_info.value
        child_page.locator("a[href='/resources']").click()
        sentence = child_page.get_by_text("Written by one of the Selenium maintainers, Boni Garcia").text_content()
        print(sentence)
        name = sentence.split(",")[1].strip()
        assert name == 'Boni Garcia'

def test_childWindow3(playwright):
    browser = playwright.chromium.launch(headless=False , args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")

    with page.expect_popup() as page_pop:
        page.locator(".blinkingText").click()
        child_page = page_pop.value
        sentence = child_page.locator("text='An Academy to '").text_content()
        print(sentence)
        # An Academy to  Learn Earn & Shine in your QA Career
        newSent = sentence.split('to')[1].strip()
        act_text = newSent.split(" in")[0].strip()
        assert act_text == "Learn Earn & Shine"
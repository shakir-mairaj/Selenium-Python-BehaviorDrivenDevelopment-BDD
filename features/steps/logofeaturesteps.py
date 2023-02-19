from behave import *
from selenium import webdriver


@given('launch browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")


@when('open website homepage')
def openHomepage(context):
    context.driver.get("https://www.google.com/")


@then('Verify logo is present')
def verifyLogo(context):
    status = context.driver.find_element("xpath", '//body/div[1]/div[2]/div[1]/img[1]').is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()

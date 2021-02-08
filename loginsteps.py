from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch Chrome browser')
def step_1(context):
    context.driver = webdriver.Chrome(executable_path="C:\\Users\srini\PycharmProjects\BBC_Login\chromedriver.exe")
    context.driver.implicitly_wait(10)


@when('I open BBC Home page')
def step_2(context):
    context.driver.get("https://www.bbc.co.uk/news")
    context.driver.maximize_window()


@when('Enter username "{user}" and password "{pwd}"')
def step_3(context, user, pwd):
    context.driver.find_element_by_xpath("//*[@id='idcta-link']").click()
    context.driver.find_element_by_css_selector("#user-identifier-input").send_keys(user)
    context.driver.find_element_by_css_selector("#password-input").send_keys(pwd)


@when('Click login button')
def step_4(context):
    context.driver.find_element(By.ID, "submit-button").click()


@then('User must login to the Dashboard page')
def step_5(context):
    try:
        text = context.driver.find_element_by_xpath("//*[@id='idcta-username']").text

    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Your account":
        context.driver.close()
        assert True, "Test Passed"


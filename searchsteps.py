
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@given('a user on the main page')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="C:\\Users\srini\PycharmProjects\BBC_Login\chromedriver.exe")
    context.driver.get("https://www.bbc.co.uk/news")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


@when('the user enters valid information in the search bar')
def step_impl(context):
    context.driver.find_element(By.ID, "orb-search-q").send_keys("News")
    context.driver.implicitly_wait(5)


@then('the list of available data displayed is filtered by that information')
def step_impl(context):
    context.driver.find_element_by_css_selector("#orb-search-button").click()
    context.driver.implicitly_wait(5)
    context.driver.close()


@when('the information yields no results')
def step_impl(context):
    context.driver.get("https://www.bbc.co.uk/news")
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.ID, "orb-search-q").send_keys("onemillion")
    context.driver.implicitly_wait(10)


@then('some information is displayed to inform the search yielded no results')
def step_impl(context):
    context.driver.find_element_by_css_selector("#orb-search-button").click()
    context.driver.close()


@given('the information displayed is filtered by the search details')
def step_impl(context):
    context.driver.get("https://www.bbc.co.uk/news")
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.ID, "orb-search-q").send_keys("Sports")
    context.driver.implicitly_wait(5)


@when('the user clear the search')
def step_impl(context):
    context.driver.find_element_by_css_selector("#orb-search-button").click()
    context.driver.implicitly_wait(5)


@then('the full list of available data is displayed')
def step_impl(context):
    context.driver.find_element(By.ID, "search-input").clear()
    context.driver.implicitly_wait(5)
    context.driver.close()

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@given('Open https://gettop.us/ page')
def open_gettop(context):
    context.driver.get('https://gettop.us/')


@when('Clicking left arrow')
def click_left_right_arrows(context):
    context.app.topbanner.click_left_arrow()


@then('User can see top banner 1')
def verify_banner(context):
    context.app.topbanner.check_banner()


@when('Clicking right arrow')
def click_left_right_arrows(context):
    context.app.topbanner.click_right_arrow()


@then('User can see top banner 2')
def verify_banner(context):
    context.app.topbanner.check_banner2()


@when('Clicking bottom dots')
def click_bottom_dots(context):
    context.app.topbanner.click_bottomdots()


@then('Verify that each product banner is taking to a correct category page')
def matching_banners(context):
    context.app.topbanner.loop_ban_links()









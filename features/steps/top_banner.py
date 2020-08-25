from behave import given, when, then
from time import sleep


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


@when ('Clicking on product banner {expected}')
def click_ipad(context, expected):
    context.app.topbanner.click_ipad(expected)

@then ('User can see correct {expected} page')
def verify_category(context, expected):
    context.app.results_page.verify_result(expected)


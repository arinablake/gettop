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


BANNER_LINK = (By.CSS_SELECTOR, '.banner-link')
RESULTS_HEADER = (By.CSS_SELECTOR, '.woocommerce-breadcrumb.breadcrumbs.uppercase')


@then('Verify that each product banner is taking to a correct category page')
def matching_banners(context):
    # context.app.topbanner.verify_matching_banners()


    ban_links = context.driver.find_elements(*BANNER_LINK)

    for x in range(len(ban_links)):
        ban_to_click = context.driver.find_elements(*BANNER_LINK)[x]
        ban_text = ban_to_click.text
        ban_to_click.click()
        context.driver.wait.until(EC.visibility_of_element_located(RESULTS_HEADER))
        results_text = context.driver.find_element(*RESULTS_HEADER).text
        assert ban_text in results_text, f'Expected {ban_text} to be in {results_text}'
        context.driver.back()
        context.app.topbanner.click_left_arrow()









from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


TOP_NAV_LINKS = (By.CSS_SELECTOR, '.header-nav a.nav-top-link:not(.nav-top-not-logged-in)')
RESULTS_HEADER = (By.CSS_SELECTOR, '.woocommerce-breadcrumb.breadcrumbs.uppercase')

PROD_LIST = (By.CSS_SELECTOR, '.menu-item.menu-item-type-post_type.menu-item-object-product')
DROP_DOWN = (By.CSS_SELECTOR, '.sub-menu.nav-dropdown.nav-dropdown-default')


# @then('Verify that each product link is taking to a correct category page')
# def matching_banners(context):
#
#     prod_links = context.driver.find_elements(*TOP_NAV_LINKS)
#
#     for x in range(len(prod_links)):
#         prod_to_click = context.driver.find_elements(*TOP_NAV_LINKS)[x]
#         prod_text = prod_to_click.text
#         prod_to_click.click()
#         context.driver.wait.until(EC.visibility_of_element_located(RESULTS_HEADER))
#         results_text = context.driver.find_element(*RESULTS_HEADER).text
#         assert prod_text in results_text, f'Expected {prod_text} to be in {results_text}'
#         context.driver.back()


@then('Verify that hovering over each product user can see correct menu options')
def matching_banners(context):

    context.prod_links = context.driver.find_elements(*TOP_NAV_LINKS)
    print(len(context.prod_links))

    for x in range(len(context.prod_links)):
        context.prod_to_click = context.driver.find_elements(*TOP_NAV_LINKS)[x]
        prods = context.driver.find_elements(*PROD_LIST)
        print(len(prods))
        prod_text = context.prod_to_click.text
        prod_text = prod_text.lower()
        print(prod_text)
        context.driver.actions = ActionChains(context.driver)
        context.driver.actions.move_to_element(context.prod_to_click).perform()

        for x in range(len(prods)):
            prod_el = context.driver.find_elements(*PROD_LIST)[x]
            prod_el_text = prod_el.text
            prod_el_text = prod_el_text.lower()
            # print(prod_el_text)
            # print(prod_text)
            assert prod_el_text.find(prod_text) == True,  f'Expected {prod_text} to be in {prod_el_text}'
            # assert prod_text is in prod_el_text, f'Expected {prod_text} to be in {prod_el_text}'



#
# @when('User can select {expected} product from top menu and correct page opens')
# # def match_mac(context, expected):
# #     context.app.top_nav_menu.click_mac()
# #     context.app.results_page.verify_result(expected)
# #     context.driver.back()
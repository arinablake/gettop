from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PRODUCT = (By.CSS_SELECTOR, '.product_list_widget li')
PRICE = (By.CSS_SELECTOR, '.woocommerce-Price-amount.amount')
NAME = (By.CSS_SELECTOR, '.product-title')
STAR = (By.CSS_SELECTOR, '.star-rating')

FOOTER_PROD_LINKS = (By.CSS_SELECTOR, '.links.footer-nav.uppercase li')
ITEM = (By.CSS_SELECTOR, '.menu-item a')
RESULTS_HEADER = (By.CSS_SELECTOR, '.woocommerce-breadcrumb.breadcrumbs.uppercase')


@when('Footer shows {expected} categories')  #
def footer_cat(context, expected):
    context.app.footer_page.verify_footer_title(expected)


@when('All products in the footer have price, name, star-rating')
def verify_foot_prods(context):
    foot_prods = context.driver.find_elements(*PRODUCT)
    print(len(foot_prods))

    for x in range(len(foot_prods)):
        context.foot_prod = context.driver.find_elements(*PRODUCT)[x]
        foot_prod_price = context.foot_prod.find_elements(*PRICE)
        assert len(foot_prod_price) > 0
        foot_prod_name = context.foot_prod.find_elements(*NAME)
        assert len(foot_prod_name) > 0
        foot_prod_star = context.foot_prod.find_elements(*STAR)
        assert len(foot_prod_star) > 0


@when('{expected} shown in footer')
def verify_copyright(context, expected):
    context.app.footer_page.verify_copyright_text(expected)


@when('Footer has button to go back to top')
def verify_back_top_btn(context):
    context.app.footer_page.verify_back_to_top_btn()


@then('Footer has working links to all product categories')
def verify_foot_prod_links(context):
    foot_prod_links = context.driver.find_elements(*FOOTER_PROD_LINKS)
    print(len(foot_prod_links))

    for x in range(len(foot_prod_links)):
        context.foot_prod_link = context.driver.find_elements(*FOOTER_PROD_LINKS)[x]
        foot_prod_item = context.foot_prod_link.find_element(*ITEM)
        foot_prod_item_text = foot_prod_item.text
        foot_prod_item.click()
        # context.driver.wait.until(EC.visibility_of_element_located(RESULTS_HEADER)
        results_text = context.driver.find_element(*RESULTS_HEADER).text
        assert foot_prod_item_text in results_text, f'Expected {foot_prod_item_text} to be in {results_text}'
        context.driver.back()







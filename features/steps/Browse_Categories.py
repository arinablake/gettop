from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('{expected} text is shown 2')
def verify_section_title(context, expected):
    context.app.browse_cat.verify_browse_title(expected)


@when('{num} correct categories are shown')
def categories(context, num):
    context.app.browse_cat.verify_cat_number(num)


CAT_LINK = (By.CSS_SELECTOR, '.box-text.text-center .uppercase.header-title')
RESULTS_HEADER = (By.CSS_SELECTOR, '.woocommerce-breadcrumb.breadcrumbs.uppercase')


@then('Upon clicking on each category, correct page opens')
def matching_categories(context):
    context.app.browse_cat.loop_browse_cat()
    # cat_links = context.driver.find_elements(*CAT_LINK)
    #
    # for x in range(len(cat_links)):
    #     cat_to_click = context.driver.find_elements(*CAT_LINK)[x]
    #     cat_text = cat_to_click.text
    #     cat_to_click.click()
    #     context.driver.wait.until(EC.visibility_of_element_located(RESULTS_HEADER))
    #     results_text = context.driver.find_element(*RESULTS_HEADER).text
    #     assert cat_text in results_text, f'Expected {cat_text} to be in {results_text}'
    #     context.driver.back()
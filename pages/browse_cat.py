from pages.base_page import Page
from selenium.webdriver.common.by import By


class BrowseCat(Page):
    TITLE_BROWSE = (By.CSS_SELECTOR, '#content > div:nth-child(5)')
    CAT_BOX = (By.CSS_SELECTOR, '.box-category')

    CAT_LINK = (By.CSS_SELECTOR, '.box-text.text-center .uppercase.header-title')
    RESULTS_HEADER = (By.CSS_SELECTOR, '.woocommerce-breadcrumb.breadcrumbs.uppercase')

    def verify_browse_title(self, expected_text: str):
        self.verify_text(expected_text, *self.TITLE_BROWSE)

    def verify_cat_number(self, num: int):
        self.verify_number(num, *self.CAT_BOX)

    def loop_browse_cat(self):
        cat_links = self.driver.find_elements(*self.CAT_LINK)

        for x in range(len(cat_links)):
            cat_to_click = self.driver.find_elements(*self.CAT_LINK)[x]
            cat_text = cat_to_click.text
            cat_to_click.click()
            self.wait_for_element_located(*self.RESULTS_HEADER)
            results_text = self.driver.find_element(*self.RESULTS_HEADER).text
            assert cat_text in results_text, f'Expected {cat_text} to be in {results_text}'
            self.driver.back()





from pages.base_page import Page
from selenium.webdriver.common.by import By


class ResultsPage(Page):
    RESULTS_HEADER = (By.CSS_SELECTOR, '.woocommerce-breadcrumb.breadcrumbs.uppercase')
    COM_INFO = (By.CSS_SELECTOR, '.woocommerce-info')
    EMPTY_CART = (By.CSS_SELECTOR, '.cart-empty.woocommerce-info')

    def verify_result(self, expected_text: str):
        self.verify_text(expected_text, *self.RESULTS_HEADER)

    def verify_ne_prod(self, expected_text: str):
        self.verify_text(expected_text, *self.COM_INFO)

    def verify_empty_cart(self, expected_text: str):
        self.verify_text(expected_text.lower(), *self.EMPTY_CART)



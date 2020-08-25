from pages.base_page import Page
from selenium.webdriver.common.by import By


class ResultsPage(Page):
    RESULTS_HEADER = (By.CSS_SELECTOR, '.woocommerce-breadcrumb.breadcrumbs.uppercase')


    def verify_result(self, expected_text: str):
        self.verify_text(expected_text, *self.RESULTS_HEADER)





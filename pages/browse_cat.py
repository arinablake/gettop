from pages.base_page import Page
from selenium.webdriver.common.by import By


class BrowseCat(Page):
    TITLE_BROWSE = (By.CSS_SELECTOR, '#content > div:nth-child(5)')
    CAT_BOX = (By.CSS_SELECTOR, '.box-category')

    def verify_browse_title(self, expected_text: str):
        self.verify_text(expected_text, *self.TITLE_BROWSE)

    def verify_cat_number(self, num: int):
        self.verify_number(num, *self.CAT_BOX)





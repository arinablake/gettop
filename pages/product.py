from pages.base_page import Page
from selenium.webdriver.common.by import By


class Product(Page):
    PRICE = (By.CSS_SELECTOR, '.woocommerce-Price-amount.amount')
    DESCRIPTION = (By.CSS_SELECTOR, '.product-short-description')
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.button[name="add-to-cart"]')

    def click_add_t_c_btn(self):
        self.click(*self.ADD_TO_CART_BTN)

    def verify_price(self):
        self.wait_for_element_appear(*self.PRICE)

    def verify_description(self):
        self.wait_for_element_appear(*self.DESCRIPTION)
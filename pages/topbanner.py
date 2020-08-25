# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from pages.base_page import Page


class TopBanner(Page):
    LEFT_ARROW = (By.CSS_SELECTOR, '.slider-wrapper.relative .flickity-button.flickity-prev-next-button.previous')
    RIGHT_ARROW = (By.CSS_SELECTOR,'.slider-wrapper.relative .flickity-button.flickity-prev-next-button.next')
    BANNER1 = (By.CSS_SELECTOR, '.banner.has-hover.is-selected')
    BANNER2 = (By.CSS_SELECTOR, '.banner.has-hover.is-selected')
    BOTTOMDOT = (By.CSS_SELECTOR, '.dot[aria-label="Page dot 2"]')
    IPAD = (By.CSS_SELECTOR, 'a[href="/product-category/ipad/"]')
    MAC = (By.CSS_SELECTOR, 'a[href="/product-category/macbook/"]')


    def click_left_arrow(self):
        self.click(*self.LEFT_ARROW)

    def click_right_arrow(self):
        self.click(*self.RIGHT_ARROW)

    def check_banner(self):
        self.wait_for_element_appear(*self.BANNER1)

    def check_banner2(self):
        self.wait_for_element_appear(*self.BANNER2)

    def click_bottomdots(self):
        self.click(*self.BOTTOMDOT)

    def click_ipad(self):
        self.click(*self.IPAD)

    def click_macbook(self):
        self.click(*self.MACBOOK)
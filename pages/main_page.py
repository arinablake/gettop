from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    ORDERS = (By.XPATH, "//span[@class='nav-line-2'][text()='& Orders']")
    SC_LOCATOR = (By.CSS_SELECTOR, "#nav-cart")
    HAM_MENU = (By.CSS_SELECTOR, "#nav-hamburger-menu")
    AM_LINK = (By.CSS_SELECTOR, "#hmenu-content > ul.hmenu.hmenu-visible > li:nth-child(3) > a")

    def click_link(self):
        self.click(*self.ORDERS)

    def click_icon(self):
        self.click(*self.SC_LOCATOR)

    def click_h_menu(self):
        self.click(*self.HAM_MENU)

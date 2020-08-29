from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from pages.base_page import Page


class TopNavMenu(Page):
    LOGO = (By.CSS_SELECTOR, '#logo > a')
    SEARCH_ICON = (By.CSS_SELECTOR, '.header-search .icon-search')
    SEARCH_FIELD = (By.CSS_SELECTOR, '#woocommerce-product-search-field-0')
    SUBMIT_ICON = (By.CSS_SELECTOR, '.ux-search-submit.submit-button.secondary .icon-search')

    MAC_LINK = (By.CSS_SELECTOR, '#menu-item-468 a.nav-top-link')



    def click_logo(self):
        self.click(*self.LOGO)

    def verify_page(self, expected_url):
        self.verify_url("https://gettop.us/")

    def hover_icon(self):
        search_ic = self.find_element(*self.SEARCH_ICON)
        self.actions.move_to_element(search_ic).perform()

    def check_search_field(self):
        self.wait_for_element_appear(*self.SEARCH_FIELD)

    def search_word(self, search_word):
        self.input(search_word, *self.SEARCH_FIELD)
        self.click(*self.SUBMIT_ICON)

    def click_mac(self):
        self.click(*self.MAC_LINK)

    # SEARCH_INPUT = (By.ID, "twotabsearchtextbox")
    # SEARCH_SUBMIT = (By.XPATH, "//input[@value='Go']")
    # SELECT_DEPARTMENT = (By.ID, "searchDropdownBox")
    # DISPLAYED_DEPARTMENT = (By.CSS_SELECTOR, 'div#nav-subnav a.nav-b')

    # def search_word(self, search_word):
    #     self.input(search_word, *self.SEARCH_INPUT)
    #     self.click(*self.SEARCH_SUBMIT)
    #
    # def select_department(self, alias):
    #     dep_selection_element = self.find_element(*self.SELECT_DEPARTMENT)
    #     select = Select(dep_selection_element)
    #     select.select_by_value(f'search-alias={alias}')
    #     # select.select_by_index(index)
    #     # select.select_by_visible_text('text')
    #
    # def verify_selected_department(self, selected_dep):
    #     self.verify_text(selected_dep, *self.DISPLAYED_DEPARTMENT)

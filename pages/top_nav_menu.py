from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from pages.base_page import Page


class TopNavMenu(Page):
    LOGO = (By.CSS_SELECTOR, '#logo > a')
    SEARCH_ICON = (By.CSS_SELECTOR, '.header-search .icon-search')
    SEARCH_FIELD = (By.CSS_SELECTOR, '#woocommerce-product-search-field-0')
    SUBMIT_ICON = (By.CSS_SELECTOR, '.ux-search-submit.submit-button.secondary .icon-search')

    MAC_LINK = (By.CSS_SELECTOR, '#menu-item-468 a.nav-top-link')

    USER_ICON = (By.CSS_SELECTOR, '.icon-user')
    LOGIN_FORM = (By.CSS_SELECTOR, '.account-login-inner')
    CART_ICON = (By.CSS_SELECTOR, '.cart-item.has-icon.has-dropdown .cart-icon.image-icon')
    EMPTY_CART_WIDGET = (By.CSS_SELECTOR, '.woocommerce-mini-cart__empty-message')

    CART_WIDGET = (By.CSS_SELECTOR, '.widget_shopping_cart_content')

    CART_PRICE = (By.CSS_SELECTOR, '.cart-price .woocommerce-Price-amount.amount')
    WIDGET_ITEM_PRICE = (By.CSS_SELECTOR, '.woocommerce-mini-cart-item.mini_cart_item .woocommerce-Price-amount.amount')
    WIDGET_ITEM_AMOUNT = (By.CSS_SELECTOR, '.quantity:not(.woocommerce-Price-currencySymbol)') #'.quantity')

    WIDGET_ITEM = (By.CSS_SELECTOR, '.woocommerce-mini-cart-item.mini_cart_item')
    WIDGET_SUBTOTAL = (By.CSS_SELECTOR, '.woocommerce-mini-cart__total.total')

    VIEW_CART_BTN = (By.CSS_SELECTOR, '.woocommerce-mini-cart__buttons.buttons > a:nth-child(1)')
    CHECKOUT_BTN = (By.CSS_SELECTOR, '.woocommerce-mini-cart__buttons.buttons > a.button.checkout.wc-forward')
    REMOVE_BTN = (By.CSS_SELECTOR, '.remove.remove_from_cart_button')

    CART_ICON_1 = (By.CSS_SELECTOR, '.cart-item.has-icon.has-dropdown .cart-icon.image-icon')


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

    def click_user_icon(self):
        self.click(*self.USER_ICON)

    def check_login_form(self):
        self.wait_for_element_appear(*self.LOGIN_FORM)

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

    def hover_cart_icon(self):
        sh_cart_icon = self.find_element(*self.CART_ICON)
        self.actions.move_to_element(sh_cart_icon).perform()

    def check_empty_cart_widget(self):
        self.wait_for_element_appear(*self.EMPTY_CART_WIDGET)

    def check_cart_widget(self):
        self.wait_for_element_appear(*self.CART_WIDGET)

    def verify_cart_widget(self, expected_text: str):
        self.verify_text(expected_text.capitalize(), *self.CART_WIDGET)

    def verify_price_text(self):
        cart_text = self.driver.find_element(*self.CART_PRICE).text
        cart_widget_text = self.driver.find_element(*self.WIDGET_ITEM_PRICE).text
        # print(cart_text)
        # print(cart_widget_text)
        assert cart_text in cart_widget_text, f'Expected text {cart_text}, but got {cart_widget_text}'

    def verify_item_amount_text(self):
        ci_item_amount_text = self.driver.find_element(*self.CART_ICON).text
        cart_widget_text = self.driver.find_element(*self.WIDGET_ITEM_AMOUNT).text
        print(ci_item_amount_text)
        print(cart_widget_text)
        assert ci_item_amount_text in cart_widget_text, f'Expected text {ci_item_amount_text}, but got {cart_widget_text}'

    def verify_item_subtotal(self):
        self.find_element(*self.WIDGET_ITEM)
        self.find_element(*self.WIDGET_SUBTOTAL)


    def verify_cart_page(self, expected_url):
        self.wait_for_element_appear(*self.WIDGET_ITEM)
        self.click(*self.VIEW_CART_BTN)
        self.verify_url("https://gettop.us/cart/")

    def verify_checkout_page(self, expected_url):
        self.wait_for_element_appear(*self.WIDGET_ITEM)
        self.click(*self.CHECKOUT_BTN)
        self.verify_url("https://gettop.us/checkout/")

    def remove_from_cart(self):
        self.wait_for_element_appear(*self.WIDGET_ITEM)
        self.click(*self.REMOVE_BTN)

    def hover_cart_icon1(self):
        s_cart_icon = self.find_element(*self.CART_ICON_1)
        self.actions.move_to_element(s_cart_icon).perform()



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

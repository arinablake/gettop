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

    # CART_ICON_1 = (By.CSS_SELECTOR, '.cart-item.has-icon.has-dropdown .cart-icon.image-icon')

    TOP_NAV_LINKS = (By.CSS_SELECTOR, '.header-nav a.nav-top-link:not(.nav-top-not-logged-in)')
    RESULTS_HEADER = (By.CSS_SELECTOR, '.woocommerce-breadcrumb.breadcrumbs.uppercase')

    PROD_LIST = (By.CSS_SELECTOR, '.menu-item.menu-item-type-post_type.menu-item-object-product a')
    DROP_DOWN = (By.CSS_SELECTOR, '.sub-menu.nav-dropdown.nav-dropdown-default')


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

    # def hover_cart_icon1(self):
    #     s_cart_icon = self.find_element(*self.CART_ICON_1)
    #     self.actions.move_to_element(s_cart_icon).perform()

    def loop_prod_cat(self):
        prod_links = self.driver.find_elements(*self.TOP_NAV_LINKS)

        for x in range(len(prod_links)):
            prod_to_click = self.driver.find_elements(*self.TOP_NAV_LINKS)[x]
            prod_text = prod_to_click.text
            prod_to_click.click()
            self.wait_for_element_located(*self.RESULTS_HEADER)
            results_text = self.driver.find_element(*self.RESULTS_HEADER).text
            assert prod_text in results_text, f'Expected {prod_text} to be in {results_text}'
            self.driver.back()

    # def loop_hover_prod_cat(self):
    #     prod_links = self.driver.find_elements(*self.TOP_NAV_LINKS)
    #
    #     for x in range(len(prod_links)):
    #         prod_to_click = self.driver.find_elements(*self.TOP_NAV_LINKS)[x]
    #         prod_text = prod_to_click.text
    #         prod_text = prod_text.lower()
    #         self.actions.move_to_element(prod_to_click).perform()
    #
    #         # drop_ds = self.driver.find_elements(*self.DROP_DOWN)
    #         drop_d = self.driver.find_elements(*self.DROP_DOWN)[x]
    #         prod_els = drop_d.find_elements(*self.PROD_LIST)
    #
    #         for x in range(len(prod_els)):
    #             prod_el = drop_d.find_elements(*self.PROD_LIST)[x]
    #             prod_el_text = prod_el.text
    #             prod_el_text = prod_el_text.lower()
    #             if prod_text == 'accessories' and prod_el_text == 'airpods with wireless charging case' or prod_el_text == 'airpods pro':
    #                 pass
    #             else:
    #                 assert prod_text in prod_el_text, f'Expected {prod_text} to be in {prod_el_text}'




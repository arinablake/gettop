from pages.base_page import Page
from selenium.webdriver.common.by import By


class Product(Page):
    PRICE = (By.CSS_SELECTOR, '.woocommerce-Price-amount.amount')
    DESCRIPTION = (By.CSS_SELECTOR, '.product-short-description')
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.button[name="add-to-cart"]')
    PROD_CART_BTN = (By.CSS_SELECTOR, '.single_add_to_cart_button.button.alt')


    TOP_NAV_LINKS = (By.CSS_SELECTOR, '.header-nav a.nav-top-link:not(.nav-top-not-logged-in)')
    RESULTS_HEADER = (By.CSS_SELECTOR, '.woocommerce-breadcrumb.breadcrumbs.uppercase')

    PROD_LIST = (By.CSS_SELECTOR, '.menu-item.menu-item-type-post_type.menu-item-object-product a')
    DROP_DOWN = (By.CSS_SELECTOR, '.sub-menu.nav-dropdown.nav-dropdown-default')

    IMAGE = (By.CSS_SELECTOR, '.woocommerce-product-gallery__image')
    NAME = (By.CSS_SELECTOR, '.product-title.product_title.entry-title')

    ZOOM_ICON = (By.CSS_SELECTOR, '.icon-expand')
    Z_ICON = (By.CSS_SELECTOR, '.pswp__button.pswp__button--zoom')
    Z_IMG = (By.CSS_SELECTOR, 'img.pswp__img')
    Z_RIGHT_ARROW = (By.CSS_SELECTOR, '.pswp__button--arrow--right')
    Z_LEFT_ARROW = (By.CSS_SELECTOR, '.pswp__button--arrow--left')
    Z_CLOSE = (By.CSS_SELECTOR, '.pswp__button.pswp__button--close')

    HEART_ICON = (By.CSS_SELECTOR, '.icon-heart')
    # WISHLIST_ADDED = (By.CSS_SELECTOR, '#yith-wcwl-message')

    PROD_IMAGE = (By.CSS_SELECTOR, '.wp-post-image.skip-lazy')
    HOME_LINK = (By.CSS_SELECTOR, '.woocommerce-breadcrumb.breadcrumbs.uppercase a:nth-child(1)')
    CAT_LINK = (By.CSS_SELECTOR, '.woocommerce-breadcrumb.breadcrumbs.uppercase a:nth-child(3)')

    CART_PLUS = (By.CSS_SELECTOR, '.plus.button.is-form')
    CART_MINUS = (By.CSS_SELECTOR, '.minus.button.is-form')
    QTY_INPUT = (By.CSS_SELECTOR, '.input-text.qty.text')
    CART_ICON = (By.CSS_SELECTOR, '.cart-item.has-icon.has-dropdown .cart-icon.image-icon')
    ADD_CART_CONFIRMATION = (By.CSS_SELECTOR, '.message-container.container.success-color.medium-text-center')

    PROD_RIGHT_ARROW = (By.CSS_SELECTOR, '#product-sidebar > div > ul > li:nth-child(1) > a')
#'.button.icon.is-outline.circle .icon-angle-right')
    PROD_LEFT_ARROW = (By.CSS_SELECTOR, '#product-sidebar > div > ul > li > a')
 #'.button.icon.is-outline.circle .icon-angle-left')
    OUT_OF_STOCK = (By.CSS_SELECTOR, '.stock.out-of-stock')


    def click_add_t_c_btn(self):
        self.click(*self.ADD_TO_CART_BTN)

    def click_prod_add_tc(self):
        self.click(*self.PROD_CART_BTN)

    def verify_price(self):
        self.wait_for_element_appear(*self.PRICE)

    def verify_description(self):
        self.wait_for_element_appear(*self.DESCRIPTION)

    def open_prod(self):
        prod_to_click = self.driver.find_elements(*self.TOP_NAV_LINKS)[0]
        self.actions.move_to_element(prod_to_click).perform()
        drop_d = self.driver.find_elements(*self.DROP_DOWN)[0]
        prod_el = drop_d.find_elements(*self.PROD_LIST)[0]
        prod_el.click()

    def verify_prod(self):
        prod_img = self.driver.find_elements(*self.IMAGE)
        assert len(prod_img) > 0
        prod_name = self.driver.find_elements(*self.NAME)
        assert len(prod_name) > 0
        prod_price = self.driver.find_elements(*self.PRICE)
        assert len(prod_price) > 0
        prod_description = self.driver.find_elements(*self.DESCRIPTION)
        assert len(prod_description) > 0

    def click_zoom_icn(self):
        self.click(*self.ZOOM_ICON)

    def click_z_icon(self):
        self.click(*self.Z_ICON)

    def verify_z_img(self):
        self.wait_for_element_appear(*self.Z_IMG)

    def click_z_img(self):
        self.click(*self.Z_IMG)

    def click_z_right_arrow(self):
        self.click(*self.Z_RIGHT_ARROW)

    def click_z_left_arrow(self):
        self.click(*self.Z_LEFT_ARROW)

    def click_z_close(self):
        self.click(*self.Z_CLOSE)

    def hover_prod_image(self):
        self.wait_for_element_appear(*self.PROD_IMAGE)
        m_prod_img = self.driver.find_element(*self.PROD_IMAGE)
        self.actions.move_to_element(m_prod_img).perform()
        m_prod_hi = self.driver.find_element(*self.HEART_ICON)
        self.actions.move_to_element(m_prod_hi).perform()

    def click_heart_icon(self):
        self.click(*self.HEART_ICON)

    # def check_wishlist(self):
    #     self.wait_for_element_appear(*self.WISHLIST_ADDED)

    def click_home_link(self):
        self.click(*self.HOME_LINK)

    def click_cat_link(self):
        cat_link = self.driver.find_element(*self.CAT_LINK)
        cat_link_text = cat_link.text
        self.click(*self.CAT_LINK)
        # results_text = self.driver.find_element(*self.RESULTS_HEADER).text
        # assert cat_link_text in results_text, f'Expected {cat_link_text} to be in {results_text}'
        self.verify_text(cat_link_text, *self.RESULTS_HEADER)

    def click_cart_plus(self):
        self.click(*self.CART_PLUS)

    def click_cart_minus(self):
        self.click(*self.CART_MINUS)

    def get_qty_input(self):
        qty_num = self.driver.find_element(*self.QTY_INPUT)
        qty_num_text = qty_num.text

    def verify_cart_item_amount_text(self):
        qty_num = self.driver.find_element(*self.QTY_INPUT)
        qty_num_text = qty_num.text
        ci_item_amount_text = self.driver.find_element(*self.CART_ICON).text
        print(ci_item_amount_text)
        assert qty_num_text in ci_item_amount_text, f'Expected text {qty_num_text}, but got {ci_item_amount_text}'

    def qty_input(self, num):
        self.input(num, *self.QTY_INPUT)

    def verify_add_to_cart_confirm(self):
        self.wait_for_element_appear(*self.ADD_CART_CONFIRMATION)

    def click_prod_right_arrow(self):
        self.click(*self.PROD_RIGHT_ARROW)

    def click_prod_left_arrow(self):
        self.click(*self.PROD_LEFT_ARROW)

    def verify_out_of_stock(self, expected):
        self.verify_text(expected.capitalize(), *self.OUT_OF_STOCK)

    def verify_out_of_stock_btns(self):
        atc_btn = self.driver.find_elements(*self.PROD_CART_BTN)
        assert len(atc_btn) == 0


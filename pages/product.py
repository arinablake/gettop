from pages.base_page import Page
from selenium.webdriver.common.by import By


class Product(Page):
    PRICE = (By.CSS_SELECTOR, '.woocommerce-Price-amount.amount')
    DESCRIPTION = (By.CSS_SELECTOR, '.product-short-description')
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.button[name="add-to-cart"]')

    TOP_NAV_LINKS = (By.CSS_SELECTOR, '.header-nav a.nav-top-link:not(.nav-top-not-logged-in)')
    RESULTS_HEADER = (By.CSS_SELECTOR, '.woocommerce-breadcrumb.breadcrumbs.uppercase')

    PROD_LIST = (By.CSS_SELECTOR, '.menu-item.menu-item-type-post_type.menu-item-object-product a')
    DROP_DOWN = (By.CSS_SELECTOR, '.sub-menu.nav-dropdown.nav-dropdown-default')

    IMAGE = (By.CSS_SELECTOR, '.woocommerce-product-gallery__image')
    NAME = (By.CSS_SELECTOR, '.product-title.product_title.entry-title')

    ZOOM_ICON = (By.CSS_SELECTOR, '.icon-expand')
    Z_IMG = (By.CSS_SELECTOR, 'img.pswp__img')
    Z_RIGHT_ARROW = (By.CSS_SELECTOR, '.pswp__button--arrow--right')
    Z_LEFT_ARROW = (By.CSS_SELECTOR, '.pswp__button--arrow--left')
    Z_CLOSE = (By.CSS_SELECTOR, '.pswp__button.pswp__button--close')

    HEART_ICON = (By.CSS_SELECTOR, '.icon-heart')
    WISHLIST_ADDED = (By.CSS_SELECTOR, '#yith-wcwl-message')

    # IMAGE1 = (By.CSS_SELECTOR, '.wp-post-image.skip-lazy')



    def click_add_t_c_btn(self):
        self.click(*self.ADD_TO_CART_BTN)

    def verify_price(self):
        self.wait_for_element_appear(*self.PRICE)

    def verify_description(self):
        self.wait_for_element_appear(*self.DESCRIPTION)

    def verify_prod(self):
        prod_to_click = self.driver.find_elements(*self.TOP_NAV_LINKS)[0]
        self.actions.move_to_element(prod_to_click).perform()
        drop_d = self.driver.find_elements(*self.DROP_DOWN)[0]
        prod_el = drop_d.find_elements(*self.PROD_LIST)[0]
        prod_el.click()
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

    def hover_image(self):
        prod_img = self.driver.find_element(*self.IMAGE)
        # prod_image = self.find_element(*self.IMAGE1)
        self.actions.move_to_element(prod_img).perform()

    def click_heart_icon(self):
        self.click(*self.HEART_ICON)

    def check_wishlist(self):
        self.wait_for_element_appear(*self.WISHLIST_ADDED)




from pages.base_page import Page
from selenium.webdriver.common.by import By


class LatestProd(Page):
    TITLE = (By.CSS_SELECTOR, ' .section-title-main')
    PRODUCT = (By.CSS_SELECTOR, '.product-small.box')
    SALE_ICON = (By.CSS_SELECTOR, '.badge-container')
    IMAGE = (By.CSS_SELECTOR, '.box-image')
    CATEGORY = (By.CSS_SELECTOR, '.category')
    NAME = (By.CSS_SELECTOR, '.name')
    PRICE = (By.CSS_SELECTOR, '.woocommerce-Price-amount.amount')
    STAR_RATING = (By.CSS_SELECTOR, '.star-rating')

    HEART_ICON = (By.CSS_SELECTOR, '.icon-heart')
    WISHLIST_ADDED = (By.CSS_SELECTOR, '#yith-wcwl-message')
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.single_add_to_cart_button')    #'.button[name="add-to-cart"]')
    QUICK_VIEW_BTN = (By.CSS_SELECTOR, '.quick-view.quick-view-added')
    QV_WINDOW = (By.CSS_SELECTOR, '.product-quick-view-container')
    CLOSE_QV = (By.CSS_SELECTOR, '.mfp-close')
    QV_NEXT_ARROW = (By.CSS_SELECTOR, '.product-gallery-slider .flickity-button.flickity-prev-next-button.next')
    QV_PREV_ARROW = (By.CSS_SELECTOR, '.product-gallery-slider .flickity-button.flickity-prev-next-button.previous')



    def verify_title(self, expected_text: str):
        self.verify_text(expected_text, *self.TITLE)

    def click_heart_icon(self):
        self.click(*self.HEART_ICON)

    def check_wishlist(self):
        self.wait_for_element_appear(*self.WISHLIST_ADDED)

    def click_image(self):
        self.click(*self.IMAGE)

    def hover_image(self):
        prod_image = self.find_element(*self.IMAGE)
        self.actions.move_to_element(prod_image).perform()

    def click_quick_view(self):
        self.click(*self.QUICK_VIEW_BTN)

    def check_qv_window(self):
        self.wait_for_element_appear(*self.QV_WINDOW)

    def close_qv(self):
        self.click(*self.CLOSE_QV)

    def click_add_to_cart_btn(self):
        self.click(*self.ADD_TO_CART_BTN)

    def click_next_arrow(self):
        self.click(*self.QV_NEXT_ARROW)

    def click_prev_arrow(self):
        self.click(*self.QV_PREV_ARROW)


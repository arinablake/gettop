# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from pages.base_page import Page


class TopBanner(Page):
    LEFT_ARROW = (By.CSS_SELECTOR, '.slider-wrapper.relative .flickity-button.flickity-prev-next-button.previous')
    RIGHT_ARROW = (By.CSS_SELECTOR, '.slider-wrapper.relative .flickity-button.flickity-prev-next-button.next')
    BANNER1 = (By.CSS_SELECTOR, '.banner.has-hover.is-selected')
    BANNER2 = (By.CSS_SELECTOR, '.banner.has-hover.is-selected')
    BOTTOMDOT = (By.CSS_SELECTOR, '.dot[aria-label="Page dot 2"]')


    # BANNER_LINK = (By.CSS_SELECTOR, '.banner-link')
    # RESULTS_HEADER = (By.CSS_SELECTOR, '.woocommerce-breadcrumb.breadcrumbs.uppercase')



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

    def click_banner(self):
        self.click(*self.BANNER_LINK)

    # def verify_matching_banners(self):
    #     ban_links = self.driver.find_elements(*BANNER_LINK)
    #
    #     for x in range(len(ban_links)):
    #         ban_to_click = self.driver.find_elements(*BANNER_LINK)[x]
    #         ban_text = ban_to_click.text
    #         ban_to_click.click()
    #         self.driver.wait.until(EC.visibility_of_element_located(RESULTS_HEADER))
    #         results_text = self.driver.find_element(*RESULTS_HEADER).text
    #         assert ban_text in results_text, f'Expected {ban_text} to be in {results_text}'
    #         self.driver.back()
    #         self.app.topbanner.click_left_arrow()

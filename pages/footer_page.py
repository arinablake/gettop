from pages.base_page import Page
from selenium.webdriver.common.by import By


class Footer(Page):
    FOOTER_TITLE = (By.CSS_SELECTOR, '.widget-title')
    COPYRIGHT_FOOTER = (By.CSS_SELECTOR, '.copyright-footer')
    BACK_TOP_BTN = (By.CSS_SELECTOR, '.back-to-top.button.icon')

    def verify_footer_title(self, expected_text: str):
        foot_titles = self.driver.find_elements(*self.FOOTER_TITLE)

        for x in range(len(foot_titles)):
            foot_title = self.driver.find_elements(*self.FOOTER_TITLE)[x]
            foot_title_text = foot_title.text
            print(foot_title_text)
            assert foot_title_text in expected_text.upper(), f'Expected {foot_title_text} to be in {expected_text.upper()}'

    def verify_copyright_text(self, expected_text: str):
        self.verify_text(expected_text, *self.COPYRIGHT_FOOTER)

    def verify_back_to_top_btn(self):
        self.find_element(*self.BACK_TOP_BTN)


#         self.verify_text(expected_text.upper(), *self.FOOTER_TITLE)
#
#
# cat_links = self.driver.find_elements(*self.CAT_LINK)
#
#         for x in range(len(cat_links)):
#             cat_to_click = self.driver.find_elements(*self.CAT_LINK)[x]
#             cat_text = cat_to_click.text
#             cat_to_click.click()
#             self.wait_for_element_located(*self.RESULTS_HEADER)
#             results_text = self.driver.find_element(*self.RESULTS_HEADER).text
#             assert cat_text in results_text, f'Expected {cat_text} to be in {results_text}'
#             self.driver.back()

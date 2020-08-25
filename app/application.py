from pages.base_page import Page
from pages.topbanner import TopBanner
from pages.results_page import ResultsPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.page = Page(self.driver)
        self.topbanner = TopBanner(self.driver)
        self.results_page = ResultsPage(self.driver)


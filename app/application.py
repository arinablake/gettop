from pages.base_page import Page
from pages.topbanner import TopBanner
from pages.results_page import ResultsPage
from pages.latest_prod import LatestProd
from pages.product import Product


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.page = Page(self.driver)
        self.topbanner = TopBanner(self.driver)
        self.results_page = ResultsPage(self.driver)
        self.latest_prod = LatestProd(self.driver)
        self.product = Product(self.driver)


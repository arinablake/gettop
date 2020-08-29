from pages.base_page import Page
from pages.topbanner import TopBanner
from pages.results_page import ResultsPage
from pages.latest_prod import LatestProd
from pages.product import Product
from pages.browse_cat import BrowseCat
from pages.top_nav_menu import TopNavMenu


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.page = Page(self.driver)
        self.topbanner = TopBanner(self.driver)
        self.results_page = ResultsPage(self.driver)
        self.latest_prod = LatestProd(self.driver)
        self.product = Product(self.driver)
        self.browse_cat = BrowseCat(self.driver)
        self.top_nav_menu = TopNavMenu(self.driver)


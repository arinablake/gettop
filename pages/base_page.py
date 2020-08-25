from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver): 
        self.driver = driver
        self.base_url = 'https://gettop.us/'
        self.driver.wait = WebDriverWait(self.driver, 15)
        self.actions = ActionChains(self.driver)

    def open_page(self, url=''):
        self.driver.get(self.base_url + url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def input(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def wait_for_element_click(self, *locator):
        e = self.driver.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.driver.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_located(self, *locator):
        self.driver.wait.until(EC.visibility_of_all_elements_located(locator))

    def verify_text(self, expected_text: str, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f'Expected text {expected_text}, but got {actual_text}'

    def verify_number(self, num: int, *locator):
        actual_num_list = self.driver.find_elements(*locator)
        assert (len(actual_num_list)) == int(num), f'Expected {num}, but got {len(actual_num_list)}'

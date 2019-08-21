from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.expected_conditions import (
    visibility_of_element_located
)
from selenium.webdriver.support.ui import WebDriverWait

class SearchOverlay:

    def __init__(self, driver, env):
        self.driver = driver
        self.env = env
        self.timeout = self.env['timeout']

    @property
    def url(self):
        return self.env['site']

    locators = {
        'root_element': (By.CSS_SELECTOR, '.search-container > form'),
        'search_field': (By.CSS_SELECTOR, '.form-fluid'),
    }

    def wait_for_load(self):
        WebDriverWait(driver=self.driver, timeout=self.timeout).until(
            visibility_of_element_located(
                locator=self.locators['root_element']
            )
        )

    def enter_search_query(self, query):
        search_field = self.driver.find_element(
            *self.locators['search_field'])
        search_field.send_keys(query)

    def submit_search_query(self):
        search_field = self.driver.find_element(
            *self.locators['search_field'])
        search_field.submit()
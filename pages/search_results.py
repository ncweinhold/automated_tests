from helpers.yaml_helpers import get_expected_text
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.expected_conditions import (
    visibility_of_element_located
)
from selenium.webdriver.support.ui import WebDriverWait

class SearchResultsPage:

    def __init__(self, driver, env):
        self.driver = driver
        self.env = env
        self.timeout = self.env['timeout']

    @property
    def url(self):
        return self.env['site']

    EXPECTED_SEARCH_RESULTS_TEXT_FILE = 'search_results.yaml'

    locators = {
        'root_element': (By.CSS_SELECTOR, '.search'),
        'heading_text': (By.CSS_SELECTOR, 'div.heading-text'),
        'nothing_found_heading': (By.CSS_SELECTOR, 'h1.post-title'),
        'nothing_found_text': (By.CSS_SELECTOR, 'div.page-content > p'),
        'search_result': (By.CSS_SELECTOR, 'div.tmb')
    }

    def wait_for_load(self):
        WebDriverWait(driver=self.driver, timeout=self.timeout).until(
            visibility_of_element_located(
                locator=self.locators['root_element']
            )
        )

    def results_heading_is_displayed(self):
        return self.driver.find_element(
            *self.locators['heading_text']).is_displayed()
    
    def results_were_found(self):
        try:
            return self.driver.find_element(
                *self.locators['search_result']).is_displayed()
        except NoSuchElementException:
            return False
    
    def no_results_were_found(self):
        try:
            return self.driver.find_element(
                *self.locators['nothing_found_heading']).is_displayed()
        except NoSuchElementException:
            return False

    def get_expected_no_results_message(self):
        return get_expected_text(
            file_name=self.EXPECTED_SEARCH_RESULTS_TEXT_FILE, 
            text='no_results_found')


    def get_no_results_message(self):
        return self.driver.find_element(
            *self.locators['nothing_found_text']).text
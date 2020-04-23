from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from utility.logger import Logger
from data.testdata import TestConst as tc


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    logs = Logger()

    def check_element_is_on_page(self, locator):
        self.logs.info(self.logs.locator_check_message(locator))
        try:
            WebDriverWait(self.driver, tc.wait_time).until(ec.presence_of_element_located(locator))
            self.logs.info(self.logs.locator_found_message(locator))
            return True
        except (NoSuchElementException, TimeoutException):
            self.logs.error(self.logs.locator_not_found(locator))
            raise

    def find_and_click_element(self, locator):
        self.logs.info(self.logs.locator_check_message(locator))
        try:
            element = WebDriverWait(self.driver, tc.wait_time).until(ec.element_to_be_clickable(locator))
            self.logs.info(self.logs.clicking_locator(locator))
            element.click()
            return True
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
            self.logs.error(self.logs.locator_not_found(locator))
            self.logs.error(self.logs.error(e))
            raise

    def scroll_to_element(self, locator):
        try:
            element = WebDriverWait(self.driver, tc.wait_time).until(ec.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            return True
        except (NoSuchElementException, TimeoutException):
            self.logs.error(self.logs.locator_not_found(locator))
            raise

    def hover_element(self, locator):
        try:
            element = WebDriverWait(self.driver, tc.wait_time).until(ec.presence_of_element_located(locator))
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            return True
        except (NoSuchElementException, TimeoutException):
            self.logs.error(self.logs.locator_not_found(locator))
            raise

    def set_text(self, locator, text):
        try:
            element = WebDriverWait(self.driver, tc.wait_time).until(ec.presence_of_element_located(locator))
            self.logs.info(self.logs.sending_text_to_element(text, locator))
            element.send_keys(text)
            return True
        except (NoSuchElementException, TimeoutException):
            self.logs.error(self.logs.locator_not_found(locator))
            raise

    def get_text(self, locator):
        self.logs.info(self.logs.getting_text_from_element(locator))
        try:
            element = WebDriverWait(self.driver, tc.wait_time).until(ec.presence_of_element_located(locator))
            self.logs.info(self.logs.text_of_locator(locator, element))
            return element.text
        except (NoSuchElementException, TimeoutException):
            self.logs.error(self.logs.locator_not_found(locator))
            raise

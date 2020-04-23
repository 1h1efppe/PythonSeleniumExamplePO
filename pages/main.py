from pages.base import BasePage as base
from locators.test_locators import TestLocators as test_locators


class MainPage(base):
    def set_search_field_value(self, text):
        base(self.driver).set_text(test_locators.search_field, text)

    def search(self):
        base(self.driver).find_and_click_element(test_locators.search_button)

    def get_first_item_text(self):
        return base(self.driver).get_text(test_locators.first_element)

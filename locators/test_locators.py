from selenium.webdriver.common.by import By


class TestLocators:
    search_field = (By.NAME, "q")
    search_button = (By.NAME, "btnK")
    first_element = (By.CSS_SELECTOR, ".r > a > h3")

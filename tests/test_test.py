import allure

from data.testdata import TestConst as tc
from pages.main import MainPage as main


@allure.testcase('Sample test with title check')
def test_test(driver):
    driver.get(tc.url)
    main(driver).set_search_field_value("Python")
    main(driver).search()
    assert "Python" in driver.title


@allure.testcase('Sample test with search results check')
def test_two(driver):
    driver.get(tc.url)
    main(driver).set_search_field_value("Python")
    main(driver).search()
    assert "Python" in main(driver).get_first_item_text()

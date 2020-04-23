import logging
import os
import pytest

from py._xmlgen import html
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(3, html.th('Timestamp', class_='sortable time', col='time'))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(3, html.td(datetime.now(), class_='col-time'))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.timestamp = str(item.function.__doc__)


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Set desirable browser')
    parser.addoption('--headless', action='store', default='0', help='Set desirable browser')


def pytest_configure(config):
    os.environ["browser"] = config.getoption('browser')
    os.environ["headless"] = config.getoption('headless')


@pytest.fixture(scope='function')
def driver():
    driver = None
    logging.info('Preparing')
    logging.info('Starting driver and setting capabilities...')
    if os.getenv('browser').lower() == 'chrome':
        if os.getenv('headless').lower() == '1':
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome("chromedriver",   options=chrome_options)
            logging.info('Headless chrome driver is ready')
        else:
            driver = webdriver.Chrome("chromedriver")
    elif os.getenv('browser').lower() == 'firefox':
        driver = webdriver.Firefox()

    if driver:
        logging.info('Driver is ready')
    else:
        logging.error('WebDriver exception')
        raise WebDriverException

    logging.info('Quiting browser')
    yield driver
    driver.quit()



import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.toast import Toast
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    """
    to initialize and quit the WebDriver
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://singular-bubblegum-3bdeb9.netlify.app/")
    yield driver
    driver.quit()

@pytest.fixture()
def test_data():
    """
    to load test data from a YAML file
    :return:
    """
    with open('../data/test_data.yaml', 'r') as file:
        return yaml.safe_load(file)

def test_toast_messages(driver, test_data):
    """
    to validate the toast messages for different types
    :param driver:
    :param test_data:
    :return:
    """
    toast_page = Toast(driver)
    for case in test_data['toast_cases']:
        message_type = case['type']
        expected_message = case['expected_message']
        actual_message = toast_page.get_toast_message(message_type)
        assert actual_message == expected_message, f"Expected: {expected_message}, Got: {actual_message}"

def test_negative_toast_messages(driver):
    """
    to validate the behavior for invalid toast message types
    :param driver:
    :return:
    """
    toast_page = Toast(driver)
    invalid_types = ['invalid_success', 'invalid_error']
    for invalid_type in invalid_types:
        with pytest.raises(Exception):
            toast_page.get_toast_message(invalid_type)

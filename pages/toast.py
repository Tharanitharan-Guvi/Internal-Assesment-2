import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Toast:
    def __init__(self, driver):
        self.driver = driver
        with open('data/locators.yaml', 'r') as file:
            self.locators = yaml.safe_load(file)['toast_messages']

    def wait_for_element(self, by, value, timeout=10):
        """
        This method is used to wait for the element to load on the DOM page
        :param by:
        :param value:
        :param timeout:
        :return:
        """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def get_toast_message(self, message_type):
        """
        This is used to get the toast message
        :param message_type:
        :return:
        """
        locator = self.locators[message_type]
        return self.wait_for_element(By.XPATH, locator).text

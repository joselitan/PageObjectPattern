import unittest
from selenium import webdriver

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # Navigate to the application homepage
        self.driver.get('http://demo-store.seleniumacademy.com/')

    def test_enter_text(self):
        input_text = "//input[@name='q']"
        self.search_field = self.driver.find_element_by_xpath(input_text)
        # self.search_field.click()
        self.search_field.clear()
        self.search_field.send_keys('earphones')
        self.search_field.submit()

    def tearDown(self):
        # close the browser window
        self.driver.quit()

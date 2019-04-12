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

    def tearDown(self):
        # close the browser window
        self.driver.quit()

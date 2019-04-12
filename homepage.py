from base import Basepage
from base import InvalidPageException

class HomePage(Basepage):

    _home_page_slideshow_locator = "//div[@class='slideshow-container']"

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            driver.find_element_by_xpath(self._home_page_slideshow_locator)
        except:
            raise InvalidPageException("Home Page not loaded")

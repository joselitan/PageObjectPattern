from base import Basepage
from base import InvalidPageException

class ProductPage(Basepage):
    _product_view_locator           = "//div[@class='product-view']"
    _product_name_locator           = "//div[@class='product-name']/span"
    _product_description_locator    = "//div[@class='tab-content']/div[@class='std']"
    _product_stock_status_locator   = "//p[@class='availability in-stock']/span[@class='value']"
    _product_price_locator          = "//span/span[@class='price']"

    def __init__(self, driver):
        super(ProductPage, self).__init__(driver)

    @property
    def name(self):
        return self.driver.find_element_by_xpath(self._product_name_locator).text.strip()

    @property
    def description(self):
        return self.driver.find_element_by_xpath(self._product_description_locator).text.strip()

    @property
    def stock_status(self):
        return self.driver.find_element_by_xpath(self._product_stock_status_locator).text.strip()

    @property
    def price(self):
        return self.driver.find_element_by_xpath(self._product_price_locator).text.strip()

    def _validate_page(self, driver):
        try:
            driver.find_element_by_xpath(self._product_view_locator)
        except:
            raise InvalidPageException('Product page not loaded')

from base import Basepage
from base import InvalidPageException
from product import ProductPage

class SearchRegion(Basepage):
    _search_box_locator = 'q'

    def __init__(self, driver):
        super(SearchRegion, self).__init__(driver)

    def searchFor(self, term):
        self.search_field = self.driver.find_element_by_name(self._search_box_locator)
        # self.search_field.click()
        self.search_field.clear()
        self.search_field.send_keys(term)
        self.search_field.submit()
        return SearchResults(self.driver)

class SearchResults(Basepage):
    _product_list_locator           = "//ul[@class='products-grid products-grid--max-3-col first last odd']/li"
    _product_name_locator           = "//h2[@class='product-name']/a"
    _product_image_link             = "//a[@class='product-image']"
    _page_title_locator             = "//div[@class='page-title']"

    _products_count = 0
    _products = {}

    def __init__(self, driver):
        super(SearchResults, self).__init__(driver)
        results = self.driver.find_elements_by_xpath(self._product_list_locator)
        for product in results:
            name = product.find_element_by_xpath(self._product_name_locator).text
            self._products[name] = product.find_element_by_xpath(self._product_image_link)

    def _validate_page(self, driver):
        if 'Search results for' not in driver.title:
            raise InvalidPageException('Search result not loaded')

    @property
    def product_count(self):
        return len(self._products)

    def get_products(self):
        return self._products

    def open_product_page(self, product_name):
        self._products[product_name].click()
        return ProductPage(self.driver)


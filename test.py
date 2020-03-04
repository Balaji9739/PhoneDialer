import unittest
import sys
from selenium import webdriver
sys.path.append('C:\\Users\\Admin\\Desktop\\Project')
from Pages.pages import MainPage, SearchPage
import Basetest


class AmazonTest(unittest.TestCase):

    def setUp(self):
        # create a new Chrome session
        Basetest.Setup()
        self.driver = webdriver.Chrome('C:\\Users\\Admin\\Desktop\\chromedriver.exe')
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("https://www.amazon.com")

    def test_search_by_text(self):
        # Time to wait amazon.com open
        amazon_main_page = MainPage(self.driver)
        assert amazon_main_page.verify_amazon_site(), "Verifies that the  text 'amazon' appears in page title"
        amazon_main_page.input_headphones("Headphones")

        amazon_search_page = SearchPage(self.driver)
        assert amazon_search_page.verify_headphones_text(), "Verified headphones text"
        assert amazon_search_page.select_bestseller_headphones(), "Get bestsellers headphone"


    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
from Locators.locators import MainPageLocators, SearchResultsPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. amazon.com"""

    def verify_amazon_site(self):
        """Verifies that the hardcoded text "amazon" appears in page title"""
        return self.driver.find_element(*MainPageLocators.AMAZON_LOGO)

    def input_headphones(self, *parms):
        '''Go and find input and write head phone'''
        headphones_text = self.driver.find_element(*MainPageLocators.AMAZON_TEXTBOX)
        if headphones_text:
            headphones_text.clear()
            headphones_text.send_keys(parms[0], Keys.ENTER)


class SearchPage(BasePage):
    """Search page action methods come here. I.e. amazon.com"""

    def verify_headphones_text(self):
        """Verifies that the hardcoded text "amazon" appears in page title"""
        return self.driver.find_element(*SearchResultsPageLocators.VERIFY_HEADPHONES_TEXT)

    def select_bestseller_headphones(self):
        '''Go and finds Best sellers'''
        href_list = []
        element = self.driver.find_elements(*SearchResultsPageLocators.HEAPHONES_BESTSELLOR)
        for i in element:
            href_list.append(i.get_attribute("href"))
        for i in href_list:
            self.driver.get(i)
            self.driver.find_element(*SearchResultsPageLocators.ADD_TO_CART_BUTTON).click()
            element_present = self.driver.find_element(*SearchResultsPageLocators.ADDED_TO_CART)
        return element_present
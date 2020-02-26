from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    AMAZON_LOGO = (By.XPATH, "//a[@aria-label='Amazon']")
    AMAZON_TEXTBOX = (By.XPATH, "//input[@id='twotabsearchtextbox']")


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    VERIFY_HEADPHONES_TEXT = (By.XPATH, "//div[@class='a-section a-spacing-small a-spacing-top-small']")
    HEAPHONES_BESTSELLOR = (
    By.XPATH, "//span[text()='Best Seller']/ancestor::div[@data-asin]//span[@data-component-type='s-product-image']//a")
    ADD_TO_CART_BUTTON = (By.XPATH, "//input[@id='add-to-cart-button']")
    ADDED_TO_CART = (By.XPATH, "//h1[normalize-space(.)='Added to Cart']")

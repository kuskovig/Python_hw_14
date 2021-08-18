from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    """
    block with locators
    """
    MAIN_PAGE_CART_BUTTON = (By.CSS_SELECTOR, "#cart button")
    MAIN_PAGE_HEADER_CART_LINK = (By.CSS_SELECTOR, "#top-links li:nth-child(4)")
    MAIN_PAGE_CURRENCY_SELECTOR = (By.CSS_SELECTOR, "#form-currency")
    MAIN_PAGE_SLIDESHOW = (By.CSS_SELECTOR, "#slideshow0.swiper-container")
    RECOMMENDED_ITEMS_WISHLIST_BUTTONS = (By.CSS_SELECTOR, ".product-layout button:nth-child(2)")
    WISHLIST_ATTEMPT_ALERT = (By.CSS_SELECTOR, ".alert")
    WISHLIST_ATTEMPT_ALERT_CLOSE = (By.CSS_SELECTOR, ".alert button")
    SEARCH_BAR_SEARCH_BUTTON = (By.CSS_SELECTOR, "span.input-group-btn button")




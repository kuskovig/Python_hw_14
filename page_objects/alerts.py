from .base_page import BasePage
from selenium.webdriver.common.by import By


class Alerts(BasePage):
    WISHLIST_ALERT = (By.CSS_SELECTOR, ".alert")
    WISHLIST_ALERT_CLOSE = (By.CSS_SELECTOR, ".alert button")

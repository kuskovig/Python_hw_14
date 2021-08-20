from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    CURRENCY_PICKER = (By.CSS_SELECTOR, ".pull-left div>button")
    CURRENCY_CHOICE = '.pull-left li>button'
    CURRENCY_SYMBOL = (By.CSS_SELECTOR, ".pull-left strong")

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self, relative_url=""):
        self.browser.get(self.url + relative_url)

    def is_element_present(self, _by, _locator):
        try:
            self.browser.find_element(_by, _locator)
        except NoSuchElementException:
            return False
        return True

    def wait_for_element(self, _by, _selector, timeout=2):
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((_by, _selector)))
        except TimeoutException:
            raise AssertionError(f"Couldn't find element for {timeout} seconds")
        return element

    def wait_for_element_and_click(self, _by, _selector, timeout=2):
        element = self.wait_for_element(_by, _selector, timeout)
        ActionChains(self.browser).pause(0.1).move_to_element(element).click().perform()

    def wait_for_element_to_disappear(self, _by, _selector, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located((_by, _selector)))
        except TimeoutException:
            raise AssertionError(f"Element didn't disappear in {timeout} seconds")

    def change_currency(self, currency):
        """
        possible currency values = EUR, USD, GBP
        """
        self.browser.find_element(*self.CURRENCY_PICKER).click()
        self.browser.find_element(By.CSS_SELECTOR, self.CURRENCY_CHOICE + f"[name='{currency}']").click()

    def currency_symbol_should_change_with_currency(self, currency, symbol):
        """
        changes currency to the user choice and checks if currency symbols changed
        """
        self.change_currency(currency)
        assert self.wait_for_element(*self.CURRENCY_SYMBOL).text == symbol, "Currency symbol haven't changed"

from page_objects.main_page import MainPage

import pytest


def test_logo(browser, url):
    page = MainPage(browser, url)
    page.open()
    page.wait_for_element(*MainPage.MAIN_PAGE_SLIDESHOW)


@pytest.mark.parametrize("currency, symbol", [("EUR", "€"),
                                              ("USD", "$"),
                                              ("GBP", "£")])
def test_currency_changes(browser, url, currency, symbol):
    page = MainPage(browser, url)
    page.open()
    page.currency_symbol_should_change_with_currency(currency, symbol)


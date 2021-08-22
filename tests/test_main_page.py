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


def test_alert_correctly_closes(browser, url):
    page = MainPage(browser, url)
    page.open()
    page.wish_random_recommended_item()
    page.close_wishlist_alert()
    page.closed_alert_should_disappear()


def test_there_is_cart_button(browser, url):
    page = MainPage(browser, url)
    page.open()
    page.should_be_cart_button()


def test_there_is_search_button(browser, url):
    page = MainPage(browser, url)
    page.open()
    page.should_be_search_button()

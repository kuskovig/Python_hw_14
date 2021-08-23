from page_objects.catalog_page import CatalogPage


def test_there_is_compare_link(browser, url):
    page = CatalogPage(browser, url)
    page.open(CatalogPage.LAPTOPS_CATALOG_RELATIVE_URL)
    page.there_is_compare_hyperlink()


def test_can_add_product_to_compare(browser, url):
    page = CatalogPage(browser, url)
    page.open(CatalogPage.LAPTOPS_CATALOG_RELATIVE_URL)
    page.add_single_random_product_to_compare()


def test_can_open_product_page(browser, url):
    page = CatalogPage(browser, url)
    page.open(CatalogPage.LAPTOPS_CATALOG_RELATIVE_URL)
    page.open_random_product_on_page()

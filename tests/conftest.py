import socket
import pytest
from selenium import webdriver


def get_local_opencart_address():
    return "http://"+socket.gethostbyname(socket.gethostname())+":8081"


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     choices=["chrome", "firefox", "opera", "edge"],
                     default="chrome")
    parser.addoption("--url",
                     action="store",
                     default=get_local_opencart_address())


@pytest.fixture
def browser(request):
    def teardown():
        driver.quit()

    driver = None
    choice = request.config.getoption("--browser")
    if choice == "chrome":
        driver = webdriver.Chrome()
    elif choice == "firefox":
        driver = webdriver.Firefox()
    elif choice == "opera":
        driver = webdriver.Opera()
    elif choice == "edge":
        driver = webdriver.Edge()

    request.addfinalizer(teardown)
    driver.set_window_size(1960, 1080)
    return driver


@pytest.fixture
def url(request):
    return request.config.getoption("--url")

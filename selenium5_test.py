import time
from selenium import webdriver
from selenium3 import make_screenshot
from selenium4_klasa import LoginPage
import pytest

test_data = [
    ('standard_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/'),
    ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html')
    ]


@pytest.mark.parametrize('uzytkownik, password, url', test_data)
def test_login_page(uzytkownik, password, url):
    ddriver = webdriver.Firefox()
    page = LoginPage(ddriver, 'user-name', 'password', 'login-button')
    page.open()
    page.enter_username(uzytkownik)
    page.enter_password(password)
    page.click_login_button()
    time.sleep(1)
    try:
        assert ddriver.current_url == url, make_screenshot(ddriver)
    finally:
        ddriver.quit()

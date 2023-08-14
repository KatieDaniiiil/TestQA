import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('film', ["Один дома", "Крестный отец"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, film):
        link = "https://yohoho.cc/"
        browser.get(link)
        input1 = browser.find_element(By.XPATH, '//*[@id="search-title"]')
        input1.send_keys(f'{film}')
        time.sleep(5)
        # этот тест запустится 2 раза

    def test_guest_should_see_navbar_element(self, browser, film):
        print('\n Тест 2')
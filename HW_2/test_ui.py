import time

import pytest
from selenium import webdriver


class TestUI:
    LOGIN = "Admin"
    LOGIN_FIELD = ("xpath", '//input[@name="username"]')
    PASSWORD = "admin123"
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    LOGIN_BUTTON = ("xpath", "//button[@type='submit']")

    def setup_method(self):
        self.driver = webdriver.Chrome()

    def test_open_yandex_main_page(self):
        self.driver.get("URL")
        assert self.driver.

    @pytest.mark.login
    def test_login(self):
        self.driver.get(url=self.URL)
        time.sleep(2)
        self.driver.find_element(*self.LOGIN_FIELD).send_keys(self.LOGIN)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(self.PASSWORD)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        assert (
            self.driver.current_url
            == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        )

    def teardown_method(self):
        self.driver.quit()

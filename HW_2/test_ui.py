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
    LINK_TO_REG_FORM = ("xpath", "//a[text()='Регистрация']")

    def setup_method(self):
        self.driver = webdriver.Chrome()

    @pytest.mark.element
    def test_element_on_page(self):
        self.driver.get(self.URL)
        time.sleep(2)
        assert self.driver.find_element(*self.LOGIN_BUTTON), "LOGIN_BUTTON NOT FOUND"

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

    @pytest.mark.navigation
    def test_page_navigation(self):
        self.driver.get("https://mail.ru/")
        time.sleep(2)
        self.driver.find_element(*self.LINK_TO_REG_FORM).click()
        time.sleep(2)

        assert (
            "https://account.mail.ru/signup?app_id_mytracker" in self.driver.current_url
        )

    def teardown_method(self):
        self.driver.quit()

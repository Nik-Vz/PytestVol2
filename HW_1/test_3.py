from selenium import webdriver


class TestTitleStepik:
    def test_title_open_stepik(self):
        driver = webdriver.Chrome()
        driver.get("https://stepik.org/")
        title = driver.title
        assert title == "Каталог онлайн-курсов – Stepik"

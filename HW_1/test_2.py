from selenium import webdriver


class TestTitleVk:
    def test_title_open_vk(self):
        driver = webdriver.Chrome()
        driver.get("https://vk.com/")
        title = driver.title
        assert title == "ВКонтакте | Добро пожаловать"

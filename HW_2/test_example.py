from selenium import webdriver


class TestExample:
    def setup_method(self):
        self.driver = webdriver.Chrome()

    def test_open_yandex_main_page(self):
        self.driver.get("https://ya.ru")
        assert self.driver.title == "Яндекс — быстрый поиск в интернете"

    def test_open_mail_main_page(self):
        self.driver.get("https://mail.ru")
        assert (
            self.driver.title
            == "Mail.ru: почта, поиск, новости, прогноз погоды, гороскоп, программа передач"
        )

    def test_open_rambler_main_page(self):
        self.driver.get("https://rambler.ru")
        assert (
            self.driver.title
            == "Рамблер/новости, почта и поиск — медийный портал: новости России и мира, электронная почта, погода, развлекательные и коммуникационные сервисы. Новости сегодня и сейчас"
        )

    def test_open_vk_main_page(self):
        self.driver.get("https://vk.com")
        assert self.driver.title == "ВКонтакте | Добро пожаловать"

    def teardown_method(self):
        self.driver.quit()

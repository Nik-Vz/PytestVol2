from selenium import webdriver


class TestTitleMail:
    def test_title_open_mail(self):
        driver = webdriver.Chrome()
        driver.get("https://mail.ru/")
        title = driver.title
        assert (
            title
            == "Mail.ru: почта, поиск, новости, прогноз погоды, гороскоп, программа передач"
        )

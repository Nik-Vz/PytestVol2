import requests
import pytest


# response = requests.get(
#     url="https://jsonplaceholder.typicode.com/",
# )
# print(response.text)


class TestAPI:
    def setup_method(self):
        self.response = requests.get(
            url="https://jsonplaceholder.typicode.com/",
        )

    def test_status_code(self):
        assert self.response.status_code == 200

    def test_content(self):
        assert 'href="https://github.com/typicode/json-server"' in self.response.text

    def test_wrong_request(self):
        assert (
            requests.get("https://jsonplaceholder.typicode.com/123").status_code != 200
        )

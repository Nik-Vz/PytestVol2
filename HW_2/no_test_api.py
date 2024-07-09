import requests


response = requests.get(
    url="https://vk.com",
)
print(response.text)

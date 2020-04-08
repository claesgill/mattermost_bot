
import requests
from datetime import datetime
from time import sleep


class Bot:
    def __init__(self, name, url):
        self.name = name
        self.url  = url

    def send_message(self, message):
        payload = {
            "text": message,
            "username": self.name
        }
        response = requests.post(self.url, json=payload)
        if response.status_code == 200:
            print(f"Message sendt with status code: {response.status_code}")
        else:
            print(f"Error sending message. Status code: {response.status_code}")


if __name__ == "__main__":
    bot_test_url = "https://chat.sits.no/hooks/9dnji19thjfcbpth461gxxnwhr"
    message = "@here Tid for standup! :point_right: https://chat.sits.no/skatt-it/channels/team-datapreparering"
    bot = Bot("BotName", bot_test_url)
    bot.send_message(message)

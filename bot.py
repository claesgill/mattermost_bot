
import requests
from datetime import datetime
from time import sleep


class Bot:
    """Simple mattermost bot

    Args:
        name (str): Name of the bot
        url (str): The url-hook provided by mattermost
    """
    __test_url = "https://chat.sits.no/hooks/9dnji19thjfcbpth461gxxnwhr"

    def __init__(self, name, url):
        self.name = name
        self.url  = url.strip(" ")

    def send_message(self, message):
        """The bot sends a message to the channel provided in the url

        Args:
            message (str): The message that the bot will post to the channel
        """
        payload = {
            "text": self.__check_url() + message,
            "username": self.name
        }
        try:
            response = requests.post(self.url, json=payload)
            if response.status_code == 200:
                print(f"Message sendt with status code: {response.status_code}")
            else:
                print(f"Error sending message. Status code: {response.status_code}")
        except:
            print(
            "\033[31m" +
            "Was not able to send message\nCheck if bot-information is correct:\n" +
            f"Bot name: '{self.name}'\n" +
            f"URL:      '{self.url}'\n"  +
            f"Message:  '{message}'\n" +
            "\033[0m")

    def __check_url(self):
        if self.url == self.__test_url:
            import os
            postfix = "Post by: {}\n".format(os.environ.get("USER"))
            return postfix
        else:
            return ""

if __name__ == "__main__":
    bot_test_url = "https://chat.sits.no/hooks/9dnji19thjfcbpth461gxxnwhr"
    message = "@here Tid for standup!"
    bot = Bot("BotName", bot_test_url)
    bot.send_message(message)

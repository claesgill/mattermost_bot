from bot import Bot
from pathlib import Path
import os

name    = input("Enter bot name: (MyBot)\n")
message = input("Enter message: (Hello Mattermost)\n")
url     = input("Enter url: (https://chat.sits.no/hooks/1234)\n")
cron    = input("Enter cron time: (* * * * *)\n")

output_file_name = "generated_bots/{}.py".format(name.replace(" ", "_"))
output_file = f"""
import sys; sys.path.append('.')
from bot import Bot

bot = Bot(name='{name}', url='{url}')
bot.send_message(message='{message}')
"""

try:
    with open(output_file_name, "w") as f:
        f.write(output_file)
    print(f"\n\033[32mSuccess generating file: {output_file_name}\033[0m\n")
except:
    print(f"\n\033[91mThere was an error generating: {output_file_name}\033[0m\n")

print("Copy the \033[32mfollowing\033[0m and paste into crontab:\n")
print(f"\033[32m{cron} python3 {Path().resolve()}/{output_file_name}\n\033[0m")

answer = input("Go to crontab: [y/N] ")
if answer == "y" or answer == "Y": 
    os.system("sudo crontab -e")
else: 
    print("Not adding bot to crontab.\n" +
          "You can edit your crontab with: 'sudo crontab -e'")
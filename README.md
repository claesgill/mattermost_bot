# Simple mattermost bot
Used to create a scrum-bot to alert us when it's time for standup. A cron job is used to run `scrum_bot.py`.

## Usage
### Create bot
#### Automatically
Run `make create-bot` and follow the instructions.  

You will need to provide the following:  
**Bot name**: Name of your bot (will be displayed when bot post messages)  
**Message**: Message that your bot will post (can contain @channel, @here etc)  
**URL**: The URL-hook from mattermost. To generate go to MM click the hamburger menu --> Integrations --> Incoming Webhooks --> Add incoming Webhook (copy the URL after the hook is created)  
**Cron time**: A valid cron time on the form: * * * * * [minute hour day(month) month day(week)]. You can use [CronGuru](https://crontab.guru/#*_*_*_*_*) for more help.  

#### Manually
If you need a more advanced bot with your own logic you can create a new python-file where you import the `Bot`-class. The following code is the minimum you have to do:  
```python3
from bot import Bot

bot = Bot(name='Scrum Master', 
          url='https://chat.sits.no/hooks/ ...')
bot.send_message(message='@here Hello MatterMost!')
```

### Testing a bot
You can list your created bots with (*only lists bots inside `generated_bots/`*):  
```shell
$ make list-bots
Mybot.py
Anotherbot.py
...
```

Further, you can choose to test a bot:  
```bash
$ make test-bot bot=Mybot
Message sendt with status code: 200
Test completed
```
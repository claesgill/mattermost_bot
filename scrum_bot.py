
from bot import Bot


message = "@here Tid for standup! :point_right: https://chat.sits.no/skatt-it/channels/team-datapreparering"
bot = Bot("StandUp", "https://chat.sits.no/hooks/cn5yuk9m7igs5bpa93yqzphh9w")
bot.send_message(message)

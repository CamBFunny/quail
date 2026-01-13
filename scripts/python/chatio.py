import os
from twitchio.ext import commands

# Load credentials securely from environment variables or a config file
# Ensure you set these environment variables in your system/script
TMI_TOKEN = os.environ.get('TMI_TOKEN', 'oauth:YOUR_OAUTH_TOKEN')
CLIENT_ID = os.environ.get('CLIENT_ID', 'YOUR_CLIENT_ID')
BOT_NICK = os.environ.get('BOT_NICK', 'your_twitch_username') # The bot's username
CHANNEL = os.environ.get('CHANNEL', 'the_channel_to_join') # The channel you want to read

class Bot(commands.Bot):

    def __init__(self):
        # Initialise the bot with the necessary access token, client ID, and the channel to connect to
        super().__init__(token=TMI_TOKEN, client_id=CLIENT_ID, nick=BOT_NICK,
                         initial_channels=[CHANNEL])

    async def event_ready(self):
        # This event fires when the bot has connected successfully
        print(f'Logged in as | {self.nick}')
        print(f'Monitoring channel | #{CHANNEL}')

    async def event_message(self, message):
        # This event fires for every single chat message
        # Messages from the bot itself are ignored to prevent loops
        if message.author.name.lower() == self.nick.lower():
            return

        print(f'{message.author.name}: {message.content}')

if __name__ == "__main__":
    bot = Bot()
    bot.run()

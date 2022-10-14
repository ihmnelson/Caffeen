import traceback

import discord
from discord.ext import commands
import logging
import os

with open("aux_files/token.txt", 'r') as f:
    token = f.read()

intents = discord.Intents.default()
intents.message_content = True
handler = logging.FileHandler(filename='aux_files/discord.log', encoding='utf-8', mode='w')


class EmbeddedHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page, color=discord.Color.purple())
            await destination.send(embed=emby)


client = commands.Bot(command_prefix=commands.when_mentioned_or('*'), intents=intents, help_command=EmbeddedHelp())

extensions = [
    'cogs.main_features',
    'cogs.template_cog'
]


@client.event
async def on_ready():
    print(f'Logged in as {client.user}, ID: {client.user.id}')
    await load_extensions()


async def load_extensions():
    for extension in extensions:
        try:
            print(f'Loading {extension}')
            await client.load_extension(f'{extension}')
        except Exception as e:
            traceback.print_tb(e.__traceback__)


client.run(token, log_handler=handler, log_level=logging.DEBUG)

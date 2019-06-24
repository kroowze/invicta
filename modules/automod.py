import discord
from discord.ext import commands
from os import system
from os import popen


class AutoMod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        # todo: embeds
        server = message.guild
        author = message.author
        flag = str(popen("Java -jar TextScript.jar -t " + message.content).read())
        if flag.startswith("1"):
            for channel in server.channels:
                if channel.name == "automod":
                    await channel.send("Message sent by <@" + str(author.id) + "> deleted.\nContent: " + str(message.content))
            await message.delete()


def setup(client):
    client.add_cog(AutoMod(client))
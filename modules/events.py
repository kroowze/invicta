import discord
from discord.ext import commands
from os import system
from os import popen


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        server = message.guild
        author = message.author
        for channel in server.channels:
            if channel.name == "logs":
                if message.content[:2] == "i!":
                    break
                else:
                    await channel.send("Message sent by <@" + str(author.id) + "> deleted in <#" + str(message.channel.id) + ">.\nContent: " + str(message.content))

    @commands.Cog.listener()
    async def on_bulk_message_delete(self, messages):
        count = 0
        id = 0
        for message in messages:
            id = message.channel.id
            count += 1
            if count == 1:
                break
        channelmeme = self.client.get_channel(id)
        channel = self.client.get_channel(id)
        server = channel.guild
        count = 0
        for nbmessages in messages:
            count += 1
        for channel in server.channels:
            if channel.name == "logs":
               await channel.send(str(count) + " messages deleted in <#" + str(channelmeme.id) + ">.")


def setup(client):
    client.add_cog(Events(client))
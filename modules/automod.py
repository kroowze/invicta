import discord
from discord.ext import commands
from os import system
from os import popen
import asyncio


class AutoMod(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_message(self, message):
        # todo: embeds
        server = message.guild
        author = message.author
        content = message.content
        content = content.replace("|", "i")
        content = content.replace(":", "")
        content = content.replace("<a", "")
        content = content.replace("<", "")
        content = content.replace(">", "")
        if not message.author.bot:
            flag = str(popen("Java -jar JHandler.jar -t " + content).read())
            if flag.startswith("1"):
                for channel in server.channels:
                    if channel.name == "automod":
                        await channel.send("Message sent by <@" + str(author.id) + "> deleted.\nContent: " + str(content))
                await message.delete()

    @commands.Cog.listener()
    async def on_message_edit(self, s, message):
        # todo: embeds
        author = message.author
        server = message.guild
        flag = str(popen("Java -jar JHandler.jar -t " + message.content).read())
        if flag.startswith("1"):
            for channel in server.channels:
                if channel.name == "automod":
                    await channel.send(
                        "Message edited by <@" + str(author.id) + "> deleted.\nContent: " + str(s.content) + " --> " + str(message.content))
            await message.delete()

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        b = before.display_name
        a = after.display_name
        server = after.guild
        if a is not b:
            flag = str(popen("Java -jar JHandler.jar -t " + a).read())
            if flag.startswith("1"):
                for channel in server.channels:
                    if channel.name == "automod":
                        await channel.send("User " + "<@" + str(before.id)+"> : " + b + " to " + a)





def setup(client):
    client.add_cog(AutoMod(client))

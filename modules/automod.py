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
        flag = str(popen("Java -jar JHandler.jar -t " + message.content).read())
        if flag.startswith("1"):
            for channel in server.channels:
                if channel.name == "automod":
                    await channel.send("Message sent by <@" + str(author.id) + "> deleted.\nContent: " + str(message.content))
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
        # todo: embeds
        b = before.display_name
        a = after.display_name
        server = after.guild
        memb = server.get_member(after.id)
        if a is not b:
            flag = str(popen("Java -jar JHandler.jar -t " + a).read())
            if flag.startswith("1"):
                for channel in server.channels:
                    if channel.name == "automod":
                        await memb.edit(nick="i!i")
                        await channel.send("User " + "<@" + str(before.id)+"> : " + b + " to " + a)



def setup(client):
    client.add_cog(AutoMod(client))
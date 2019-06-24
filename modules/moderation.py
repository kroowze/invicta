import discord
from discord.ext import commands
from time import sleep
import os
import asyncio
import datetime
from tinydb import TinyDB
from tinydb import Query


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, id, *reason):
        message = ctx.message
        await message.delete()
        channel = ctx.message.channel
        author = ctx.message.author
        server = ctx.message.guild
        if id[0] == "<":
                id = id.replace("<", "")
                id = id.replace(">", "")
                id = id.replace("@", "")
        user = self.client.get_user(int(id))
        await server.ban(user)
        await channel.send("**Successfully banned "+user.name+"#"+user.discriminator+"!**")
        for channel in server.channels:
            if channel.name == "moderation":
                await channel.send(user.name + "#" + user.discriminator + " was banned by <@" + author.id + "> for the reason: " + str(reason))

    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, id, *reason):
        message = ctx.message
        await message.delete()
        channel = ctx.message.channel
        author = ctx.message.author
        server = ctx.message.guild
        if id[0] == "<":
                id = id.replace("<", "")
                id = id.replace(">", "")
                id = id.replace("@", "")
        user = self.client.get_user(int(id))
        await server.kick(user)
        await channel.send("**Successfully kicked "+user.name+"#"+user.discriminator+"!**")
        for channel in server.channels:
            if channel.name == "moderation":
                await channel.send(user.name + "#" + user.discriminator + " was kicked by <@" + author.id + "> for the reason: " + str(reason))

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, *options):
        message = ctx.message
        messages = []
        channel = ctx.message.channel
        author = ctx.message.author
        server = ctx.message.guild
        optioncount = 0
        for x in options:
            optioncount += 1
        if options[0] == "bots":
            async for message in channel.history(limit=31):
                if message.author.bot == True:
                    messages.append(message)
        elif options[0].startswith("<"):
            id = options[0]
            id = id.replace("<", "")
            id = id.replace(">", "")
            id = id.replace("@", "")
            if optioncount == 1:
                async for message in channel.history(limit=31):
                    if message.author.id == int(id):
                        messages.append(message)
            elif optioncount == 2:
                limit = int(options[0]) + 1
                async for message in channel.history(limit=limit):
                    if message.author.id == int(id):
                        messages.append(message)
        elif options[0][0].isdigit():
            if int(options[0]) > 5000:
                await channel.send("Please enter a number of messages below 5000.")
            else:
                limit = int(options[0]) + 1
                async for message in channel.history(limit=limit):
                    messages.append(message)
        await channel.delete_messages(messages)

    @commands.command(pass_context=True)
    async def report(self, ctx, *report):
        author = ctx.message.author
        message = ctx.message
        channel = ctx.message.channel
        server = ctx.message.guild
        reportmsg = ""
        for word in report:
            word += " "
            reportmsg += word
        await message.delete()
        for channel in server.channels:
            if channel.name == "reports":
                await channel.send(reportmsg + "\n\n sent by: " + "<@" + str(author.id) + ">.")
        await author.send("**Your report has been successfully sent to the moderators of " + server.name + "!**")


def setup(client):
    client.add_cog(Moderation(client))

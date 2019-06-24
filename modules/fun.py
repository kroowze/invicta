import discord
from discord.ext import commands
from os import system
from os import popen


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def vote(self, ctx, *vote):
        channel = ctx.message.channel
        message = ctx.message
        votemsg = ""
        for word in vote:
            word += " "
            votemsg += word
        await message.delete()
        votemessage = await channel.send(votemsg)
        message = await channel.fetch_message(votemessage.id)
        await message.add_reaction("👍")
        await message.add_reaction("👎")



def setup(client):
    client.add_cog(Fun(client))
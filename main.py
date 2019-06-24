import discord
from discord.ext import commands
from time import sleep
import datetime
from os import system

f = open("token.txt")
TOKEN = f.readline().strip()

client = commands.Bot(command_prefix = "i!")

extensions = ["modules.moderation", "modules.automod", "modules.events", "modules.fun"]

bot_owners = [225057590697132032, 384116325699682315]

if TOKEN == "":
    print("No token could be found, please set one in the token.txt file.")


@client.event
async def on_ready():
    print("[INFO] Invicta is up and running ^w^!")
    current_game = "i!help"
    game = discord.Game(current_game)
    await client.change_presence(activity=game)
    print("[INFO] Presence has been set to: " + current_game)
    print("[INFO] Make sure to create the #logs, #moderation, #automod, and the #reports channels.")


@client.command(pass_context=True)
async def load(ctx, extension):
    channel = ctx.message.channel
    for id in bot_owners:
        if ctx.message.author.id == id:
            try:
                client.load_extension(extension)
                print("[INFO] Loaded {}".format(extension))
                await channel.send("Loaded {}".format(extension))
            except Exception as error:
                print("[INFO] {} cannot be loaded. [{}]".format(extension, error))


@client.command(pass_context=True)
async def unload(ctx, extension):
    channel = ctx.message.channel
    for id in bot_owners:
        if ctx.message.author.id == id:
            try:
                client.unload_extension(extension)
                print("[INFO] Unloaded {}".format(extension))
                await channel.send("Unloaded {}".format(extension))
            except Exception as error:
                print("[INFO] {} cannot be unloaded. [{}]".format(extension, error))


@client.command(pass_context=True)
async def reload(ctx, extension):
    channel = ctx.message.channel
    for id in bot_owners:
        if ctx.message.author.id == id:
            try:
                client.unload_extension(extension)
                sleep(0.5)
                client.load_extension(extension)
                print("[INFO] Reloaded {}".format(extension))
                await channel.send("Reloaded {}".format(extension))
            except Exception as error:
                print("[INFO] {} cannot be reloaded. [{}]".format(extension, error))

if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print("[INFO] {} cannot be loaded. [{}]".format(extension, error))

client.run(TOKEN)

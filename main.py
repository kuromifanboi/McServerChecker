import os
import discord
from discord.ext import commands
from mcstatus import JavaServer

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print('Bot info:')
    print('----------------------------------------------------')
    print(f'Bot name: {bot.user.name}')
    print(f'Bot id: {bot.user.id}')
    print(f'Bot version: {discord.__version__}')
    print('Bot is ready')
    print('----------------------------------------------------')

@bot.command()
async def lookup(ctx):
    try:
        server = JavaServer.lookup(ctx.message.content[8:])
        status = server.status()
        await ctx.send(f"{ctx.message.content[8:]} has {status.players.online} players online\nThe server replied in {status.latency} ms")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

bot.run(os.environ['DISCORD_TOKEN'])

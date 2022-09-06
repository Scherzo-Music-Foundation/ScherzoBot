import discord
import os

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
	print("Ready")

TOKEN = os.environ["TOKEN"]
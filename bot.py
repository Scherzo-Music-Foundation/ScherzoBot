from discord import Client, Intents, Status, Activity, ActivityType
import os

client = Client(intents=Intents.default())

@client.event
async def on_ready():
  print("Ready")
  await client.change_presence(status=Status.online,activity=Activity(type=ActivityType.watching, name="over Scherzo!"))

@client.event
async def on_message(ctx):
  if ctx.guild.id == 1016518413209837670 and not ctx.author.bot:
    await ctx.channel.send("hi")
  


TOKEN = os.environ["TOKEN"]
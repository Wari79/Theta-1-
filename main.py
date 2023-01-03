import discord
from discord.ext import commands
from replit import db
import requests
import random
import json
import asyncio
from keep_alive import keep_alive
import os
from discord.utils import find
from discord.ext import tasks
from googletrans import Translator
import traceback
import sys
import pickle
from discord.ext.commands import (
    has_permissions,
    MissingPermissions,
    has_role,
    MissingRole,
    cooldown,
    BucketType,
    NotOwner,
    CommandNotFound,
    MissingRequiredArgument,
)
import time

from emojis import yellow, red, green, inv, loading
from discord import app_commands


# ------------------------FUNCTIONS---------------------
DEFAULT_PREFIX = ">"


def determine_prefix(bot, msg):
    guild = msg.guild
    base = [DEFAULT_PREFIX]

    with open("prefix.json", "r", encoding="utf-8") as fp:
        custom_prefixes = json.load(fp)

    if guild:
        try:
            prefix = custom_prefixes[f"{guild.id}"]
            return prefix
        except KeyError:
            return base
            return prefix

    return base

# ------------------CONFIGS--------------------------------
staff = [798280308071596063, 686649585422434361]
intents = discord.Intents.all()
client = commands.Bot(command_prefix=determine_prefix, owner_ids=set(staff), intents=intents
)
tree = client.tree
client.remove_command("help")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(
            type=discord.ActivityType.playing, name=f"with {len(client.guilds)} servers and {len(client.users)} members"))
  
    ham = client.get_user(798280308071596063)
    embed = discord.Embed(description="**Theta Is Currently Online**", color=red)
    await ham.send(embed=embed)
    await client.load_extension("cogs.(-)staff")
    await client.load_extension("cogs.(-)SYSTEM")
    await client.load_extension("cogs.(D)info")
    await client.load_extension("cogs.(E)shop")
    await client.load_extension("cogs.(F)actions")
    await client.load_extension("cogs.(F)actions2")
    await client.load_extension("cogs.(H)quest")
    await client.load_extension("cogs.(C)income")
    await client.load_extension("cogs.(I)levels")
    await client.load_extension("cogs.logging")
    await client.load_extension("cogs.maintenance")
    
    

  
@client.command(aliases = ["refresh"])
@commands.is_owner()
async def r(ctx):
  first = discord.Embed(description=f"On it {loading}", color=red)
  second = await ctx.reply(embed=first)
  await client.reload_extension("cogs.(-)staff")
  await client.reload_extension("cogs.(-)SYSTEM")
  await client.reload_extension("cogs.(D)info")
  await client.reload_extension("cogs.(E)shop")
  await client.reload_extension("cogs.(F)actions")
  await client.reload_extension("cogs.(F)actions2")
  # await client.reload_extension("cogs.(H)quest")
  
  await client.reload_extension("cogs.(C)income")
  await client.reload_extension("cogs.(I)levels")
  await client.reload_extension("cogs.logging")
  await client.reload_extension("cogs.maintenance")
  await tree.sync()
  await asyncio.sleep(2)
  third = discord.Embed(description="Refreshed **10** cog files", color=green)
  await second.edit(embed=third)



# @client.command()
# @commands.is_owner()
# async def clr(ctx):
#   ctx.client.tree.clear_commands(guild=ctx.guild)
#   await ctx.send("done!")
#   await tree.sync()








  




# ------------------LAST CONFIG SHELL-----------------------


keep_alive()
try:
  client.run(os.getenv("TOKEN"))
except:
    os.system("kill 1")

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

from emojis import yellow, red, green
from discord import app_commands




class moderation(commands.Cog):
    def __init__(self, client): 
        self.client = client

    def cooldown(rate, per_sec=0, per_min=0, per_hour=0, type=commands.BucketType.default):
        return commands.cooldown(rate, per_sec + 60 * per_min + 3600 * per_hour, type)







      
    

    @app_commands.command(description="Slash commands coming soon!") 
    async def slash(self, int: discord.Interaction):
      await int.response.send_message("Full slash commands coming soon!")




async def setup(client):
    await client.add_cog(moderation(client)) 
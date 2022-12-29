import discord
from discord.ext import commands
import os
import pickle
import random
import asyncio
import json
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
from emojis import tank, tank2, sold, res, hearts, dead, comp, arr, wall, strike, ca, scrap, spy, medal, crate, red, green, yellow, inv
data_filename2 = "levels/levels"
data_filename = "currency files/data"

from discord.ui import *

from discord import app_commands

class Data:
      def __init__(self, xp, level, resources, soldiers, tanks, spy, wall, strikes, s, r, scrap, crate, ca, medals, cfc, cfca, mesg):
        self.level = level
        self.resources = resources
        self.soldiers = soldiers
        self.tanks = tanks
        self.spy = spy
        self.wall = wall
        self.strikes = strikes
        self.mesg = mesg
        self.s = s
        self.r = r
        self.crate = crate
        self.medals = medals
        self.scrap = scrap
        self.ca = ca
        self.cfc = cfc
        self.cfca = cfca
        self.xp = xp

class logging(commands.Cog):
    def __init__(self, client): 
        self.client = client




    @commands.command()  
    @commands.is_owner()
    async def logs(self, ctx):

      default_log = discord.utils.get(ctx.guild.text_channels, name="theta-logs")

      if not default_log:
        conf1 = discord.Embed(description="Do you want to create a log channel for theta?", color=inv)
      
        button_one = Button(label = "✅", style = discord.ButtonStyle.green)
        button_two = Button(label = "❌", style = discord.ButtonStyle.red)

        view = View()
        view.add_item(button_one)
        view.add_item(button_two)

        conf3 = await ctx.reply(embed=conf1, view=view) 

        async def button_one_callback_check(interaction):
          if interaction.user == ctx.author:
            
            overwrites = {ctx.guild.default_role:  discord.PermissionOverwrite(read_messages=False,send_messages=False, add_reactions=False,read_message_history=False)} 
            conf2 = discord.Embed(description="Creating channel..", color=yellow)

            await conf3.delete()
            
            
            channel1 = await ctx.guild.create_text_channel(name="theta-logs", overwrites=overwrites) 
            done = discord.Embed(description=f"Created channel {channel1.mention}", color=inv)
            await interaction.response.send_message(embed=done)

            
            

          else:
            error = discord.Embed(description="This button is not for you to press!", color=inv)
            await interaction.response.send_message(embed=error)

            
        
        async def button_two_callback_check(interaction):
          if interaction.user == ctx.author:
            
            
            conf2 = discord.Embed(description="Cancelled the process", color=red)

            await conf3.edit(embed=conf2, view=None)
          else:
            error = discord.Embed(description="This button is not for you to press!", color=red)
            await interaction.response.send_message(embed=error)
        button_one.callback = button_one_callback_check
        button_two.callback = button_two_callback_check
      
      else:
        found = discord.Embed(description=f"Found an existing channel! {default_log.mention}", color=inv)
        await ctx.reply(embed=found) 
 



    

async def setup(client):
    await client.add_cog(logging(client))  




def load_data():
        if os.path.isfile(data_filename):
            with open(data_filename, "rb") as file:
              return pickle.load(file)
        else:
            return dict()


def load_member_data(member_ID):
    data = load_data()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0)

    return data[member_ID]

def save_member_data(member_ID, member_data):
    data = load_data()

    data[member_ID] = member_data

    with open(data_filename, "wb") as file:
      pickle.dump(data, file)

def load_data2():
        if os.path.isfile(data_filename2):
            with open(data_filename2, "rb") as file:
              return pickle.load(file)
        else:
            return dict()


def load_member_data2(member_ID):
    data = load_data2()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0)

    return data[member_ID]

def save_member_data2(member_ID, member_data2):
    data = load_data2()

    data[member_ID] = member_data2

    with open(data_filename2, "wb") as file:
        pickle.dump(data, file)
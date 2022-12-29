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

class levels(commands.Cog):
    def __init__(self, client): 
        self.client = client

    @commands.hybrid_command(name = "xp_giving", description="Give xp to desired member, if not, then author is selected by default")
    @commands.is_owner()
    async def give_xp(self, ctx, amount, member:discord.Member=None):
      if member == None:
        member = ctx.author
      if not amount[0].isnumeric():
        invamount = discord.Embed(title="Invalid Amount", description=f"Sorry, `{amount}` is an invalid integer/number, please include an integer and nothing else.\n`Ex. (1 --> 100)`", color=red)
        await ctx.reply(embed=invamount)
        return
      member_data2 = load_member_data2(member.id)
      member_data2.xp += int(amount)
      done = discord.Embed(description=f"Gave `{amount}` XP to {member.mention}", color=inv)
      await ctx.reply(embed=done)
      save_member_data2(member.id, member_data2)
      

    @commands.command() 
    async def xp(self, ctx):
      member_data2 = load_member_data2(ctx.author.id)
      xp_status = discord.Embed(title="Current Profile", description=f"**Level:** `{member_data2.level}`\n-\n**XP:** `{member_data2.xp}`", color=yellow)
      await ctx.reply(embed=xp_status)

    @commands.command()
    async def res(self, ctx, member:discord.Member=None):
      if member == None:
        member = ctx.author
      member_data2 = load_member_data2(ctx.author.id)
      member_data2.xp = 0
      member_data2.level = 0
      await ctx.send(f"reseted {member.mention}'s base")
      save_member_data2(ctx.author.id, member_data2)
      
            
            
      
      










async def setup(client):
    await client.add_cog(levels(client))  




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
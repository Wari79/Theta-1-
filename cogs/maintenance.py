import discord
from discord.ext import commands
import os
import pickle
import asyncio
import random
from emojis import tank, tank2, sold, res, hearts, dead, comp, arr, wall, strike, ca, scrap, spy, medal, crate, green, red, yellow, inv

class maintenance(commands.Cog):
    def __init__(self, client): 
        self.client = client

    


    @commands.command()
    @commands.is_owner()
    async def activate(self, ctx, maintenance=None):
      default_log = discord.utils.get(self.client.get_all_channels(), id=1057356641911181373)
      if maintenance != "maintenance":
        no = discord.Embed(description="did you mean `activate maintenance` ?", color=inv)
        await ctx.reply(embed=no)
        return
      conf = discord.Embed(description="Executing maintenance protocol..", color=inv)
      conf1 = await ctx.reply(embed=conf)

      
      recruit = self.client.get_command("recruit")
      explore = self.client.get_command("expedition")
      sell = self.client.get_command("sell")
      strike = self.client.get_command("strike")
      trade = self.client.get_command("trade")
      attack = self.client.get_command("attack")
      construct = self.client.get_command("construct")

      
      
      # for member in self.client.get_all_members():
      #   member_data = load_member_data(member.id)
      #   member_data.maint += 1

      #   save_member_data(member.id, member_data)
        




      
      recruit.update(enabled=False)
      explore.update(enabled=False)
      sell.update(enabled=False)
      strike.update(enabled=False)
      trade.update(enabled=False)
      attack.update(enabled=False)
      construct.update(enabled=False)

      done = discord.Embed(description="**Successfully turned protocol on!**\n-\n`Recruit - Expedition - Construct - Trade - Sell - Attack - Strike` commands are now turned off", color=inv)
      await conf1.edit(embed=done)

      report = discord.Embed(title="Maintenance Protocol Activated", description=f"Activator: {ctx.author} ({ctx.author.id})", color=inv)
      await default_log.send(embed=report)

    @commands.command()
    @commands.is_owner()
    async def deactivate(self, ctx, maintenance=None):
      default_log = discord.utils.get(self.client.get_all_channels(), id=1057356641911181373)
      if maintenance != "maintenance":
        no = discord.Embed(description="did you mean `deactivate maintenance` ?", color=inv)
        await ctx.reply(embed=no)
        return
      conf = discord.Embed(description="Disabling maintenance..", color=inv)
      conf1 = await ctx.reply(embed=conf)

      
      recruit = self.client.get_command("recruit")
      explore = self.client.get_command("expedition")
      sell = self.client.get_command("sell")
      strike = self.client.get_command("strike")
      trade = self.client.get_command("trade")
      attack = self.client.get_command("attack")
      construct = self.client.get_command("construct")




      
      recruit.update(enabled=True)
      explore.update(enabled=True)
      sell.update(enabled=True)
      strike.update(enabled=True)
      trade.update(enabled=True)
      attack.update(enabled=True)
      construct.update(enabled=True)

      done = discord.Embed(description="**Successfully turned protocol off!**\n-\n`Recruit - Expedition - Construct - Trade - Sell - Attack - Strike` commands are now turned back on", color=inv)
      await conf1.edit(embed=done)

      report = discord.Embed(title="Maintenance Protocol Deactivated", description=f"Deactivator: {ctx.author} ({ctx.author.id})", color=inv)
      await default_log.send(embed=report)

async def setup(client): 
  await client.add_cog(maintenance(client)) 


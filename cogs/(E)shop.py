import discord
from discord.ext import commands
import os
import pickle
import random
import asyncio
from emojis import tank, tank2, sold, res, hearts, dead, comp, arr, wall, strike, ca, scrap, spy, medal, crate, red, green, yellow

from discord.ui import *

data_filename = "currency files/data"
class Data:
      def __init__(self, resources, soldiers, tanks, spy, wall, strikes, s, r, scrap, crate, ca, medals, cfc, cfca, mesg):
        self.resources = resources
        self.soldiers = soldiers
        self.tanks = tanks
        self.spy = spy
        self.wall = wall
        self.mesg = mesg
        self.strikes = strikes
        self.s = s
        self.r = r
        self.crate = crate
        self.medals = medals
        self.scrap = scrap
        self.ca = ca
        self.cfc = cfc
        self.cfca = cfca


class shop(commands.Cog):
    def __init__(self, client):
        self.client = client

    def cooldown(rate, per_sec=0, per_min=0, per_hour=0, type=commands.BucketType.default):
        return commands.cooldown(rate, per_sec + 60 * per_min + 3600 * per_hour, type)

    # @commands.command()
    # @commands.guild_only()
    # @cooldown(1, per_sec=40, type=commands.BucketType.user)
    # async def construct(self, ctx):
    #   member_data = load_member_data(ctx.author.id)


    #   embed1 = discord.Embed(description=f"What shall we construct, commander?\n-\nTank = {tank}\nRobotic spy = 🕵️\nWall = {wall}\nStrike = {strike}\nCrate = {crate}\nScrap = {scrap}\nCombat Aircraft = {ca}\nItems/Costs = 📋\nCancel = ❌", color=0x309730)

      
      
      
    #   confirmation = await ctx.reply(embed = embed1)

    #   await confirmation.add_reaction(tank)
    #   await confirmation.add_reaction("🕵️")
    #   await confirmation.add_reaction("🧱")
    #   await confirmation.add_reaction("🚀")
    #   await confirmation.add_reaction("📦")
    #   await confirmation.add_reaction("⚙️")
    #   await confirmation.add_reaction("🛩️")
    #   await confirmation.add_reaction("📋")
    #   await confirmation.add_reaction("❌")

      
    #   def check(reaction, user):
    #     return user == ctx.author

    #   reaction = None

    #   while True:
      
    #     if str(reaction) == tank:
    #         await confirmation.clear_reactions()
    #         # if member_data.resources >= 35:

    #         ask = discord.Embed(description=f"How many {tank} are you requesting to construct?", color=yellow)

    #         await confirmation.edit(embed=ask)
          
    #         amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)
          
            
    #         await confirmation.delete()


    #         calculation = int(amount.content) * 100

    #         confirmation2 = discord.Embed(description=f"Are you sure you want to construct {amount.content} {tank} for {calculation} {res}?", color=yellow)

    #         confirmation22 = await ctx.send(embed=confirmation2)

    #         await confirmation22.add_reaction("✅")
    #         await confirmation22.add_reaction("❌")
    #         def check(reaction, user):
    #           return user == ctx.author

    #         reaction = None

    #         while True:
    #           if str(reaction) == "✅":
    #             await confirmation22.clear_reactions()
    #             if calculation > member_data.resources:
                  
    #               error = discord.Embed(title="Insufficient Amount", description=f"Sorry commander, you dont have the required resources!\n-\n> **You need: {calculation} {res}**", color=red)
    #               await ctx.send(embed=error)
    #               ctx.command.reset_cooldown(ctx)
    #               return
    #             else:
    #               async with ctx.typing():
    #                 start = discord.Embed(description=f"[C{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start)
    #                 await asyncio.sleep(1.5)
    #                 start2 = discord.Embed(description=f"[Co{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start2)
    #                 await asyncio.sleep(1.5)
    #                 start3 = discord.Embed(description=f"[Con{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start3)
    #                 await asyncio.sleep(1.5)
    #                 start4 = discord.Embed(description=f"[Cons{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start4)
    #                 await asyncio.sleep(1.5)
    #                 start5 = discord.Embed(description=f"[Const{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start5)
    #                 await asyncio.sleep(1.5)
    #                 start6 = discord.Embed(description=f"[Constr{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start6)
    #                 await asyncio.sleep(1.5)
    #                 start7 = discord.Embed(description=f"[Constru{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start7)
    #                 await asyncio.sleep(1.5)
    #                 start8 = discord.Embed(description=f"[Construc{tank2}]", color=green)    
    #                 await confirmation22.edit(embed=start8)
    #                 await asyncio.sleep(1.5)
    #                 start9 = discord.Embed(description=f"[Construct{tank2}]", color=green)    
    #                 await confirmation22.edit(embed=start9)
    #                 await asyncio.sleep(1.5)
    #                 start10= discord.Embed(description=f"[Constructe{tank2}]", color=green)    
    #                 await confirmation22.edit(embed=start10)
    #                 await asyncio.sleep(1.5)
    #                 start11 = discord.Embed(description=f"[Constructed {tank} !]", color=green)
    #                 await confirmation22.edit(embed=start11)
    #                 await asyncio.sleep(1.5)
    #               success = discord.Embed(title="Completed Construction", description=f"**Succesfully constructed {amount.content} {tank} for ` {calculation} ` {res}**", color=green)
    #               await confirmation22.delete()
    #               await ctx.reply(embed=success)

    #               member_data.resources -= int(calculation)
    #               member_data.tanks += int(amount.content)
    #               save_member_data(ctx.author.id, member_data)
    #               return
    #           elif str(reaction) == "❌":
                
    #             await confirmation22.clear_reactions()
    #             cancel = discord.Embed(description="Construction cancelled :white_check_mark:", color=green)
    #             await confirmation22.edit(embed=cancel)
    #             ctx.command.reset_cooldown(ctx)
    #             return
    #           try:
    #             reaction, user = await self.client.wait_for("reaction_add", timeout=15.0, check=check)
    #             await confirmation22.remove_reaction(reaction, user)
    #           except:
    #             break
          
  
                                      
    #     elif str(reaction) == "🕵️":
    #         await confirmation.clear_reactions()
    #         ask = discord.Embed(description=f"How many {spy} are you requesting to construct?", color=yellow)

    #         await confirmation.edit(embed=ask)
          
    #         amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)
          
            
    #         await confirmation.delete()


    #         calculation = int(amount.content) * 190

    #         confirmation2 = discord.Embed(description=f"Are you sure you want to construct {amount.content} {spy} for {calculation} {res}?", color=yellow)

    #         confirmation22 = await ctx.send(embed=confirmation2)

    #         await confirmation22.add_reaction("✅")
    #         await confirmation22.add_reaction("❌")
    #         def check(reaction, user):
    #           return user == ctx.author

    #         reaction = None

    #         while True:
    #           if str(reaction) == "✅":
    #             await confirmation22.clear_reactions()
    #             if calculation > member_data.resources:
                  
    #               error = discord.Embed(title="Insufficient Amount", description=f"Sorry commander, you dont have the required resources!\n-\n> **You need: {calculation} {res}**", color=red)
    #               await ctx.send(embed=error)
    #               ctx.command.reset_cooldown(ctx)
    #               return
    #             else:
    #               async with ctx.typing():
    #                 start = discord.Embed(description=f"[C{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start)
    #                 await asyncio.sleep(1.5)
    #                 start2 = discord.Embed(description=f"[Co{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start2)
    #                 await asyncio.sleep(1.5)
    #                 start3 = discord.Embed(description=f"[Con{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start3)
    #                 await asyncio.sleep(1.5)
    #                 start4 = discord.Embed(description=f"[Cons{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start4)
    #                 await asyncio.sleep(1.5)
    #                 start5 = discord.Embed(description=f"[Const{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start5)
    #                 await asyncio.sleep(1.5)
    #                 start6 = discord.Embed(description=f"[Constr{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start6)
    #                 await asyncio.sleep(1.5)
    #                 start7 = discord.Embed(description=f"[Constru{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start7)
    #                 await asyncio.sleep(1.5)
    #                 start8 = discord.Embed(description=f"[Construc{tank2}]", color=green)    
    #                 await confirmation22.edit(embed=start8)
    #                 await asyncio.sleep(1.5)
    #                 start9 = discord.Embed(description=f"[Construct{tank2}]", color=green)    
    #                 await confirmation22.edit(embed=start9)
    #                 await asyncio.sleep(1.5)
    #                 start10= discord.Embed(description=f"[Constructe{tank2}]", color=green)    
    #                 await confirmation22.edit(embed=start10)
    #                 await asyncio.sleep(1.5)
    #                 start11 = discord.Embed(description=f"[Constructed {spy} !]", color=green)
    #                 await confirmation22.edit(embed=start11)
    #                 await asyncio.sleep(1.5)
    #               success = discord.Embed(title="Completed Construction", description=f"**Succesfully constructed {amount.content} {spy} for ` {calculation} ` {res}**", color=green)
    #               await confirmation22.delete()
    #               await ctx.reply(embed=success)

    #               member_data.resources -= int(calculation)
    #               member_data.spy += int(amount.content)
    #               save_member_data(ctx.author.id, member_data)
    #               return
    #           elif str(reaction) == "❌":
                
    #             await confirmation22.clear_reactions()
                
    #             cancel = discord.Embed(description="Construction cancelled :white_check_mark:", color=green)
    #             await confirmation22.edit(embed=cancel)
    #             ctx.command.reset_cooldown(ctx)
    #             return
    #           try:
    #             reaction, user = await self.client.wait_for("reaction_add", timeout=15.0, check=check)
    #             await confirmation22.remove_reaction(reaction, user)
    #           except:
    #             break
          













    #     elif str(reaction) == "📦":
    #       await confirmation.clear_reactions()
    #       if member_data.medals >= 6:
            
    #         dones = discord.Embed(description=f"Congratulations commander! you succesfully crafted **1 Crate** {crate}", color=0x309730)
    #         await confirmation.edit(embed=dones)
            
              
    #         member_data.medals -= 6
    #         # member_data.resources -= 90
    #         member_data.crate += 1
    #         save_member_data(ctx.author.id, member_data)

    #       else:
    #         error = discord.Embed(title="INSUFFICIENT AMOUNT", description=f"Sorry commander, you don't have enough {medal} to construct a crate.", color=0xFFD700)
    #         await confirmation.edit(embed=error)  
    #         ctx.command.reset_cooldown(ctx)





            

    #     elif str(reaction) == "🧱":
    #         await confirmation.clear_reactions()
    #         ask = discord.Embed(description=f"How many {wall} are you requesting to construct?", color=yellow)

    #         await confirmation.edit(embed=ask)
          
    #         amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)
          
            
    #         await confirmation.delete()


    #         calculation = int(amount.content) * 950

    #         confirmation2 = discord.Embed(description=f"Are you sure you want to construct {amount.content} {wall} for {calculation} {res}?", color=yellow)

    #         confirmation22 = await ctx.send(embed=confirmation2)

    #         await confirmation22.add_reaction("✅")
    #         await confirmation22.add_reaction("❌")
    #         def check(reaction, user):
    #           return user == ctx.author

    #         reaction = None

    #         while True:
    #           if str(reaction) == "✅":
    #             await confirmation22.clear_reactions()
    #             if calculation > member_data.resources:
                  
    #               error = discord.Embed(title="Insufficient Amount", description=f"Sorry commander, you dont have the required resources!\n-\n> **You need: {calculation} {res}**", color=red)
    #               await ctx.send(embed=error)
    #               ctx.command.reset_cooldown(ctx)
    #               return
    #             else:
    #               async with ctx.typing():
    #                 start = discord.Embed(description=f"[C{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start)
    #                 await asyncio.sleep(1.5)
    #                 start2 = discord.Embed(description=f"[Co{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start2)
    #                 await asyncio.sleep(1.5)
    #                 start3 = discord.Embed(description=f"[Con{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start3)
    #                 await asyncio.sleep(1.5)
    #                 start4 = discord.Embed(description=f"[Cons{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start4)
    #                 await asyncio.sleep(1.5)
    #                 start5 = discord.Embed(description=f"[Const{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start5)
    #                 await asyncio.sleep(1.5)
    #                 start6 = discord.Embed(description=f"[Constr{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start6)
    #                 await asyncio.sleep(1.5)
    #                 start7 = discord.Embed(description=f"[Constru{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start7)
    #                 await asyncio.sleep(1.5)
    #                 start8 = discord.Embed(description=f"[Construc{tank2}]", color=green)    
    #                 await confirmation22.edit(embed=start8)
    #                 await asyncio.sleep(1.5)
    #                 start9 = discord.Embed(description=f"[Construct{tank2}]", color=green)    
    #                 await confirmation22.edit(embed=start9)
    #                 await asyncio.sleep(1.5)
    #                 start10= discord.Embed(description=f"[Constructe{tank2}]", color=green)    
    #                 await confirmation22.edit(embed=start10)
    #                 await asyncio.sleep(1.5)
    #                 start11 = discord.Embed(description=f"[Constructed {wall} !]", color=green)
    #                 await confirmation22.edit(embed=start11)
    #                 await asyncio.sleep(1.5)
    #               success = discord.Embed(title="Completed Construction", description=f"**Succesfully constructed {amount.content} {wall} for ` {calculation} ` {res}**", color=green)
    #               await confirmation22.delete()
    #               await ctx.reply(embed=success)

    #               member_data.resources -= int(calculation)
    #               member_data.wall += int(amount.content)
    #               save_member_data(ctx.author.id, member_data)
    #               return
    #           elif str(reaction) == "❌":
                
    #             await confirmation22.clear_reactions()
                
    #             cancel = discord.Embed(description="Construction cancelled :white_check_mark:", color=green)
    #             await confirmation22.edit(embed=cancel)
    #             ctx.command.reset_cooldown(ctx)
    #             return
    #           try:
    #             reaction, user = await self.client.wait_for("reaction_add", timeout=15.0, check=check)
    #             await confirmation22.remove_reaction(reaction, user)
                
    #           except:
    #             break  
    #     elif str(reaction) == "🚀":
    #         await confirmation.clear_reactions()
    #         ask = discord.Embed(description=f"How many {strike} are you requesting to construct?", color=yellow)

    #         await confirmation.edit(embed=ask)
          
    #         amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)
          
            
    #         await confirmation.delete()


    #         calculation = int(amount.content) * 1600

    #         confirmation2 = discord.Embed(description=f"Are you sure you want to construct {amount.content} {strike} for {calculation} {res}?", color=yellow)

    #         confirmation22 = await ctx.send(embed=confirmation2)

    #         await confirmation22.add_reaction("✅")
    #         await confirmation22.add_reaction("❌")
    #         def check(reaction, user):
    #           return user == ctx.author

    #         reaction = None

    #         while True:
    #           if str(reaction) == "✅":
    #             await confirmation22.clear_reactions()
    #             if calculation > member_data.resources:
                  
    #               error = discord.Embed(title="Insufficient Amount", description=f"Sorry commander, you dont have the required resources!\n-\n> **You need: {calculation} {res}**", color=red)
    #               await ctx.send(embed=error)
    #               ctx.command.reset_cooldown(ctx)
    #               return
    #             else:
    #               async with ctx.typing():
    #                 start = discord.Embed(description=f"[C{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start)
    #                 await asyncio.sleep(1.5)
    #                 start2 = discord.Embed(description=f"[Co{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start2)
    #                 await asyncio.sleep(1.5)
    #                 start3 = discord.Embed(description=f"[Con{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start3)
    #                 await asyncio.sleep(1.5)
    #                 start4 = discord.Embed(description=f"[Cons{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start4)
    #                 await asyncio.sleep(1.5)
    #                 start5 = discord.Embed(description=f"[Const{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start5)
    #                 await asyncio.sleep(1.5)
    #                 start6 = discord.Embed(description=f"[Constr{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start6)
    #                 await asyncio.sleep(1.5)
    #                 start7 = discord.Embed(description=f"[Constru{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start7)
    #                 await asyncio.sleep(1.5)
    #                 start8 = discord.Embed(description=f"[Construc{tank2}]", color=green)    
    #                 await confirmation22.edit(embed=start8)
    #                 await asyncio.sleep(1.5)
    #                 start9 = discord.Embed(description=f"[Construct{tank2}]", color=green)    
    #                 await confirmation22.edit(embed=start9)
    #                 await asyncio.sleep(1.5)
    #                 start10= discord.Embed(description=f"[Constructe{tank2}]", color=green)    
    #                 await confirmation22.edit(embed=start10)
    #                 await asyncio.sleep(1.5)
    #                 start11 = discord.Embed(description=f"[Constructed {strike} !]", color=green)
    #                 await confirmation22.edit(embed=start11)
    #                 await asyncio.sleep(1.5)
    #               success = discord.Embed(title="Completed Construction", description=f"**Succesfully constructed {amount.content} {strike} for ` {calculation} ` {res}**", color=green)
    #               await confirmation22.delete()
    #               await ctx.reply(embed=success)

    #               member_data.resources -= int(calculation)
    #               member_data.strikes += int(amount.content)
    #               save_member_data(ctx.author.id, member_data)
    #               return
    #           elif str(reaction) == "❌":
                
    #             await confirmation22.clear_reactions()
                
    #             cancel = discord.Embed(description="Construction cancelled :white_check_mark:", color=green)
    #             await confirmation22.edit(embed=cancel)
    #             ctx.command.reset_cooldown(ctx)
    #             return
    #           try:
    #             reaction, user = await self.client.wait_for("reaction_add", timeout=15.0, check=check)
    #             await confirmation22.remove_reaction(reaction, user)
    #           except:
    #             break
          
          

  
    #     elif str(reaction) == "🛩️":
    #         await confirmation.clear_reactions()
    #         ask = discord.Embed(description=f"How many {ca} are you requesting to construct?", color=yellow)

    #         await confirmation.edit(embed=ask)
          
    #         amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)
          
            
    #         await confirmation.delete()


    #         calculation = int(amount.content) * 7

    #         confirmation2 = discord.Embed(description=f"Are you sure you want to construct {amount.content} {ca} for {calculation} {scrap}?", color=yellow)

    #         confirmation22 = await ctx.send(embed=confirmation2)

    #         await confirmation22.add_reaction("✅")
    #         await confirmation22.add_reaction("❌")
    #         def check(reaction, user):
    #           return user == ctx.author

    #         reaction = None

    #         while True:
    #           if str(reaction) == "✅":
    #             await confirmation22.clear_reactions()
    #             if calculation > member_data.scrap:
                  
    #               error = discord.Embed(title="Insufficient Amount", description=f"Sorry commander, you dont have the required resources!\n-\n> **You need: {calculation} {scrap}**", color=red)
    #               await ctx.send(embed=error)
    #               ctx.command.reset_cooldown(ctx)
    #               return
    #             else:
    #               async with ctx.typing():
    #                 start = discord.Embed(description=f"[C{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start)
    #                 await asyncio.sleep(1.5)
    #                 start2 = discord.Embed(description=f"[Co{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start2)
    #                 await asyncio.sleep(1.5)
    #                 start3 = discord.Embed(description=f"[Con{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start3)
    #                 await asyncio.sleep(1.5)
    #                 start4 = discord.Embed(description=f"[Cons{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start4)
    #                 await asyncio.sleep(1.5)
    #                 start5 = discord.Embed(description=f"[Const{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start5)
    #                 await asyncio.sleep(1.5)
    #                 start6 = discord.Embed(description=f"[Constr{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start6)
    #                 await asyncio.sleep(1.5)
    #                 start7 = discord.Embed(description=f"[Constru{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start7)
    #                 await asyncio.sleep(1.5)
    #                 start8 = discord.Embed(description=f"[Construc{tank2}]", color=green)    
    #                 await confirmation22.edit(embed=start8)
    #                 await asyncio.sleep(1.5)
    #                 start9 = discord.Embed(description=f"[Construct{tank2}]", color=green)    
    #                 await confirmation22.edit(embed=start9)
    #                 await asyncio.sleep(1.5)
    #                 start10= discord.Embed(description=f"[Constructe{tank2}]", color=green)    
    #                 await confirmation22.edit(embed=start10)
    #                 await asyncio.sleep(1.5)
    #                 start11 = discord.Embed(description=f"[Constructed {ca} !]", color=green)
    #                 await confirmation22.edit(embed=start11)
    #                 await asyncio.sleep(1.5)
    #               success = discord.Embed(title="Completed Construction", description=f"**Succesfully constructed {amount.content} {ca} for ` {calculation} ` {scrap}**", color=green)
    #               await confirmation22.delete()
    #               await ctx.reply(embed=success)

    #               member_data.scrap -= int(calculation)
    #               member_data.ca += int(amount.content)
    #               save_member_data(ctx.author.id, member_data)
    #               return
    #           elif str(reaction) == "❌":
                
    #             await confirmation22.clear_reactions()
                
    #             cancel = discord.Embed(description="Construction cancelled :white_check_mark:", color=green)
    #             await confirmation22.edit(embed=cancel)
    #             ctx.command.reset_cooldown(ctx)
    #             return
    #           try:
    #             reaction, user = await self.client.wait_for("reaction_add", timeout=15.0, check=check)
    #             await confirmation22.remove_reaction(reaction, user)
    #           except:
    #             break
    #     elif str(reaction) == "⚙️":
    #         await confirmation.clear_reactions()
    #         ask = discord.Embed(description=f"How many {scrap} are you requesting to construct?", color=yellow)

    #         await confirmation.edit(embed=ask)
          
    #         amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)
          
            
    #         await confirmation.delete()


    #         calculation = int(amount.content) * 1000

    #         confirmation2 = discord.Embed(description=f"Are you sure you want to construct {amount.content} {scrap} for {calculation} {res}?", color=yellow)

    #         confirmation22 = await ctx.send(embed=confirmation2)

    #         await confirmation22.add_reaction("✅")
    #         await confirmation22.add_reaction("❌")
    #         def check(reaction, user):
    #           return user == ctx.author

    #         reaction = None

    #         while True:
    #           if str(reaction) == "✅":
    #             await confirmation22.clear_reactions()
    #             if calculation > member_data.resources:
                  
    #               error = discord.Embed(title="Insufficient Amount", description=f"Sorry commander, you dont have the required resources!\n-\n> **You need: {calculation} {res}**", color=red)
    #               await ctx.send(embed=error)
    #               ctx.command.reset_cooldown(ctx)
    #               return
    #             else:
    #               async with ctx.typing():
    #                 start = discord.Embed(description=f"[C{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start)
    #                 await asyncio.sleep(1.5)
    #                 start2 = discord.Embed(description=f"[Co{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start2)
    #                 await asyncio.sleep(1.5)
    #                 start3 = discord.Embed(description=f"[Con{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start3)
    #                 await asyncio.sleep(1.5)
    #                 start4 = discord.Embed(description=f"[Cons{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start4)
    #                 await asyncio.sleep(1.5)
    #                 start5 = discord.Embed(description=f"[Const{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start5)
    #                 await asyncio.sleep(1.5)
    #                 start6 = discord.Embed(description=f"[Constr{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start6)
    #                 await asyncio.sleep(1.5)
    #                 start7 = discord.Embed(description=f"[Constru{tank2}]", color=green)
    #                 await confirmation22.edit(embed=start7)
    #                 await asyncio.sleep(1.5)
    #                 start8 = discord.Embed(description=f"[Construc{tank2}]", color=green)    
    #                 await confirmation22.edit(embed=start8)
    #                 await asyncio.sleep(1.5)
    #                 start9 = discord.Embed(description=f"[Construct{tank2}]", color=green)    
    #                 await confirmation22.edit(embed=start9)
    #                 await asyncio.sleep(1.5)
    #                 start10= discord.Embed(description=f"[Constructe{tank2}]", color=green)    
    #                 await confirmation22.edit(embed=start10)
    #                 await asyncio.sleep(1.5)
    #                 start11 = discord.Embed(description=f"[Constructed {scrap} !]", color=green)
    #                 await confirmation22.edit(embed=start11)
    #                 await asyncio.sleep(1.5)
    #               success = discord.Embed(title="Completed Construction", description=f"**Succesfully constructed {amount.content} {scrap} for ` {calculation} ` {res}**", color=green)
    #               await confirmation22.delete()
    #               await ctx.reply(embed=success)

    #               member_data.resources -= int(calculation)
    #               member_data.scrap += int(amount.content)
    #               save_member_data(ctx.author.id, member_data)
                  
    #               return
    #           elif str(reaction) == "❌":
                
    #             await confirmation22.clear_reactions()
                
    #             cancel = discord.Embed(description="Construction cancelled :white_check_mark:", color=green)
    #             await confirmation22.edit(embed=cancel)
    #             ctx.command.reset_cooldown(ctx)
    #             return
    #           try:
    #             reaction, user = await self.client.wait_for("reaction_add", timeout=15.0, check=check)
    #             await confirmation22.remove_reaction(reaction, user)
    #           except:
    #             break
    #     elif str(reaction) == "📋":
    #       await confirmation.clear_reactions()
    #       weapons = discord.Embed(description=f"Tank {tank} = **100 {res}**\n-\nRobotic Spy :detective: = **190** {res}\n-\nWall {wall} = **950** {res}\n-\nStrike {strike} = **1600** {res}\n-\nCrate {crate} = **6** {medal}\n-\nScrap {scrap} = **1000** {res}\n-\nCombat Aircraft {ca} = **7 {scrap}**", color=green)
          
    #       await confirmation.edit(embed=weapons)
    #       ctx.command.reset_cooldown(ctx)
    #       return
            
    #     elif str(reaction) == "❌":
    #       await confirmation.clear_reactions()
    #       cancel = discord.Embed(description="Cancelled construction :thumbsup:", color=0xFF0000)
          
    #       await confirmation.edit(embed=cancel)
    #       ctx.command.reset_cooldown(ctx)

    #     try:
    #           reaction, user = await self.client.wait_for("reaction_add", timeout=35.0, check=check)
    #           await confirmation.remove_reaction(reaction, user)
    #     except:
    #            break







    @commands.command(aliases = ["cons"])
    @commands.guild_only()
    @cooldown(1, per_sec=35, type=commands.BucketType.user)
    async def construct(self, ctx):
      member_data = load_member_data(ctx.author.id)
      
      construct_options = Select(placeholder="Select a construction option",options=[

           discord.SelectOption(label="Prices and Lists", value="list", emoji="📋"),
           discord.SelectOption(label="Cancel", value="cancel", emoji="❌"),
           discord.SelectOption(label="Tank", value="tank", emoji=discord.PartialEmoji.from_str("<:tank:1042497974426665020>")),
           discord.SelectOption(label="Spy", value="spy", emoji="🕵️"),
           discord.SelectOption(label="Wall", value="wall", emoji="🧱"),
           discord.SelectOption(label="Strike", value="strike", emoji="🚀"),
           discord.SelectOption(label="Crate", value="crate", emoji="📦"),
           discord.SelectOption(label="Scrap", value="scrap", emoji="⚙️"),
           discord.SelectOption(label="Combat Aircraft", value="ca", emoji="🛩️"),
           
           

         ])
      

      co = View()
      co.add_item(construct_options)


      embed1 = discord.Embed(description=f"What shall we construct, commander?", color=green)

      confirmation = await ctx.reply(embed = embed1, view=co)
      

      async def options(interaction):
        if interaction.user == ctx.author:
          if construct_options.values[0] == "tank":
              ask = discord.Embed(description=f"How many {tank} are you requesting to construct?", color=yellow)
      
              await confirmation.edit(embed=ask, view=None)
              amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)

              if not amount.content[0].isnumeric():
                invamount = discord.Embed(title="Invalid Amount", description=f"Sorry, `{amount.content}` is an invalid integer/number, please include an integer and nothing else.\n`Ex. (1 --> 100)`", color=red)
                await amount.reply(embed=invamount)
                return
                
                  
              await confirmation.delete()
      
      
              calculation = int(amount.content) * 200
              
      
              button_check = Button(label = "✔", style=discord.ButtonStyle.green)
              button_x = Button(label = "❌", style=discord.ButtonStyle.red)
      
              view = View()
              view.add_item(button_check)
              view.add_item(button_x)
      
              confirmation2 = discord.Embed(description=f"Are you sure you want to construct {amount.content} {tank} for {calculation} {res}?", color=yellow)
              confirm22 = await amount.reply(embed=confirmation2, view=view)
      
              async def button_check_c(interaction):
                await confirm22.delete()
                if member_data.resources < int(calculation):
                  error = discord.Embed(title="Insufficient Amount", description=f"Sorry commander, you dont have the required resources!\n-\n> **You need: {calculation} {res}**", color=red)
                  await amount.reply(embed=error)
                  ctx.command.reset_cooldown(ctx)
                  return
                else:
                  success = discord.Embed(title="Completed Construction", description=f"**Succesfully constructed {amount.content} {tank} for ` {calculation} ` {res}**", color=green)
                  await ctx.reply(embed=success, view=None)
                  member_data.resources -= int(calculation)
                  member_data.tanks += int(amount.content)
                  save_member_data(ctx.author.id, member_data)
                  return
                
              async def button_x_c(interaction):
                cancel = discord.Embed(description="Construction cancelled :white_check_mark:", color=green)
                await confirm22.edit(embed=cancel, view=None)
                ctx.command.reset_cooldown(ctx)
                return
  
              button_check.callback = button_check_c
              button_x.callback = button_x_c
  
    
  
          elif construct_options.values[0] == "spy":
            ask = discord.Embed(description=f"How many {spy} are you requesting to construct?", color=yellow)
            await confirmation.edit(embed=ask, view=None)
            
            amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)

            if not amount.content[0].isnumeric():
                invamount = discord.Embed(title="Invalid Amount", description=f"Sorry, `{amount.content}` is an invalid integer/number, please include an integer and nothing else.\n`Ex. (1 --> 100)`", color=red)
                await amount.reply(embed=invamount)
                return
            
              
            await confirmation.delete()
  
            button_check = Button(label = "✔", style=discord.ButtonStyle.green)
            button_x = Button(label = "❌", style=discord.ButtonStyle.red)
      
            view = View()
            view.add_item(button_check)
            view.add_item(button_x)
  
            calculation = int(amount.content) * 285
  
            confirmation2 = discord.Embed(description=f"Are you sure you want to construct {amount.content} {spy} for {calculation} {res}?", color=yellow)
            confirm22 = await amount.reply(embed=confirmation2, view=view)
  
            async def button_check_c(interaction):
                await confirm22.delete()
                if member_data.resources < int(calculation):
                  error = discord.Embed(title="Insufficient Amount", description=f"Sorry commander, you dont have the required resources!\n-\n> **You need: {calculation} {res}**", color=red)
                  await amount.reply(embed=error)
                  ctx.command.reset_cooldown(ctx)
                  return
                else:
                  success = discord.Embed(title="Completed Construction", description=f"**Succesfully constructed {amount.content} {spy} for ` {calculation} ` {res}**", color=green)
                  await ctx.reply(embed=success, view=None)
                  member_data.resources -= int(calculation)
                  member_data.spy += int(amount.content)
                  save_member_data(ctx.author.id, member_data)
                  return
                
            async def button_x_c(interaction):
                cancel = discord.Embed(description="Construction cancelled :white_check_mark:", color=green)
                await confirm22.edit(embed=cancel, view=None)
                ctx.command.reset_cooldown(ctx)
                return
  
            button_check.callback = button_check_c
            button_x.callback = button_x_c
  
  
  
  
  
  
          
          elif construct_options.values[0] == "wall":
            ask = discord.Embed(description=f"How many {wall} are you requesting to construct?", color=yellow)
            await confirmation.edit(embed=ask, view=None)
            
            amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)

            if not amount.content[0].isnumeric():
                invamount = discord.Embed(title="Invalid Amount", description=f"Sorry, `{amount.content}` is an invalid integer/number, please include an integer and nothing else.\n`Ex. (1 --> 100)`", color=red)
                await amount.reply(embed=invamount)
                return
            
              
            await confirmation.delete()
  
            button_check = Button(label = "✔", style=discord.ButtonStyle.green)
            button_x = Button(label = "❌", style=discord.ButtonStyle.red)
      
            view = View()
            view.add_item(button_check)
            view.add_item(button_x)
  
            calculation = int(amount.content) * 1000
  
            confirmation2 = discord.Embed(description=f"Are you sure you want to construct {amount.content} {wall} for {calculation} {res}?", color=yellow)
            confirm22 = await amount.reply(embed=confirmation2, view=view)
  
            async def button_check_c(interaction):
                await confirm22.delete()
                if member_data.resources < int(calculation):
                  error = discord.Embed(title="Insufficient Amount", description=f"Sorry commander, you dont have the required resources!\n-\n> **You need: {calculation} {res}**", color=red)
                  await amount.reply(embed=error)
                  ctx.command.reset_cooldown(ctx)
                  return
                else:
                  success = discord.Embed(title="Completed Construction", description=f"**Succesfully constructed {amount.content} {wall} for ` {calculation} ` {res}**", color=green)
                  await ctx.reply(embed=success, view=None)
                  member_data.resources -= int(calculation)
                  member_data.wall += int(amount.content)
                  save_member_data(ctx.author.id, member_data)
                  return
                
            async def button_x_c(interaction):
                cancel = discord.Embed(description="Construction cancelled :white_check_mark:", color=green)
                await confirm22.edit(embed=cancel, view=None)
                ctx.command.reset_cooldown(ctx)
                return
  
            button_check.callback = button_check_c
            button_x.callback = button_x_c
          elif construct_options.values[0] == "strike":
            ask = discord.Embed(description=f"How many {strike} are you requesting to construct?", color=yellow)
            await confirmation.edit(embed=ask, view=None)
            
            amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)

            if not amount.content[0].isnumeric():
                invamount = discord.Embed(title="Invalid Amount", description=f"Sorry, `{amount.content}` is an invalid integer/number, please include an integer and nothing else.\n`Ex. (1 --> 100)`", color=red)
                await amount.reply(embed=invamount)
                return
            
              
            await confirmation.delete()
  
            button_check = Button(label = "✔", style=discord.ButtonStyle.green)
            button_x = Button(label = "❌", style=discord.ButtonStyle.red)
      
            view = View()
            view.add_item(button_check)
            view.add_item(button_x)
  
            calculation = int(amount.content) * 1150
  
            confirmation2 = discord.Embed(description=f"Are you sure you want to construct {amount.content} {strike} for {calculation} {res}?", color=yellow)
            confirm22 = await amount.reply(embed=confirmation2, view=view)
  
            async def button_check_c(interaction):
                await confirm22.delete()
                if member_data.resources < int(calculation):
                  error = discord.Embed(title="Insufficient Amount", description=f"Sorry commander, you dont have the required resources!\n-\n> **You need: {calculation} {res}**", color=red)
                  await amount.reply(embed=error)
                  ctx.command.reset_cooldown(ctx)
                  return
                else:
                  success = discord.Embed(title="Completed Construction", description=f"**Succesfully constructed {amount.content} {strike} for ` {calculation} ` {res}**", color=green)
                  await ctx.reply(embed=success, view=None)
                  member_data.resources -= int(calculation)
                  member_data.strikes += int(amount.content)
                  save_member_data(ctx.author.id, member_data)
                  return
                
            async def button_x_c(interaction):
                cancel = discord.Embed(description="Construction cancelled :white_check_mark:", color=green)
                await confirm22.edit(embed=cancel, view=None)
                ctx.command.reset_cooldown(ctx)
                return
  
            button_check.callback = button_check_c
            button_x.callback = button_x_c
          elif construct_options.values[0] == "scrap":
            ask = discord.Embed(description=f"How many {scrap} are you requesting to construct?", color=yellow)
            await confirmation.edit(embed=ask, view=None)
            
            amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)

            if not amount.content[0].isnumeric():
                invamount = discord.Embed(title="Invalid Amount", description=f"Sorry, `{amount.content}` is an invalid integer/number, please include an integer and nothing else.\n`Ex. (1 --> 100)`", color=red)
                await amount.reply(embed=invamount)
                return
            
              
            await confirmation.delete()
  
            button_check = Button(label = "✔", style=discord.ButtonStyle.green)
            button_x = Button(label = "❌", style=discord.ButtonStyle.red)
      
            view = View()
            view.add_item(button_check)
            view.add_item(button_x)
  
            calculation = int(amount.content) * 2000
  
            confirmation2 = discord.Embed(description=f"Are you sure you want to construct {amount.content} {scrap} for {calculation} {res}?", color=yellow)
            confirm22 = await amount.reply(embed=confirmation2, view=view)
  
            async def button_check_c(interaction):
                await confirm22.delete()
                if member_data.resources < int(calculation):
                  error = discord.Embed(title="Insufficient Amount", description=f"Sorry commander, you dont have the required resources!\n-\n> **You need: {calculation} {res}**", color=red)
                  await amount.reply(embed=error)
                  ctx.command.reset_cooldown(ctx)
                  return
                else:
                  success = discord.Embed(title="Completed Construction", description=f"**Succesfully constructed {amount.content} {scrap} for ` {calculation} ` {res}**", color=green)
                  await ctx.reply(embed=success, view=None)
                  member_data.resources -= int(calculation)
                  member_data.scrap += int(amount.content)
                  save_member_data(ctx.author.id, member_data)
                  return
                
            async def button_x_c(interaction):
                cancel = discord.Embed(description="Construction cancelled :white_check_mark:", color=green)
                await confirm22.edit(embed=cancel, view=None)
                ctx.command.reset_cooldown(ctx)
                return
  
            button_check.callback = button_check_c
            button_x.callback = button_x_c
          # elif select.values[0] == "tank":
  
  
          
          elif construct_options.values[0] == "crate":
            ask = discord.Embed(description=f"How many {crate} are you requesting to construct?", color=yellow)
            await confirmation.edit(embed=ask, view=None)
            
            amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)

            if not amount.content[0].isnumeric():
                invamount = discord.Embed(title="Invalid Amount", description=f"Sorry, `{amount.content}` is an invalid integer/number, please include an integer and nothing else.\n`Ex. (1 --> 100)`", color=red)
                await amount.reply(embed=invamount)
                return
            
              
            await confirmation.delete()
  
            button_check = Button(label = "✔", style=discord.ButtonStyle.green)
            button_x = Button(label = "❌", style=discord.ButtonStyle.red)
      
            view = View()
            view.add_item(button_check)
            view.add_item(button_x)
  
            calculation = int(amount.content) * 5
  
            confirmation2 = discord.Embed(description=f"Are you sure you want to construct {amount.content} {crate} for {calculation} {medal}?", color=yellow)
            confirm22 = await amount.reply(embed=confirmation2, view=view)
  
            async def button_check_c(interaction):
                await confirm22.delete()
                if member_data.medal < int(calculation):
                  error = discord.Embed(title="Insufficient Amount", description=f"Sorry commander, you dont have the required resources!\n-\n> **You need: {calculation} {medal}**", color=red)
                  await amount.reply(embed=error)
                  ctx.command.reset_cooldown(ctx)
                  return
                else:
                  success = discord.Embed(title="Completed Construction", description=f"**Succesfully constructed {amount.content} {crate} for ` {calculation} ` {medal}**", color=green)
                  await ctx.reply(embed=success, view=None)
                  member_data.medals -= int(calculation)
                  member_data.crate += int(amount.content)
                  save_member_data(ctx.author.id, member_data)
                  return
                
            async def button_x_c(interaction):
                cancel = discord.Embed(description="Construction cancelled :white_check_mark:", color=green)
                await confirm22.edit(embed=cancel, view=None)
                ctx.command.reset_cooldown(ctx)
                return
  
            button_check.callback = button_check_c
            button_x.callback = button_x_c
          elif construct_options.values[0] == "list":
            weapons = discord.Embed(description=f"Tank {tank} = **200 {res}**\n-\nRobotic Spy :detective: = **285** {res}\n-\nWall {wall} = **1000** {res}\n-\nStrike {strike} = **1150** {res}\n-\nCrate {crate} = **5** {medal}\n-\nScrap {scrap} = **2000** {res}\n-\nCombat Aircraft {ca} = **5 {scrap}**", color=green)
            await interaction.response.send_message("These prices differ from event to event, don't forget to check them frequently! stay theta :D", ephemeral=True)
            
            await confirmation.edit(embed=weapons, view=co)
          elif construct_options.values[0] == "cancel":
            cancel = discord.Embed(description="Cancelled construction :thumbsup:", color=0xFF0000)
            await confirmation.edit(embed=cancel, view=None)
            ctx.command.reset_cooldown(ctx)
            return
          elif construct_options.values[0] == "ca":    
            ask = discord.Embed(description=f"How many {ca} are you requesting to construct?", color=yellow)
            await confirmation.edit(embed=ask, view=None)
            
            amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)

            if not amount.content[0].isnumeric():
                invamount = discord.Embed(title="Invalid Amount", description=f"Sorry, `{amount.content}` is an invalid integer/number, please include an integer and nothing else.\n`Ex. (1 --> 100)`", color=red)
                await amount.reply(embed=invamount)
                return
            
              
            await confirmation.delete()
  
            button_check = Button(label = "✔", style=discord.ButtonStyle.green)
            button_x = Button(label = "❌", style=discord.ButtonStyle.red)
      
            view = View()
            view.add_item(button_check)
            view.add_item(button_x)
  
            calculation = int(amount.content) * 5
  
            confirmation2 = discord.Embed(description=f"Are you sure you want to construct {amount.content} {ca} for {calculation} {scrap}?", color=yellow)
            confirm22 = await amount.reply(embed=confirmation2, view=view)
  
            async def button_check_c(interaction):
                await confirm22.delete()
                if member_data.scrap < int(calculation):
                  error = discord.Embed(title="Insufficient Amount", description=f"Sorry commander, you dont have the required resources!\n-\n> **You need: {calculation} {scrap}**", color=red)
                  await amount.reply(embed=error)
                  ctx.command.reset_cooldown(ctx)
                  return
                else:
                  success = discord.Embed(title="Completed Construction", description=f"**Succesfully constructed {amount.content} {ca} for ` {calculation} ` {scrap}**", color=green)
                  await ctx.reply(embed=success, view=None)
                  member_data.scrap -= int(calculation)
                  member_data.ca += int(amount.content)
                  save_member_data(ctx.author.id, member_data)
                  return
                
            async def button_x_c(interaction):
                cancel = discord.Embed(description="Construction cancelled :white_check_mark:", color=green)
                await confirm22.edit(embed=cancel, view=None)
                ctx.command.reset_cooldown(ctx)
                return
  
            button_check.callback = button_check_c
            button_x.callback = button_x_c
        else:
          await interaction.response.send_message("This menu is not for you!", ephemeral=True)
      construct_options.callback = options

        
        

      
      




  

      






async def setup(client):
    await client.add_cog(shop(client))   

def load_data():
        if os.path.isfile(data_filename):
            with open(data_filename, "rb") as file:
                return pickle.load(file)
        else:
            return dict()

def load_member_data(member_ID):
    data = load_data()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]

def save_member_data(member_ID, member_data):
    data = load_data()

    data[member_ID] = member_data

    with open(data_filename, "wb") as file:
        pickle.dump(data, file)







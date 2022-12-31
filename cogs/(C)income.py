import discord
from discord.ext import commands
import os
import pickle
import random
import asyncio
import json
from emojis import tank, tank2, sold, res, hearts, dead, comp, arr, wall, strike, ca, scrap, spy, medal, crate, red, green, yellow, crates, ar, inv, disabled
from places import desert, ba, ruins

from discord.ui import *
from discord import app_commands



data_filename = "currency files/data"
data_filename2 = "levels/levels"

class Data:
      def __init__(self, resources, soldiers, tanks, spy, wall, strikes, s, r, scrap, crate, ca, medals, cfc, cfca, mesg, xp, level):
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
        self.level = level


class income(commands.Cog):
    def __init__(self, client):
        self.client = client

    def cooldown(rate, per_sec=0, per_min=0, per_hour=0, type=commands.BucketType.default):
        return commands.cooldown(rate, per_sec + 60 * per_min + 3600 * per_hour, type) 

  


    
          
          


#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#------------------------------------------------------------------------- #-------------------------------------------------------------------------   

    @commands.hybrid_command(description="Recruit some soldiers!", aliases = ["Recruit"]) 
    @commands.guild_only()
    @cooldown(1, per_sec=15, type=commands.BucketType.user)
    async def recruit(self, ctx):
        
        
      
        member_data = load_member_data(ctx.author.id)
      
        option = random.randrange(30,40)
      
      
        member_data.soldiers += int(option)

        s2 = discord.Embed(description=f"**Recruit sequence completed**, you recruited **{option} {sold}**", color=inv)
        

        await ctx.reply(embed=s2)
      
        save_member_data(ctx.author.id, member_data)
        member_data2 = load_member_data2(ctx.author.id)
        member_data2.xp += 1
        save_member_data2(ctx.author.id, member_data2)
        if member_data.s >= 150:
          pass
        if member_data.s < 150:
          member_data.s += 1
          save_member_data(ctx.author.id, member_data)

        default_log = discord.utils.get(self.client.get_all_channels(), id=1057356641911181373)

        try:
          log = discord.Embed(description=f"**{ctx.author.name}#{ctx.author.discriminator}** just recruited `{option}` {sold}\n-\nFrom: {ctx.guild.name} server", color=inv)
          await default_log.send(embed=log)
        except:
          pass
        

      
#-------------------------------------------------------------------------
#---------------------------------------------------------------------------


    
    @commands.hybrid_command(description="Collect and search for some resources!",aliases = ["explore", "Explore"])
    @commands.guild_only()
    @cooldown(1, per_sec=15, type=commands.BucketType.user)
    # @cooldown(1, per_sec=5, type=commands.BucketType.user)
    async def expedition(self, ctx):

      not_you = discord.Embed(description=f"This action cannot be done by you {disabled}", color=inv)

      
      
      member_data = load_member_data(ctx.author.id)

       

      ruinsc = random.randrange(60,80)

      dec = random.randrange(40,80)
    
      bac = random.randrange(50,80)
      pr = Button(label = f"{ruins}", style=discord.ButtonStyle.green)
      pb = Button(label=f"{ba}", style=discord.ButtonStyle.green)
      pd = Button(label = f"{desert}", style=discord.ButtonStyle.green)
      ruins_chosen = discord.Embed(title="The Ruins", description=f"These ruins might clearly have some resources, you checked under a big stone and found **{ruinsc} {res}**", color=red)
      ruins_chosen_b = Button(label = f"{ruins}", style=discord.ButtonStyle.green, disabled=True)
      desert_chosen = discord.Embed(title="The Desert", description=f"This prototype of hell must have something hidden, you search inside a dead animal's skull and find **{dec} {res}**", color=red)
      desert_chosen_b = Button(label = f"{desert}", style=discord.ButtonStyle.green, disabled=True)
      base_chosen = discord.Embed(title="The Abandone Base", description=f"This area is left over, you spectate the storage room and find **{bac} {res}**", color=red)
      base_chosen_b = Button(label=f"{ba}", style=discord.ButtonStyle.green, disabled=True)
      
      view = View()
      view.add_item(pr)
      view.add_item(pb)
      view.add_item(pd)
      
        
    
      
        
        
       
      
       
      search = discord.Embed(description=f"**Where do you want to complete your expedition?**", color=inv)
      rep = await ctx.reply(embed=search, view=view)
      


      #functions
      async def button_callback_ruins(interaction):
        if interaction.user == ctx.author:

          view.clear_items()
          view_ruins = View()
          view_ruins.add_item(ruins_chosen_b)
          
          res_b1 = member_data.resources
          res_b11 = member_data.resources + ruinsc
          if res_b1 < 0:
            res_b1 = 0
          
          await rep.edit(embed=ruins_chosen, view=view_ruins)
          member_data.resources += int(ruinsc)
          save_member_data(ctx.author.id, member_data) 
          await interaction.response.send_message(f"{res_b1} {res} {ar} {res_b11} {res}", ephemeral=True)
          
          member_data2 = load_member_data2(ctx.author.id)
          member_data2.xp += 1
          save_member_data2(ctx.author.id, member_data2)
  
        
          if member_data.r >= 150:
            pass
          if member_data.r < 150:
             member_data.r += 1
             save_member_data(ctx.author.id, member_data)

          default_log = discord.utils.get(self.client.get_all_channels(), id=1057356641911181373)

          try:
            log = discord.Embed(description=f"**{ctx.author.name}#{ctx.author.discriminator}** just caught `{ruinsc}` {res}\n-\nFrom: {ctx.guild.name} server", color=inv)
            await default_log.send(embed=log)
          except:
            pass
          return
        else:
          await interaction.response.send_message(embed=not_you, ephemeral=True)

      async def button_callback_base(interaction):
        if interaction.user == ctx.author:
          view.clear_items()
  
          view_base = View()
          view_base.add_item(base_chosen_b)
  
          res_b2 = member_data.resources
          res_b22 = member_data.resources + bac
          if res_b2 < 0:
            res_b2 = 0
          await rep.edit(embed=base_chosen, view=view_base)
          member_data.resources += int(bac)
          save_member_data(ctx.author.id, member_data) 
          await interaction.response.send_message(f"{res_b2} {res} {ar} {res_b22} {res}", ephemeral=True)

          member_data2 = load_member_data2(ctx.author.id)
          member_data2.xp += 1
          save_member_data2(ctx.author.id, member_data2)
  
          if member_data.r >= 150:
            pass
          if member_data.r < 150:
             member_data.r += 1
             save_member_data(ctx.author.id, member_data)

          default_log = discord.utils.get(self.client.get_all_channels(), id=1057356641911181373)

          try:
            log = discord.Embed(description=f"**{ctx.author.name}#{ctx.author.discriminator}** just caught `{bac}` {res}\n-\nFrom: {ctx.guild.name} server", color=inv)
            await default_log.send(embed=log)
          except:
            pass
          return

          
        else:
          await interaction.response.send_message(embed=not_you, ephemeral=True)

      async def button_callback_desert(interaction):
        if interaction.user == ctx.author:
          view.clear_items()
          view_desert = View()
          view_desert.add_item(desert_chosen_b)
          res_b3 = member_data.resources
          res_b33 = member_data.resources + dec
          if res_b3 < 0:
            res_b3 = 0
          await rep.edit(embed=desert_chosen, view=view_desert)
          member_data.resources += int(dec)
          save_member_data(ctx.author.id, member_data) 
          await interaction.response.send_message(f"{res_b3} {res} {ar} {res_b33} {res}", ephemeral=True)

          member_data2 = load_member_data2(ctx.author.id)
          member_data2.xp += 1
          save_member_data2(ctx.author.id, member_data2)
          
          if member_data.r >= 150:
            pass
          if member_data.r < 150:
             member_data.r += 1
             save_member_data(ctx.author.id, member_data)

          default_log = discord.utils.get(self.client.get_all_channels(), id=1057356641911181373)

          try:
            log = discord.Embed(description=f"**{ctx.author.name}#{ctx.author.discriminator}** just caught `{dec}` {res}\n-\nFrom: {ctx.guild.name} server", color=inv)
            await default_log.send(embed=log)
          except:
            pass
          return
        else:
          await interaction.response.send_message(embed=not_you, ephemeral=True)
  
      pr.callback = button_callback_ruins
      pb.callback = button_callback_base
      pd.callback = button_callback_desert


      

    @commands.command()
    @commands.guild_only()
    @cooldown(1, per_sec=30, type=commands.BucketType.user)
    async def open(self, ctx, crate=None):
      member_data = load_member_data(ctx.author.id)
      if crate != "crate":
        return
      if member_data.crate <= 0:
        error = discord.Embed(title="Error!", description=f"Commander, you don't have a {crate} to open", color=red)
        await ctx.reply(embed=error)
      else:
        async with ctx.typing():
          start = discord.Embed(description=f"[C-------- {crates}]", color=discord.Colour.random())
          message = await ctx.reply(embed=start)
          await asyncio.sleep(1.5)
          start2 = discord.Embed(description=f"[Co------- {sold}]", color=discord.Colour.random())
          await message.edit(embed=start2)
          await asyncio.sleep(1.5)
          start3 = discord.Embed(description=f"[Com------ {spy}]", color=discord.Colour.random())
          await message.edit(embed=start3)
          await asyncio.sleep(1.5)
          start4 = discord.Embed(description=f"[Comp----- {tank}]", color=discord.Colour.random())
          await message.edit(embed=start4)
          await asyncio.sleep(1.5)
          start5 = discord.Embed(description=f"[Compl---- {res}]", color=discord.Colour.random())
          await message.edit(embed=start5)
          await asyncio.sleep(1.5)
          start6 = discord.Embed(description=f"[Comple--- {strike}]", color=discord.Colour.random())
          await message.edit(embed=start6)
          await asyncio.sleep(1.5)
          start7 = discord.Embed(description=f"[Complet-- {wall}]", color=discord.Colour.random())
          await message.edit(embed=start7)
          await asyncio.sleep(1.5)
          start8 = discord.Embed(description=f"[Complete- {tank2}]", color=discord.Colour.random())
          await message.edit(embed=start8)
          await asyncio.sleep(1.5)
          start9 = discord.Embed(description=f"[Completed openning {crates}!]", color=green)
          await message.edit(embed=start9)
          await asyncio.sleep(1.5)

          option_s = random.randrange(100,175)
          rare_list = ["strike", "wall"]
          option_rare = random.choice(rare_list)
          option_rare2 = random.randrange(3,4)
          option_t = random.randrange(10,20)
          
          option_r = random.randrange(150,350)
          option_Spy = random.randrange(3,4)
          if option_rare == "strike":
            r_emoji = strike
            member_data.strikes += int(option_rare2)
            save_member_data(ctx.author.id, member_data)
          if option_rare == "wall":
            r_emoji = wall
            member_data.wall += int(option_rare2)
            save_member_data(ctx.author.id, member_data)

          
          fin = discord.Embed(description=f"Crate Contained:\n-\n{option_r} {res}\n{option_s} {sold}\n{option_t} {tank}\n{option_Spy} {spy}\n{option_rare2} {r_emoji}", color=inv)
          await message.edit(embed=fin)

          #result
          member_data.soldiers += int(option_s)
          member_data.tanks += int(option_t)
          member_data.spy += int(option_Spy)
          member_data.resources += int(option_r)
          member_data.crate -= 1


          
          save_member_data(ctx.author.id, member_data)

          default_log = discord.utils.get(self.client.get_all_channels(), id=1057356641911181373)

          try:
            log = discord.Embed(description=f"**{ctx.author.name}#{ctx.author.discriminator}** just openned a {crate}\n> Containing:\n{option_r} {res}\n{option_s} {sold}\n{option_t} {tank}\n{option_Spy} {spy}\n{option_rare2} {r_emoji}\n-\nFrom: {ctx.guild.name} server", color=inv)
            await default_log.send(embed=log)
          except:
            pass
        

    
      
#----Data

async def setup(client):
    await client.add_cog(income(client))   

def load_data():
        if os.path.isfile(data_filename):
            with open(data_filename, "rb") as file:
                return pickle.load(file)
        else:
            return dict()

def load_member_data(member_ID):
    data = load_data()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]

def save_member_data2(member_ID, member_data2):
    data = load_data2()

    data[member_ID] = member_data2

    with open(data_filename2, "wb") as file:
        pickle.dump(data, file)

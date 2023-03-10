import discord
from discord.ext import commands
from replit import db
import requests
import random
import json
import asyncio
import pickle
from keep_alive import keep_alive
import os
from discord.utils import find
import datetime
from datetime import datetime
from discord.ext import tasks
from googletrans import Translator
import traceback
import sys
import time
from emojis import suit, tank, tank2, sold, res, hearts, dead, comp, wall, strike, ca, scrap, spy, medal, crate, red, green, yellow, inv, loading2, ar, py
data_filename = "currency files/data"
data_filename2 = "levels/levels"
from discord import app_commands
from discord.ui import *
from PIL import Image, ImageFont, ImageDraw, ImageStat
import textwrap
from io import BytesIO
import numpy as np


gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
 
gscale2 = ' .:-=+*#%@'
 
def getAverageL(image: Image):
        im = np.array(image)
        w,h = im.shape
     
        return np.average(im.reshape(w*h))
     
def covertImageToAscii(IMAGE: Image, cols: int, scale: float, moreLevels: bool):
        global gscale1, gscale2
        image = IMAGE.convert('L')
        W, H = image.size
        w = W/cols
        h = w/scale
        rows = int(H/h)
         
        if cols > W or rows > H:
            return None
     
        aimg = []
        for j in range(rows):
            y1 = int(j*h)
            y2 = int((j+1)*h)
     
            if j == rows-1:
                y2 = H
     
            aimg.append("")
     
            for i in range(cols):
                x1 = int(i*w)
                x2 = int((i+1)*w)
                if i == cols-1:
                    x2 = W
                img = image.crop((x1, y1, x2, y2))          
                avg = int(getAverageL(img))
     
                if moreLevels:
                    gsval = gscale1[int((avg*69)/270)]
                else:
                    gsval = gscale2[int((avg*9)/270)]
    
                aimg[j] += gsval
        return aimg
    
def ascii_art(image: BytesIO, more_levels = False):
        scale = .65
        cols = 100
    
        image = Image.open(image)
    
        aimg = covertImageToAscii( image, cols, scale, more_levels )
       
        return aimg
    
def brightness_level(image: Image.Image):
        image = image.convert('L')
        stat = ImageStat.Stat(image)
        return stat.mean[0]
    
def create_welcome(user:discord.Member, user_avatar, join_pos):
        canvas = Image.new('RGB', (650, 250), (0,0,0,1))
    
        image_array = [canvas]

      

        

        

        

        # status = str(user.activity[:10]) + "\n" + str(user.activity)[10]

        text_color = 210, 43, 43 #108, 247, 80
        info_font = ImageFont.truetype("terminal.ttf", size=16)
        welcome_font = ImageFont.truetype("terminal.ttf", size=20)
        name_font = ImageFont.truetype("terminal.ttf", size=30)
        ascii_font = ImageFont.truetype("terminal.ttf", size=3)
        WELCOME_TEXT = "Identification Card"
        NAME_TEXT = user.name
        INFO_TEXT = [
          f"Subject Tag: #{user.discriminator}", 
          f"Subject ID: {user.id}", 
          f"Account Created: {user.created_at.strftime('%B %d, %Y')}", 
          f"Status: {user.status.name.upper()}", 
          f"Activity:"] + textwrap.wrap(user.activity.name if user.activity else "UNDETECTED", 25)
  
    
        for letter_range in range(len(WELCOME_TEXT)):
            im = image_array[-1].copy()
            draw = ImageDraw.Draw(im)
            draw.text((5+(welcome_font.size-5)*letter_range, 5), WELCOME_TEXT[letter_range], fill=text_color, font=welcome_font)
            image_array.append(im)
        
        # DELAY BEFORE WRITING THE NAME
        image_array += [image_array[-1] for _ in range(2)]
    
        for letter_range in range(len(NAME_TEXT)):
            im = image_array[-1].copy()
            draw = ImageDraw.Draw(im)
            draw.text((5+(name_font.size-10)*letter_range, 30), NAME_TEXT[letter_range], fill=text_color, font=name_font)
            image_array.append(im)
    
        # DELAY BEFORE WRITING THE INFO
        image_array += [image_array[-1] for _ in range(2)]
    
        for (index, line) in enumerate(INFO_TEXT):
            for letter_range in range(len(line)):
                im = image_array[-1].copy()
                draw = ImageDraw.Draw(im)
                draw.text((5+(info_font.size-5)*letter_range, 80+20*index), line[letter_range], fill=text_color, font=info_font)
                image_array.append(im)
    
        # DELAY BEFORE DRAWING THE IMAGE
        image_array += [image_array[-1] for _ in range(2)]
    
    
        brightness = brightness_level(Image.open(BytesIO(user_avatar)))
        ascii = ascii_art(BytesIO(user_avatar), more_levels=brightness>170)
    
        if not ascii: return
    
        ascii_len = len(ascii)*ascii_font.size
    
        ascii_image = Image.new('RGB', (ascii_len, ascii_len), (0,0,0))
        draw = ImageDraw.Draw(ascii_image)
    
        for (index, line) in enumerate(ascii):
            im = ascii_image.copy()
            draw = ImageDraw.Draw(im)
            # draw.text((L_MARGIN, T_MARGIN+ascii_font.size*index), line, fill=text_color, font=ascii_font)
            draw.text((0, ascii_font.size*index), line, fill=text_color, font=ascii_font)
            ascii_image = im
            im = image_array[-1].copy()
            im.paste(ascii_image.resize((275,275)), (380, 0))
    
            image_array.append(im)
    
        img = BytesIO()
        canvas.save(img, "GIF", save_all=True, append_images=image_array[1:], duration=50)
        img.seek(0)
    
        return img


def restart_bot():
    os.execv(sys.executable, ["python"] + sys.argv)

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

class staff(commands.Cog):
    def __init__(self, client):
        self.client = client
        #discord.Colour.random()

    # @commands.command()
    # @commands.is_owner()
    # async def announcement(self, ctx):
    #   default_log = discord.utils.get(self.client.get_all_channels(), id=1057356641911181373)
    #   await ctx.send("sending announcement to guilds")
    #   for guild in self.client.guilds:
    #     owner = guild.owner

    #     server_link = Button(label="Theta's Official Server", url="https://discord.gg/82Jf7uEqDs")
    #     view = View()
    #     view.add_item(server_link)
  
          
    #     ans = discord.Embed(title="Private Owner Message", description=f"I just realized i **DIDNT** add theta's invite link in the previous announcement :skull: , IM SO SORRY HERE U GO JUST CLICK THE BUTTON :sob:\n-\nStupid ham (Hamzy#0227)", color=red)
          
    #     try:
          
    #       await owner.send(embed=ans, view=view)
 
    #     except discord.Forbidden:
    #       error = discord.Embed(description=f"{owner.name}#{owner.discriminator} from {owner.guild.name} has dms turned off!")
    #       await ctx.reply(embed=error)

    @commands.command()
    @commands.is_owner()
    async def latest(self, ctx, status=None):
      if status != "status":
        did = discord.Embed(description="Did you mean `latest status` ?", color=inv)
        await ctx.reply(embed=did)
        return
      await self.client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.playing, name=f"with {len(self.client.guilds)} servers and {len(self.client.users)} members"))
      done = discord.Embed(description="Refreshed bot's appearance", color=inv)
      await ctx.reply(embed=done)

    
        
    
    
        

    
    

    @commands.command()
    @commands.is_owner()
    async def restart(self, ctx):
        restart = discord.Embed(description="Restarting, wait for a confirmation message", color=green)
        await ctx.message.add_reaction("???")
        await ctx.send(embed=restart, delete_after=8)
        restart_bot()

    

      
          
    @commands.command(aliases = ["Developer commands", "Developer Commands", "developer commands"])
    async def dc(self, ctx):
      with open("prefix.json", "r", encoding="utf-8") as fp:
        custom_prefixes = json.load(fp)
      prefix = custom_prefixes[f"{ctx.guild.id}"]
      og = discord.Embed(title="Bot's System", description="These are sets of commands that are only compatibale with bot owners regarding the bot", color=green)
      
      og.add_field(name=f"`{prefix}restart`", value="Restart full bot including Main.py file", inline=False)
      
      og.add_field(name=f"`{prefix}refresh`", value="Refresh all cog files to save updates done to them", inline=False)

      og.add_field(name=f"`{prefix}emoji`", value="Sends a full list of a double paged emoji string, id formatted and code formatted", inline=False)

      og.add_field(name=f"`{prefix}latest status`", value="Updates the bot's status/stats")




      
      og3 = discord.Embed(title="Currency Wise", description="These are sets of commands that are only compatibale with bot owners regarding the currency", color=green)
      
      og3.add_field(name=f"`{prefix}get`", value="Interactive command to give you any weaponized object inside the pickle file", inline=False)
      
      og3.add_field(name=f"`{prefix}give @member/id`", value="Interactive command to give the member any weaponized object inside the pickle file", inline=False)

      og3.add_field(name=f"`{prefix}reset @member/id`", value="Resets mentioned member's base", inline=False)
      
      og3.add_field(name=f"`{prefix}take @member/id`", value="Interactive command to take away any weaponized object inside the pickle file from the member", inline=False)
      
      

      

      
      lists = [og, og3]
      async with ctx.typing():
        await asyncio.sleep(1)
      message = await ctx.reply(embed=og)
      await message.add_reaction("???")
      await message.add_reaction("???")
      await message.add_reaction("???")
      await message.add_reaction("???")

      def check(reaction, user):
          return user == ctx.author

      i = 0
      reaction = None

      while True:
          if str(reaction) == "???":
              i = 0
              await message.edit(embed=lists[i])
          elif str(reaction) == "???":
              if i > 0:
                  i -= 1
                  await message.edit(embed=lists[i])
          elif str(reaction) == "???":
              if i < 1:
                  i += 1
                  await message.edit(embed=lists[i])
          elif str(reaction) == "???":
              i = 1
              await message.edit(embed=lists[i])

          try:
              reaction, user = await self.client.wait_for(
                "reaction_add", timeout=120.0, check=check
            )
              await message.remove_reaction(reaction, user)
          except:
              break
      await message.clear_reactions()

    # @commands.command()
    # @commands.is_owner()
    # async def board(self, ctx):
    #   list_of_theta_members=[]
      
    #   for guild in self.client.guilds:
    #     for member in guild.members:
    #       member_data = load_member_data(member.id)
    #       member_data2 = load_member_data2(member.id)

    #       if member_data2.xp >= 1:
    #         list_of_theta_members.append(f"**{member.name}#{member.discriminator}** {ar} level `{member_data2.level}`")
          
    #       else:
    #         pass
    #   final = list(set(list_of_theta_members))
      
      
      # test = discord.Embed(description=f"\n".join(final), color=inv)
      # await ctx.reply(embed=test)         


    @commands.hybrid_command(description="Shows you boards of players")
    async def leaderboard(self, ctx):
      moment = discord.Embed(description="Loading boards..", color=inv)
      moment_send = await ctx.reply(embed=moment)
      list_of_theta_members_levels = []
      list_of_theta_members_xp = []
      
      for guild in self.client.guilds:
        for member in guild.members:
          member_data = load_member_data(member.id)
          member_data2 = load_member_data2(member.id)

          if member_data2.level >= 1:
            list_of_theta_members_levels.append(f"**{member.name}#{member.discriminator}** {ar} level `{member_data2.level}`")

          if member_data2.xp >= 1:
            list_of_theta_members_xp.append(f"**{member.name}#{member.discriminator}** {ar} `{member_data2.xp}` xp in level `{member_data2.level}`")
          
          else:
            pass
      lvl = list(set(list_of_theta_members_levels))
      xp = list(set(list_of_theta_members_xp))
      conf1_embed = discord.Embed(description="Please a select a field in order to show its players!", color=inv)

      field_option = Select(placeholder="Select a field", options=[
        discord.SelectOption(label="Level Board", value="level"),
        discord.SelectOption(label="XP Board", value="xp"),
      ])

      view = View()
      view.add_item(field_option)

      conf2 = await moment_send.edit(embed=conf1_embed, view=view)

      async def options(interaction):
        if field_option.values[0] == "level":
          level_embed = discord.Embed(title="Board of levels", description="\n".join(lvl), color=inv)
          await interaction.response.send_message(embed=level_embed, ephemeral=False)
          await conf2.delete()
          

        elif field_option.values[0] == "xp":
          xp_embed = discord.Embed(title="Board of xp", description="\n".join(xp), color=inv)
          await interaction.response.send_message(embed=xp_embed, ephemeral=False)
          await conf2.delete()

      field_option.callback = options


    @app_commands.command(description = "DM command using theta!")
    @commands.is_owner()
    @commands.guild_only()
    async def dm(self, interaction: discord.Interaction, user_id : str, dm_message: str): 
      user = await self.client.fetch_user(user_id)

      try:

          embed = discord.Embed(description = f"**{dm_message}**", colour = red)
          embed.set_footer(text = f"Message sent to you by: Theta's Development Team | powered by Theta")
  
          await user.send(embed=embed)
          
          await interaction.response.send_message(f"DM successfully sent!", ephemeral=True)
      except discord.Forbidden:
          
          error = discord.Embed(description=f"Couldn't dm {user.name} :x:", color=inv)
          await interaction.response.send_message(embed=error)

     
  
    


    @commands.command(aliases = ["emojis"])
    async def emoji(self, ctx):
      if len(ctx.guild.emojis) <= 0:
        non = discord.Embed(description="No available emojis are active in this server", color=inv)
        await ctx.reply(embed=non)
      if len(ctx.guild.emojis) >= 1:
        
        
        emoji_string = '\n'.join(f"<{'a' if _.animated else ''}:{_.name}:{_.id}> {_.id}" for num, _ in enumerate(ctx.guild.emojis, start=1)) if len(ctx.guild.emojis) > 0 else "None"

        emoji_string2 = '\n'.join(f"<{'a' if _.animated else ''}:{_.name}:{_.id}> `<{'a' if _.animated else ''}:{_.name}:{_.id}>`" for num, _ in enumerate(ctx.guild.emojis, start=1)) if len(ctx.guild.emojis) > 0 else "None"

      
        
        embed1 = discord.Embed(title="Emojis",description=emoji_string, color=inv)
        embed2 = discord.Embed(title="Emojis",description=emoji_string2, color=inv)
        

        lists = [embed1, embed2]
        message = await ctx.reply(embed=embed1)
        await message.add_reaction("???")
        await message.add_reaction("???")
        

        def check(reaction, user):
            return user == ctx.author

        i = 0
        reaction = None

        while True:
          
            if str(reaction) == "???":
                if i > 0:
                    i -= 1
                    await message.edit(embed=lists[i])
            elif str(reaction) == "???":
                if i < 3:
                    i += 1
                    await message.edit(embed=lists[i])

            try:
                reaction, user = await self.client.wait_for(
                    "reaction_add", timeout=50.0, check=check
                )
                await message.remove_reaction(reaction, user)
            except:
                break

        await message.clear_reactions()

          


  
    @commands.command()
    @commands.is_owner()
    async def reset(self, ctx, member:discord.Member=None):
      if member == None:
        member = ctx.author
      member_data = load_member_data(member.id)
      member_data2 = load_member_data2(member.id)
      member_data.soldiers = 0
      member_data2.level = 0
      member_data2.xp = 0
      member_data.tanks = 0
      member_data.resources = 0
      member_data.spy = 0
      member_data.strikes = 0
      member_data.wall = 0
      member_data.ca = 0
      member_data.crate = 0
      member_data.scrap = 0
      member_data.medals = 0
      save_member_data(member.id, member_data)
      confirmation = discord.Embed(description=f"Successfully reseted `{member}'s` base :white_check_mark:", color=red)
      await ctx.reply(embed=confirmation)
      
      


      
    
    @commands.command()
    @commands.is_owner()
    async def get(self, ctx):
      member_data = load_member_data(ctx.author.id)
      first = discord.Embed(description=f"What shall I give you, general?\n-\nSoldiers {sold}\nTanks {tank}\nRobotic Spy :detective:\nResources {res}\nWall {wall}\nStrike {strike}\nCrate {crate}\nca {ca}", color=green)
      await ctx.reply(embed=first)
      msg1 = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id,)

      
      third = discord.Embed(description="What is the amount you are requesting?", color=green)
      await ctx.reply(embed=third)
      complete = discord.Embed(description="you have successfully been given what you requested. :white_check_mark:", color=green)
      
      amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id,)
      if msg1.content.lower() == "tanks" or msg1.content.lower() == "Tanks" or msg1.content.lower() =="tank" or msg1.content.lower() == "Tank":
        member_data.tanks += int(amount.content)
        await ctx.reply(embed=complete)
        save_member_data(ctx.author.id, member_data)  
        return
    
      elif msg1.content.lower() == "resources" or msg1.content.lower() == "Resources" or msg1.content.lower() == "Resource" or msg1.content.lower() == "resource":
        member_data.resources += int(amount.content)
        await ctx.reply(embed=complete)
        save_member_data(ctx.author.id, member_data)
        return
      elif msg1.content.lower() == "ca" or msg1.content.lower() == "Ca" or msg1.content.lower() == "Combat Aircraft" or msg1.content.lower() == "Combat aircraft":
        member_data.ca += int(amount.content)
        await ctx.reply(embed=complete)
        save_member_data(ctx.author.id, member_data)
        return
      elif msg1.content.lower() == "crate" or msg1.content.lower() == "Crate" or msg1.content.lower() == "Crates" or msg1.content.lower() == "crates":
        member_data.crate += int(amount.content)
        await ctx.reply(embed=complete)
        save_member_data(ctx.author.id, member_data)
        return
      elif msg1.content.lower() == "walls" or msg1.content.lower() == "wall" or msg1.content.lower() == "Walls" or msg1.content.lower() == "Wall":
        member_data.wall += int(amount.content)
        await ctx.reply(embed=complete)
        save_member_data(ctx.author.id, member_data)
        return
      elif msg1.content.lower() == "spy" or msg1.content.lower() == "Spy" or msg1.content.lower() == "spies" or msg1.content.lower() == "Spies":
        member_data.spy += int(amount.content)
        await ctx.reply(embed=complete)
        save_member_data(ctx.author.id, member_data)
        return  
      elif msg1.content.lower() == "soldiers" or msg1.content.lower() == "Soldier" or msg1.content.lower() == "soldier" or msg1.content.lower() == "Soldiers":
        member_data.soldiers += int(amount.content)
        await ctx.reply(embed=complete)
        save_member_data(ctx.author.id, member_data)
      elif msg1.content.lower() == "strike" or msg1.content.lower() == "Strike" or msg1.content.lower() == "strikes" or msg1.content.lower() == "Strikes":
        member_data.strikes += int(amount.content)
        await ctx.reply(embed=complete)
        save_member_data(ctx.author.id, member_data)
      else:
        error = discord.Embed(description="Sorry, couldn't identify the construction, **make sure there is no capital letters and try again!**", color=red)
        await ctx.reply(embed=error)
    

  
    @commands.command()
    @commands.is_owner()
    async def give(self, ctx, user_id):
      member = await self.client.fetch_user(user_id)
      member_data = load_member_data(member.id)
      first = discord.Embed(description=f"What shall I give this commander, general?\n-\nSoldiers {sold}\nTanks {tank}\nRobotic Spy :detective:\nResources {res}\nWall {wall}\nStrikes {strike}\nCrate {crate}", color=green)
      await ctx.reply(embed=first)
      msg1 = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id,)

      
      third = discord.Embed(description="What is the amount you request?", color=green)
      await ctx.reply(embed=third)
      
      amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id,)
      complete = discord.Embed(description="Commander recieved the demanded request. :white_check_mark:", color=green)
      if msg1.content.lower() == "tanks" or msg1.content.lower() == "Tanks" or msg1.content.lower() =="tank" or msg1.content.lower() == "Tank":
        member_data.tanks += int(amount.content)
        await ctx.reply(embed=complete)
        ss1 = discord.Embed(description=f"Commander, you were given {amount.content} {tank} from the system.", color=green)
        await member.send(embed=ss1)
        save_member_data(member.id, member_data)  
        return
    
      elif msg1.content.lower() == "resources" or msg1.content.lower() == "Resources" or msg1.content.lower() == "Resource" or msg1.content.lower() == "resource":
        member_data.resources += int(amount.content)
        await ctx.reply(embed=complete)
        ss2 = discord.Embed(description=f"Commander, you were given {amount.content} {res} from the system", color=green)
        await member.send(embed=ss2)
        save_member_data(member.id, member_data)
        return
      elif msg1.content.lower() == "walls" or msg1.content.lower() == "wall" or msg1.content.lower() == "Walls" or msg1.content.lower() == "Wall":
        member_data.wall += int(amount.content)
        await ctx.reply(embed=complete)
        ss3 = discord.Embed(description=f"Commander, you were given {amount.content} {wall} from the system.", color=green)
        await member.send(embed=ss3)
        save_member_data(member.id, member_data)
        return
      elif msg1.content.lower() == "crate" or msg1.content.lower() == "Crate" or msg1.content.lower() == "Crates" or msg1.content.lower() == "crates":
        member_data.crate += int(amount.content)
        await ctx.reply(embed=complete)
        ss3 = discord.Embed(description=f"Commander, you were given {amount.content} {crate} from the system.", color=green)
        await member.send(embed=ss3)
        save_member_data(member.id, member_data)
        return
      elif msg1.content.lower() == "spy" or msg1.content.lower() == "Spy" or msg1.content.lower() == "spies" or msg1.content.lower() == "Spies":
        member_data.spy += int(amount.content)
        await ctx.reply(embed=complete)
        ss4 = discord.Embed(description=f"Commander, you were given {amount.content} :detective: from the system.", color=green)
        await member.send(embed=ss4)
        save_member_data(member.id, member_data)
        return  
      elif msg1.content.lower() == "soldiers" or msg1.content.lower() == "Soldier" or msg1.content.lower() == "soldier" or msg1.content.lower() == "Soldiers":
        member_data.soldiers += int(amount.content)
        await ctx.reply(embed=complete)
        ss5 = discord.Embed(description=f"Commander, you were given {amount.content} {sold} from the system.", color=green)
        await member.send(embed=ss5)
        save_member_data(member.id, member_data)
      elif msg1.content.lower() == "strike" or msg1.content.lower() == "Strike" or msg1.content.lower() == "strikes" or msg1.content.lower() == "Strikes":
        member_data.strikes += int(amount.content)
        await ctx.reply(embed=complete)
        ss6 = discord.Embed(description=f"Commander, you were given {amount.content} {strike} from the system.", color=green)
        await member.send(embed=ss6)
        save_member_data(member.id, member_data)
      else:
        error = discord.Embed(description="Sorry, couldn't identify the construction, **make sure there is no capital letters and try again!**", color=red)
        await ctx.reply(embed=error)

  
    @commands.command()
    @commands.is_owner()
    async def take(self, ctx, member:discord.Member=None):
      if member == None:
        member = ctx.author
      member_data = load_member_data(member.id)
      
      first = discord.Embed(description=f"What shall take from this user, general?\n-\nSoldiers {sold}\nTanks {tank}\nRobotic Spy/Spy :detective:\nResources {res}\nWalls {wall}\nStrike {strike}\ncrate {crate}", color=red)
      await ctx.reply(embed=first)
      msg1 = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id,)

      
      third = discord.Embed(description="What is the amount you request?", color=yellow)
      await ctx.reply(embed=third)
      
      amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id,)
      complete = discord.Embed(description="Deletion successful. :white_check_mark:", color=red)
      if msg1.content.lower() == "tanks":
        member_data.tanks -= int(amount.content)
        await ctx.reply(embed=complete)
        ss1 = discord.Embed(description=f"Commander, you were subtracted {amount.content} {tank} by the system operators.", color=yellow)
        await member.send(embed=ss1)
        save_member_data(member.id, member_data)  
        return



      elif msg1.content.lower() == "crate":
        member_data.crate -= int(amount.content)
        await ctx.reply(embed=complete)
        ss2 = discord.Embed(description=f"Commander, you were subtracted {amount.content} {crate} by the system operators", color=yellow)
        await member.send(embed=ss2)
        save_member_data(member.id, member_data)
        return
    
      elif msg1.content.lower() == "resources":
        member_data.resources -= int(amount.content)
        await ctx.reply(embed=complete)
        ss2 = discord.Embed(description=f"Commander, you were subtracted {amount.content} {res} by the system operators", color=yellow)
        await member.send(embed=ss2)
        save_member_data(member.id, member_data)
        return
      elif msg1.content.lower() == "walls":
        member_data.wall -= int(amount.content)
        await ctx.reply(embed=complete)
        ss3 = discord.Embed(description=f"Commander, you were subtracted {amount.content} {wall} by the system operators.", color=yellow)
        await member.send(embed=ss3)
        save_member_data(member.id, member_data)
        return
      elif msg1.content.lower() == "spy":
        member_data.spy -= int(amount.content)
        await ctx.reply(embed=complete)
        ss4 = discord.Embed(description=f"Commander, you were subtracted {amount.content} :detective: by the system operators.", color=yellow)
        await member.send(embed=ss4)
        save_member_data(member.id, member_data)
        return  
      elif msg1.content.lower() == "soldiers":
        member_data.soldiers -= int(amount.content)
        await ctx.reply(embed=complete)
        ss5 = discord.Embed(description=f"Commander, you were subtracted {amount.content} {sold} by the system operators.", color=green)
        await member.send(embed=ss5)
        save_member_data(member.id, member_data)
      elif msg1.content.lower() == "strike":
        member_data.strikes -= int(amount.content)
        await ctx.reply(embed=complete)
        ss6 = discord.Embed(description=f"Commander, you were subtracted {amount.content} {strike} by the system operators.", color=green)
        await member.send(embed=ss6)
        save_member_data(member.id, member_data)
      else:
        error = discord.Embed(description="Sorry, couldn't identify the construction, **make sure there is no capital letters and try again!**", color=red)
        await ctx.reply(embed=error)
    


    
    @commands.command()
    async def invite(self, ctx):
      inv = discord.Embed(title="Theta's Invitation", description="Thank you for using theta and thank you for sharing it!\n-\n**Invite** is right [Here!](https://discord.com/api/oauth2/authorize?client_id=901389809283629067&permissions=8&scope=bot%20applications.commands) don't forget to join the [Official Theta Server](https://discord.gg/82Jf7uEqDs)", color=red)
      await ctx.reply(embed=inv)

  
    




























    # @app_commands.command(description="Identify yourself or a member with theta's format!")
    # async def identify(self, interaction:discord.Interaction, member:discord.Member=None):
    #   if member == None:
    #     member = interaction.user

    #   await interaction.response.defer(ephemeral=False)
    #   avatar = await member.display_avatar.read()
    
    #   welcome_image = await self.client.loop.run_in_executor(None, lambda: create_welcome(member, avatar, member.guild.member_count))

    #   await interaction.followup.send(file=discord.File(welcome_image, "identification.gif"), ephemeral=False)

    @commands.hybrid_command(description="Identify yourself or a member with theta's format!")
    async def identify(self, ctx, member:discord.Member=None):
      if member == None:
        member = ctx.author

      loads = discord.Embed(description=f"**Loading Identification Card** {loading2}", color=red)
      loads_e = await ctx.reply(embed=loads)
      avatar = await member.display_avatar.read()
    
      welcome_image = await self.client.loop.run_in_executor(None, lambda: create_welcome(member, avatar, member.guild.member_count))

      await loads_e.delete()

      await ctx.reply(file=discord.File(welcome_image, "identification.gif"), ephemeral=False)

    
      






      
async def setup(client):
    await client.add_cog(staff(client))



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
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0)

    return data[member_ID]

def save_member_data2(member_ID, member_data2):
    data = load_data2()

    data[member_ID] = member_data2

    with open(data_filename2, "wb") as file:
        pickle.dump(data, file)

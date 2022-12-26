import discord
from discord.ext import commands
import os
import pickle
import asyncio
import json
from emojis import tank, tank2, sold, res, hearts, dead, comp, arr, wall, strike, ca, scrap, spy, medal, crate, red, green, yellow, inv
from discord.ui import *

from discord import app_commands



air = "https://media.discordapp.net/attachments/814828851724943361/1038888979686244362/ezgif.com-gif-maker_4.gif"
spies = "https://media.discordapp.net/attachments/814828851724943361/1038885671697403984/ezgif.com-gif-maker_3.gif"
base = "https://media.discordapp.net/attachments/814828851724943361/1038878064521777212/ezgif.com-gif-maker.gif"
walls = "https://media.discordapp.net/attachments/814828851724943361/1038878256922906634/ezgif.com-gif-maker_1.gif"
tank3 = "https://media.discordapp.net/attachments/814828851724943361/1038881920978792499/ezgif.com-gif-maker_2.gif"
trade = "https://media.discordapp.net/attachments/814828851724943361/1038891016306049145/ezgif.com-gif-maker_5.gif"
war = "https://media.discordapp.net/attachments/814828851724943361/1038891231633215488/ezgif.com-gif-maker_6.gif"
sell = "https://media.discordapp.net/attachments/814828851724943361/1038892781181091961/ezgif.com-gif-maker_7.gif"

col = 0x89CFF0

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
        
        


class info(commands.Cog):
    def __init__(self, client): 
        self.client = client

    def cooldown(rate, per_sec=0, per_min=0, per_hour=0, type=commands.BucketType.default):
        return commands.cooldown(rate, per_sec + 60 * per_min + 3600 * per_hour, type)




    @commands.command(aliases = ["cmd", "command", "commands"])
    @commands.guild_only()
    async def help(self, ctx): 
      guild = ctx.guild
      with open("prefix.json", "r", encoding="utf-8") as fp:
        custom_prefixes = json.load(fp)
        prefix = custom_prefixes[f"{guild.id}"]
      intro = discord.Embed(title="**Theta’s Helping guide**",description=f"Welcome, Commander {ctx.author.name} to Theta’s Helping guide.\n-\nThis guide will explain Theta Bot, its basics, and the elements it contains.\n-\nNavigate the guide using the reactions below.", color=red)

      confirmation = discord.Embed(title="Important Note!", description="In the following embeds of the guide you will be observing alot of commands that require member mentioning, however you may use [ids](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-#:~:text=In%20the%20right%2Dclick%20menu,ID%20copied%20to%20your%20clipboard.) that are accessible from [Developer tools](https://www.youtube.com/watch?v=e_UoIwmS8Xk). Ids make it less suspicious and more secretive to accomplish your commands without disturbances to others.", color=yellow)

      

      #Page 1: Consits of introuction to Theta
      ham = self.client.get_user(798280308071596063)
      p1 = discord.Embed(description=f"**Theta**\nTheta is an interactive role play custom bot made by {ham}, it is a war simulation game that contains simple yet fun gameplay.\n-\nYour mission is to become the greatest commander out there, and Theta is here to assist you in completing this ambitious mission.", color = red) 


      
      #Page 2: Base
      p2 = discord.Embed(title="Your base, your root", description=f"> The base is the core of your adventure; everything you gain in the game will have an affect on your journey and your base, either positively or negatively. Your base contains  important sections;\n1) **Protection**\n2) **Army**\n3) **Specials**\n4) **Wealth**\n-\n> You may check your base using `/base`", color = red) 

      p2.set_image(url=base)

      
      #Page 3: Protection
      p3 = discord.Embed(title="Proection", description=f"> Protection comes first, and by that we mean shields and walls\n-\n> **Wall** {wall} is an obtainable item that may be constructed with `{prefix}construct`, and its sole purpose is to guard you from an approaching attack.\n-\n> **Stike** {strike} is an available construction that may be built with `{prefix}construct`, and its main purpose is to function as a sort of ticket to an attack, but they do not cause any harm to enemy's base or troops. __**You need a strike to perform an attack**__", color = red)

      p3.set_image(url=walls)
      
      
      #Page 4: Army 1
      p4 = discord.Embed(title="Army P1/2", description=f"> Army in Theta mainly focus on two great factors; **Soldiers {sold}** and **tanks {tank}**. A **soldier** is worth `1 hp` while a **tank** is worth `10 hp`.\n-\nYou can recruit **soldiers** using `{prefix}recruit` and you can construct a **tank** using `{prefix}construct`",color = red)

      p4.set_image(url=tank3)

      
      #Page 5: Army 2
      p5 = discord.Embed(title="Army P2/2", description = f"> **Spies {spy}** observe other commanders' bases primarily. They fully tell you of what the other commander have acquired in their base. You can construct a spy using `{prefix}construct`\n-\n> You may spy another commander using `{prefix}spy @member/id`", color = red)
      p5.set_image(url=spies)
      
      

      p6 = discord.Embed(title="Specials", description=f"> Special weapons and gadgets are available to make you more powerful.\n-\n> **Combat Aircraft {ca}**, combat aircraft is a very strong weapon that provides air strikes that deals a total of ` 1000 hp ` damage to enemy's base, they can be constructed using `{prefix}construct`.\n-\n> **Scrap {scrap}** are materials that are used to construct combat aircrafts. Scraps can be constructed using `{prefix}construct`.\n-\n> **Crates {crate}** are loot-like boxes that contain sets of goods, they can be crafted with war medals.\n-\n> **War medals {medal}** can be obtained after every successful war commanders initiate, they are also visible in your base.\n-\nTo use air strikes on a member, use `{prefix}strike @member/id`\nTo open a crate use `{prefix}open crate`", color=red)
      p6.set_image(url=air)

      
      

      p7 = discord.Embed(title="Wealth", description=f"> **Resources {res}** are the most important factor in this game, they are the 'currency' of the game, they can be obtained by `{prefix}expedition` and are used in constructions. You can gain resources by invading other commanders as well on completing quests", color = red)

      p8 = discord.Embed(title="Attacking", description=f"> To declare an **attack** and start war, use `{prefix}attack @member/id` and mention the commander you want to attack, but you have to play it smart and choose the right moment to strike a blow.", color=red)
      p8.set_image(url=war)

      

      p9= discord.Embed(title="Extra P1/2", description = f"> **Trading**\n-\nThis command allows you to trade a certain amount of item for another user's item. This can be used via `{prefix}trade @member/id (trader item amount) (trader item name) (user item amount) (user item name)`\n-\n> **Quests**\nQuests are weekly missions that all commanders can complete in order to gain a big amount of goodies, they last for a short time, but there rewards will benefit you for awhile, use `{prefix}view quests` to view all the quests available at that time, your progress and the rewards you get for completing each one of them.",  color = red)
      p9.set_image(url=trade)

      

      p92 = discord.Embed(title="Extra P2/2", description = f"> **Selling**\n-\nYou can sell items/weapons that you don't need anymore using `{prefix}sell (amount) (item name)` but you will only gain half it's original price", color = red)
      p92.set_image(url=sell)


      end = discord.Embed(title="You're ready to go!", description=f"> **That's it commander, that's the end of the guide. You now know the basics of the bot and the bot's purpose and vision and feel free to share Theta using `{prefix}invite`, good luck!**\n-\n> Oh and before i forget, here is a free crate if you do `{prefix}redeem starter` ;) -Ham", color=green)
      end.set_image(url="https://media.discordapp.net/attachments/814828851724943361/1038897468886237254/ezgif.com-gif-maker_8.gif")

      

      

      lists = [intro, confirmation, p2, p3, p4, p5, p6, p7, p8, p9, p92, end]
      async with ctx.typing():
        await asyncio.sleep(1)
      message = await ctx.reply(embed=intro)
      await message.add_reaction("⏮")
      await message.add_reaction("◀")
      await message.add_reaction("▶")
      await message.add_reaction("⏭")

      def check(reaction, user):
          return user == ctx.author

      i = 0
      reaction = None

      while True:
          if str(reaction) == "⏮":
              i = 0
              await message.edit(embed=lists[i])
          elif str(reaction) == "◀":
              if i > 0:
                  i -= 1
                  await message.edit(embed=lists[i])
          elif str(reaction) == "▶":
              if i < 11:
                  i += 1
                  await message.edit(embed=lists[i])
          elif str(reaction) == "⏭":
              i = 11
              await message.edit(embed=lists[i])

          try:
              reaction, user = await self.client.wait_for(
                "reaction_add", timeout=120.0, check=check
            )
              await message.remove_reaction(reaction, user)
          except:
              break
      await message.clear_reactions()

  


  
    @app_commands.command(description="Sends you your base!") 
    @commands.guild_only()
    async def base(self, int: discord.Interaction):
      member_data = load_member_data(int.user.id)
      member_data2 = load_member_data2(int.user.id)
      health1 = member_data.soldiers * 1
      health2 = member_data.soldiers * 1 + member_data.tanks * 10

      if member_data.strikes < 0:
        member_data.strikes = 0
      if member_data.resources < 0:
        member_data.resources = 0
      #----
      embeds = discord.Embed(title=f"{int.user.display_name}'s Base", color=0x36393F) #18191C #0x36393F
      
      embeds.add_field(name="Protection", value=f"{str(member_data.wall)} {wall}\n{member_data.strikes} {strike}", inline = True)
      embeds.add_field(name="War Medals", value=f"{member_data.medals} {medal}", inline=True)
      
      embeds.add_field(name="Army", value=f"{str(member_data.soldiers)} {sold}\n{str(member_data.tanks)} {tank}\n{str(member_data.spy)} :detective:", inline = False)
      
      embeds.add_field(name="Specials", value=f"{member_data.ca} {ca}\n{member_data.crate} {crate}\n{member_data.scrap} {scrap}", inline = False)
      embeds.add_field(name="Wealth", value=f"{str(member_data.resources)} {res}", inline = False)
      embeds.add_field(name="Total HP", value=f"{health2} {hearts}", inline = True)
      if member_data2.level <= 0:
        required = "5"
        embeds.set_footer(text = f"{int.user.name}'s level : {member_data2.level} | {member_data2.xp}/{required} xp to level up")
      if member_data2.level == 1:
        required = "10"
        embeds.set_footer(text = f"{int.user.name}'s level : {member_data2.level} | {member_data2.xp}/{required} xp to level up") 
        
      if member_data2.level == 2:
        required = "15"
        embeds.set_footer(text = f"{int.user.name}'s level : {member_data2.level} | {member_data2.xp}/{required} xp to level up") 
        
      



        
      embeds.set_thumbnail(url="https://media.discordapp.net/attachments/814828851724943361/995035645053513829/ezgif.com-gif-maker.jpg")
      
      
      await int.response.send_message(embed=embeds, ephemeral=True)
        

      
          






    @app_commands.command(description="Owner only beta command") 
    @commands.is_owner()
    @commands.guild_only()
    async def base_beta(self, int: discord.Interaction):
      member_data = load_member_data(int.user.id)
      member_data2 = load_member_data2(int.user.id)
      health1 = member_data.soldiers * 1
      health2 = member_data.soldiers * 1 + member_data.tanks * 10

      if member_data.strikes < 0:
        member_data.strikes = 0
      if member_data.resources < 0:
        member_data.resources = 0
      #----

      base_options = Select(min_values=1, max_values=6,placeholder="Choose factions to appear in your base!", options=[

        discord.SelectOption(label="Protection", value="protection"),
        discord.SelectOption(label="War Medals", value="wm"),
        discord.SelectOption(label="Army", value="army"),
        discord.SelectOption(label="Specials", value="specials"),
        discord.SelectOption(label="Wealth", value="wealth"),
        discord.SelectOption(label="Total HP", value="hp"),
        
      ])

      bo = View(timeout=None)
      bo.add_item(base_options)

      embeds = discord.Embed(title=f"{int.user.display_name}'s Base", color=inv)
      if member_data2.level <= 0:
        required = "5"
        embeds.set_footer(text = f"{int.user.name}'s level : {member_data2.level} | {member_data2.xp}/{required}' to level up")
      if member_data2.level == 1:
        required = "10"
        embeds.set_footer(text = f"{int.user.name}'s level : {member_data2.level} | {member_data2.xp}/{required}' to level up") 
        
      if member_data2.level == 2:
        required = "15"
        embeds.set_footer(text = f"{int.user.name}'s level : {member_data2.level} | {member_data2.xp}/{required}' to level up")




      embeds.set_thumbnail(url="https://media.discordapp.net/attachments/814828851724943361/995035645053513829/ezgif.com-gif-maker.jpg")

      confirmation = await int.response.send_message(embed = embeds, view=bo, ephemeral=True)

      async def options(int):
          if base_options.values[0] == "protection":
            await int.response.edit_message(embed=embeds, view=bo)
            embeds.add_field(name="Protection", value=f"{str(member_data.wall)} {wall}\n{member_data.strikes} {strike}", inline = True)
            
          elif base_options.values[0] == "wm":
            embeds.add_field(name="War Medals", value=f"{member_data.medals} {medal}", inline=True)
            
          elif base_options.values[0] == "army":
            embeds.add_field(name="Army", value=f"{str(member_data.soldiers)} {sold}\n{str(member_data.tanks)} {tank}\n{str(member_data.spy)} :detective:", inline = False)
            
          elif base_options.values[0] == "specials":
            embeds.add_field(name="Specials", value=f"{member_data.ca} {ca}\n{member_data.crate} {crate}\n{member_data.scrap} {scrap}", inline = False)
            
          elif base_options.values[0] == "wealth":
            embeds.add_field(name="Wealth", value=f"{str(member_data.resources)} {res}", inline = False)
            
          elif base_options.values[0] == "hp":
            embeds.add_field(name="Total HP", value=f"{health2} {hearts}", inline = True)


        
      base_options.callback = options


      





















      
         
        

          
     


async def setup(client):
    await client.add_cog(info(client))   

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




#--------------------------------


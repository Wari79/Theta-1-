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
from emojis import tank, tank2, sold, res, hearts, dead, comp, arr, wall, strike, ca, scrap, spy, medal, crate, red, green, yellow



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
        

class quest(commands.Cog):
    def __init__(self, client): 
        self.client = client



  
    @commands.command()
    @commands.is_owner()
    async def add_q2(self, ctx, amount, member:discord.Member=None):
      if member == None:
        member = ctx.author
      member_data = load_member_data(member.id)
      
      member_data.s += int(amount)
      save_member_data(member.id, member_data)
      sub = discord.Embed(description=f"Successfully added {amount} progress to {member.name}", color=green)
      sat = discord.Embed(description="Sorry for the inconvenience however due to data loss, you were given an aid to your on going `Quest 2`", color=red)
      await ctx.send(embed=sub)
      await member.send(embed=sat)

  
    @commands.command()
    @commands.is_owner()
    async def add_q3(self, ctx, amount, member:discord.Member=None):
      if member == None:
        member = ctx.author
      member_data = load_member_data(member.id)
      
      member_data.r += int(amount)
      save_member_data(member.id, member_data)
      sub = discord.Embed(description=f"Successfully added {amount} progress to {member.name}", color=green)
      sat = discord.Embed(description="Sorry for the inconvenience however due to data loss, you were given an aid to your on going `Quest 2`", color=red)
      await ctx.send(embed=sub)
      await member.send(embed=sat)


  
    @commands.command()
    @commands.is_owner()
    async def subtract_q3(self, ctx, amount, member:discord.Member=None):
      if member == None:
        member = ctx.author
      member_data = load_member_data(member.id)
      member_data.r -= int(amount)
      save_member_data(member.id, member_data)
      sub = discord.Embed(description=f"Successfully subtracted {amount} from {member.name}", color=red)
      await ctx.send(embed=sub)
      ss1 = discord.Embed(description=f"Commander, you were subtracted {amount} points in your on-going ` Quest 3 ` by the system operators.", color=yellow)
      await member.send(embed=ss1)

  
    @commands.command()
    @commands.is_owner()
    async def subtract_q2(self, ctx, amount, member:discord.Member=None):
      if member == None:
        member = ctx.author
      member_data = load_member_data(member.id)
      member_data.s -= int(amount)
      save_member_data(member.id, member_data)
      sub = discord.Embed(description=f"Successfully subtracted {amount} from {member.name}", color=red)
      await ctx.send(embed=sub)
      ss1 = discord.Embed(description=f"Commander, you were subtracted {amount} points in your on-going ` Quest 2 ` by the system operators.", color=yellow)
      await member.send(embed=ss1)


      

  






  
    @commands.Cog.listener()
    async def on_message(self, message):
      member_data = load_member_data(message.author.id)
      member_data2 = load_member_data2(message.author.id)
      
      
      if member_data2.xp >= 5 and member_data2.level <= 0:
        member_data2.level += 1
        member_data2.xp = 0
        member_data.resources += 250
        save_member_data2(message.author.id, member_data2)
        save_member_data(message.author.id, member_data)
              
        lvl = discord.Embed(title="Level Up!", description=f"you just levelled up!, you're now level `{member_data2.level}`\n-\n**Rewards:**\n> 250 {res}", color=green)
        await message.channel.send(f"{message.author.mention}", embed=lvl)
        return
      else:
        pass
        
      if member_data2.xp >= 10 and member_data2.level <= 1:
        member_data2.level += 1
        member_data2.xp = 0
        save_member_data2(message.author.id, member_data2)
        lvl = discord.Embed(title="Level Up!", description=f"you just levelled up!, you're now level `{member_data2.level}`", color=green)
        await message.channel.send(f"{message.author.mention}", embed=lvl)
        return
      else:
        pass

      if member_data2.xp >= 15 and member_data2.level <= 2:
        member_data2.level += 1
        member_data2.xp = 0
        member_data.wall += 1
        member_data.resources += 250
        save_member_data2(message.author.id, member_data2)
        lvl = discord.Embed(title="Level Up!", description=f"you just levelled up!, you're now level `{member_data2.level}`\n-\n**Rewards:**\n> 250 {res}\n> 1 {wall}", color=green)
        await message.channel.send(f"{message.author.mention}", embed=lvl)
        return
      else:
        pass

      if member_data2.xp >= 25 and member_data2.level <= 3:
        member_data2.level += 1
        member_data2.xp = 0
        member_data.wall += 2
        member_data.crate += 1
        member_data.resources += 350
        save_member_data2(message.author.id, member_data2)
        lvl = discord.Embed(title="Level Up!", description=f"you just levelled up!, you're now level `{member_data2.level}`\n-\n**Rewards:**\n> 350 {res}\n> 2 {wall}\n> 1 {crate}", color=green)
        await message.channel.send(f"{message.author.mention}", embed=lvl)
        return
      else:
        pass


      if member_data2.xp >= 35 and member_data2.level <= 4:
        member_data2.level += 1
        member_data2.xp = 0
        member_data.wall += 3
        member_data.crate += 1
        member_data.resources += 450
        member_data.strikes += 2
        save_member_data2(message.author.id, member_data2)
        lvl = discord.Embed(title="Level Up!", description=f"you just levelled up!, you're now level `{member_data2.level}`\n-\n**Rewards:**\n> 450 {res}\n> 3 {wall}\n> 1 {crate}\n> 2 {strike}", color=green)
        await message.channel.send(f"{message.author.mention}", embed=lvl)
        return
      else:
        pass

      if member_data2.xp >= 45 and member_data2.level <= 5:
        member_data2.level += 1
        member_data2.xp = 0
        member_data.wall += 3
        member_data.crate += 2
        member_data.resources += 550
        member_data.strikes += 2
        save_member_data2(message.author.id, member_data2)
        lvl = discord.Embed(title="Level Up!", description=f"you just levelled up!, you're now level `{member_data2.level}`\n-\n**Rewards:**\n> 550 {res}\n> 3 {wall}\n> 2 {crate}\n> 2 {strike}", color=green)
        await message.channel.send(f"{message.author.mention}", embed=lvl)
        return
      else:
        pass

      if member_data2.xp >= 55 and member_data2.level <= 6:
        member_data2.level += 1
        member_data2.xp = 0
        member_data.wall += 1
        member_data.spy += 3 
        member_data.resources += 600
        member_data.strikes += 3
        member_data.crate += 2
        save_member_data2(message.author.id, member_data2)
        lvl = discord.Embed(title="Level Up!", description=f"you just levelled up!, you're now level `{member_data2.level}`\n-\n**Rewards:**\n> 600 {res}\n> 1 {wall}\n> 2 {crate}\n> 3 {strike}\n> 1 {spy}", color=green)
        await message.channel.send(f"{message.author.mention}", embed=lvl)
        return
      else:
        pass
      































        
      
      if member_data.mesg >= 1:
        with open("Quests/(A)redeem.json") as json_file:
              data = json.load(json_file)
        try:
            if data["members"][str(message.author.id)]:
              pass
        except KeyError:
            imports = {
            "member": message.author.id, 
            "name": message.author.name,
            "checkability": "Redeemed"
            }
            data["members"][message.author.id] = imports
            with open("Quests/(A)redeem.json", "w") as j:
              json.dump(data, j, indent=4)
            save_member_data(message.author.id, member_data)
            
      else:
        pass
      member_data = load_member_data(message.author.id)
      
      if member_data.s >= 150:
        with open("Quests/(B)quest.json") as json_file:
              data = json.load(json_file)
        try:
            if data["members"][str(message.author.id)]:
              pass
        except KeyError:
            imports = {
            "member": message.author.id, 
            "name": message.author.name,
            "checkability": "Completed"
            }
            data["members"][message.author.id] = imports
            with open("Quests/(B)quest.json", "w") as j:
              json.dump(data, j, indent=4)
            member_data.strikes += 2
            save_member_data(message.author.id, member_data)
            reward2 = discord.Embed(description=f"**Quest Completed**\n-\n> You recieved 2 {strike} for completing a quest.", color=green)
            await message.channel.send(f"{message.author.mention}", embed=reward2)
      else:
        pass

      if member_data.r >= 150:
        with open("Quests/(C)quest.json") as json_file:
              data = json.load(json_file)
        try:
            if data["members"][str(message.author.id)]:
              pass
        except KeyError:
            imports = {
            "member": message.author.id, 
            "name": message.author.name,
            "checkability": "Completed"
            }
            data["members"][message.author.id] = imports
            with open("Quests/(C)quest.json", "w") as j:
              json.dump(data, j, indent=4)
            member_data.strikes += 2
            member_data.wall += 2
            save_member_data(message.author.id, member_data)
            reward3 = discord.Embed(description=f"**Quest Completed**\n-\n> You recieved 2 {wall} & 2 {strike} for completing a quest.", color=green)
            await message.channel.send(f"{message.author.mention}", embed=reward3)
      else:
        pass
      if member_data.cfca >= 3:
        with open("Quests/(D)quest.json") as json_file:
              data = json.load(json_file)
        try:
            if data["members"][str(message.author.id)]:
              pass
        except KeyError:
            imports = {
            "member": message.author.id, 
            "name": message.author.name,
            "checkability": "Completed"
            }
            data["members"][message.author.id] = imports
            with open("Quests/(D)quest.json", "w") as j:
              json.dump(data, j, indent=4)
            
            member_data.resources += 1750
            save_member_data(message.author.id, member_data)
            reward2 = discord.Embed(description=f"**Quest Completed**\n-\n> You recieved 1750 {res} for completing a quest.", color=green)
            await message.channel.send(f"{message.author.mention}", embed=reward2)

      

    @commands.command()
    @commands.guild_only()
    async def redeem(self, ctx, starter=None):
      if starter != "starter":
        await ctx.reply("Perhaps you meant, `redeem starter` ?")
        return
      member_data = load_member_data(ctx.author.id)
      if member_data.mesg < 1:
        member_data.crate += 1
        member_data.mesg += 1
        suc = discord.Embed(title="Succesful Redemuption", description=f"You recieved 1 {crate} for redeeming the `starter pack`", color=green)
        await ctx.reply(embed=suc)
        save_member_data(ctx.author.id, member_data)
      else:
        error = discord.Embed(title="Already Redeemed", description="You already redeemed `Starter Pack`", color=red)
        await ctx.reply(embed=error)

  
    @commands.command()
    @commands.guild_only()
    async def view(self, ctx, quests=None):
      if quests != "quests":
        return
      member_data = load_member_data(ctx.author.id)
      

      if member_data.s >= 150:
        member_data.s = comp

      if member_data.r >= 150:
        member_data.r = comp

      if member_data.cfca >= 3:
        member_data.cfca = comp

      


      progress1 = discord.Embed(title="Quests", description=f"> **Recruit soldiers 150 times**\n{arr} {member_data.s}/150\n__Reward: 2 {strike}__\n-\n> **Gain resources 150 times**\n{arr} {member_data.r}/150\n__Reward: 2 {strike} & 2 {wall}__\n-\n> **Strike 3 commanders using the special Combat Airstrike**\n{arr} {member_data.cfca}/3\n__Reward: 1750 {res}__", color=green)
      await ctx.reply(embed=progress1)
      return


      if member_data.mesg >= 150 and member_data.s >= 150 and member_data.r >= 150 and member_data.cfca >= 3:
        completed = discord.Embed(title="Quests", description=f"> **All Quests completed {comp}**", color=green)
        await ctx.reply(embed=completed)
        return
      
      

      
      
async def setup(client):
    await client.add_cog(quest(client))  


  

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

#--------------------------------------------------------


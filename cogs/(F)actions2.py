import discord
from discord.ext import commands
import os
import pickle
import asyncio
import random
from emojis import tank, tank2, sold, res, hearts, dead, comp, arr, wall, strike, ca, scrap, spy, medal, crate, green, red, yellow



ins = "https://media.discordapp.net/attachments/814828851724943361/1038503971532324984/army-troops_2.gif"
inta = "https://media.discordapp.net/attachments/814828851724943361/1038503994751983707/tanks.gif"
inw = "https://media.discordapp.net/attachments/814828851724943361/1038503916230414428/wall.gif"



data_filename = "currency files/data"

class Data:
      def __init__(self, resources, soldiers, tanks, spy, wall, strikes, s, r, scrap, crate, ca, medals, cfc, cfca, mesg):
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



class actions2(commands.Cog):
    def __init__(self, client):
        self.client = client

    def cooldown(rate, per_sec=0, per_min=0, per_hour=0, type=commands.BucketType.default):
        return commands.cooldown(rate, per_sec + 60 * per_min + 3600 * per_hour, type)


    @commands.command()
    @commands.guild_only()
    async def strike(self, ctx, member:discord.Member):
      member_data = load_member_data(ctx.author.id)
      
      victim_data = load_member_data(member.id)
      
      if member_data.ca <= 0:
        error = discord.Embed(title="Insufficient Amount", description=f"Commander, you don't have any available {ca} to launch a Combat Aircraft", color=yellow)
        await ctx.reply(embed=error)

        
      else:
        check1 = discord.Embed(title="Warning",description=f"**Commander {ctx.author.name},**\n-\nAir strikes deal a total of `1000` HP damage to the mentioned comander's base. It will destroy several walls, soldiers, and tanks that user might have. Are you sure you want to proceed this action on {member.mention}", color=yellow)
        
        checkc = await ctx.send(embed=check1) 
        
        await checkc.add_reaction("✅")
        await checkc.add_reaction("❌")
        def check(reaction, user):
          return user == ctx.author

        reaction = None
        while True:  
          if str(reaction) == "✅":
            await checkc.clear_reactions()
            if victim_data.wall >= 5:
              async with ctx.typing():
                dw = random.randrange(3,5)
                destroying_walls = discord.Embed(description="Air Striking walls..", color=yellow)
                destroying_walls.set_image(url=inw)
                await checkc.edit(embed=destroying_walls)
                victim_data.wall -= int(dw)
                await asyncio.sleep(5)
                
                save_member_data(ctx.author.id, member_data)
                save_member_data(member.id, victim_data)
            if victim_data.wall < 5:
              async with ctx.typing():
                    
                destroying_walls = discord.Embed(description="Air Striking walls..", color=yellow)
                destroying_walls.set_image(url=inw)
                war = await checkc.edit(embed=destroying_walls)
                victim_data.wall = 0
                await asyncio.sleep(5) 
                
                save_member_data(ctx.author.id, member_data)
                save_member_data(member.id, victim_data)
                
            if victim_data.tanks >= 45:
                  
              dw2 = random.randrange(15,40)
              destroying_tanks = discord.Embed(description="Air Striking tanks..", color=yellow)
              destroying_tanks.set_image(url=inta)
              await checkc.edit(embed=destroying_tanks)
              victim_data.tanks -= int(dw2)
              await asyncio.sleep(5)
              
              save_member_data(member.id, victim_data)

            if victim_data.tanks < 45:
              destroying_tanks = discord.Embed(description="Air Striking tanks..", color=yellow)
              destroying_tanks.set_image(url=inta)
              await checkc.edit(embed=destroying_tanks)
              victim_data.tanks = 0
              await asyncio.sleep(5)
              
              save_member_data(member.id, victim_data)
                  
            if victim_data.soldiers >= 500:
              dw3 = random.randrange(250,500)
              destroying_soldiers = discord.Embed(description="Air Striking soldiers..", color=yellow)
              destroying_soldiers.set_image(url=ins)
              await checkc.edit(embed=destroying_soldiers)
              victim_data.soldiers -= int(dw3)
              await asyncio.sleep(5)
              
              save_member_data(member.id, victim_data)

                    
            if victim_data.soldiers < 500:
              destroying_soldiers = discord.Embed(description="Air Striking soldiers..", color=yellow)
              destroying_soldiers.set_image(url=ins)
              await checkc.edit(embed=destroying_soldiers)
              victim_data.soldiers = 0
              
              save_member_data(member.id, victim_data)
              await asyncio.sleep(5)




            finish = discord.Embed(title="Air Striked!", description=f"Killed soldiers and made them {victim_data.soldiers} {sold} left\n-\nDestroyed tanks while {victim_data.tanks} {tank} remained\n-\nAfter crushing all the walls, {victim_data.wall} {wall} were left", color=green)
            await checkc.edit(embed=finish)
            member_data.ca -= 1
            save_member_data(ctx.author.id, member_data)

            emergency = discord.Embed(title="Emergency", description=f"Commander! you have been air striked!, you now have:\n-\n{victim_data.soldiers} {sold}\n{victim_data.tanks} {tank}\n{victim_data.wall} {wall}", color=red)
            await member.send(embed=emergency)



            if member_data.cfca >= 3:
              pass
            if member_data.cfca < 3:
              
              member_data.cfca += 1
              save_member_data(ctx.author.id, member_data)
            
          
          elif str(reaction) == "❌":
            await checkc.clear_reactions()
            cancelled = discord.Embed(description="Cancelled air strikes operation.", color=green)
            await checkc.edit(embed=cancelled)
            
            ctx.command.reset_cooldown(ctx)
            return

          try:
             reaction, user = await self.client.wait_for("reaction_add", timeout=35.0, check=check)
             await checkc.remove_reaction(reaction, user)
             ctx.command.reset_cooldown(ctx)
          except:
            break
          
async def setup(client):
    await client.add_cog(actions2(client))   

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



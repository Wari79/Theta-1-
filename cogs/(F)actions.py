import discord
from discord.ext import commands
import os
import pickle
import asyncio
from emojis import tank, tank2, sold, res, hearts, dead, comp, arr, wall, strike, ca, scrap, spy, medal, crate, red, green, yellow
import json
from discord.ui import *




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



class actions(commands.Cog):
    def __init__(self, client):
        self.client = client

    def cooldown(rate, per_sec=0, per_min=0, per_hour=0, type=commands.BucketType.default):
        return commands.cooldown(rate, per_sec + 60 * per_min + 3600 * per_hour, type)


    @commands.command()
    @commands.guild_only()
    async def attack(self, ctx, victim:discord.Member): 
      if victim == ctx.author:
        async with ctx.typing():
          await asyncio.sleep(2)
        error1 = discord.Embed(description="Apologies!! we cannot initiate the raid on the same base, mention seomone's base instead!", color=0xFF0000)
        await ctx.reply(embed=error1)
        ctx.command.reset_cooldown(ctx)
        return
      else:
        if not victim.bot:
          member_data = load_member_data(ctx.author.id)
          member_data2 = load_member_data(victim.id)
          if member_data.strikes <= 0:
            insuf = discord.Embed(title="Error!", description=f"You need at least 1 {strike} to launch an attack!", color=0xFFD700)
            await ctx.reply(embed=insuf)
            ctx.command.reset_cooldown(ctx)
            return
          else:

            if member_data2.soldiers <= 150 and member_data2.tanks <= 0:
              error2 = discord.Embed(description="Cannot initiate an attack on a base including less than `150` HP", color=0xFF0000)
              await ctx.reply(embed=error2)
              ctx.command.reset_cooldown(ctx)
              return
            else:   
              if member_data2.wall > 0:
                striked = discord.Embed(description=f"Commander **{ctx.author.name}** striked **{victim.name}** with 1 {strike} on their wall.", color=yellow)
                
                await ctx.reply(embed=striked)

                informer = discord.Embed(title="Emergency!", description=f"Commander **{ctx.author.name}**, Just striked your base with a strike. You now have {member_data2.wall} {wall} left", color=red)
                await victim.send(embed=informer)
                ctx.command.reset_cooldown(ctx)
                #results
                member_data.strikes -= 1
                member_data2.wall -= 1
                save_member_data(ctx.author.id, member_data)
                save_member_data(victim.id, member_data2)
              else:  

                confirm_it = discord.Embed(title="Warning", description=f"Continuing this command will subtract 1 {strike} from your base, are you sure you will continue?", color=yellow)
                firm = await ctx.reply(embed=confirm_it)

                await firm.add_reaction("✅")
                await firm.add_reaction("❌")

                def check(reaction, user):
                  return user == ctx.author

                reaction = None
                while True:  
                  if str(reaction) == "✅":
                    await firm.clear_reactions()
                    confirmed = discord.Embed(description="Confirmed, proceeding with attack command..", color=green)
                    await firm.edit(embed=confirmed, delete_after=10.0)
                    initiation = discord.Embed(description="__**Initiating the attack sequence**__", color=0x567d46)
                    initiation1 = await ctx.reply(embed=initiation)
                    async with ctx.typing():
                      await asyncio.sleep(3)
                    initiate = discord.Embed(description=f"**How many soldiers are you attacking with?** (You currently have {member_data.soldiers} {sold})", color=0x567d46)  

                    await initiation1.edit(embed=initiate)
                    soldiers = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id,)

  
                    if member_data.soldiers >= int(soldiers.content):  
                      war1 = discord.Embed(description=f"**Going with {soldiers.content} soldiers. How many tanks you attacking with?** (You currently have {member_data.tanks} {tank})", color=0x567d46)  

                      await ctx.send(embed=war1)
    
                      tanks = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id,)
    
    
                      if member_data.tanks >= int(tanks.content):
                          war2 = discord.Embed(description=f"**Going with {tanks.content} tanks.**", color=0x567d46)

                          await ctx.send(embed=war2)


                
              
            
        
                          powert1 = int(tanks.content) * 10
                          powert2 = member_data2.tanks * 10

                
                          hp1r = int(soldiers.content) + powert1
                          hp2r = member_data2.soldiers + powert2
                          hp1t = int(tanks.content) - member_data2.tanks
                          hp2t = member_data2.tanks - int(tanks.content)

                          ground3 = discord.Embed(description=f"**__Commander {ctx.author.name}'s Offence__**\n{soldiers.content} {sold}\n{tanks.content} {tank}\n{hearts} : `{hp1r}`\n**__Commander {victim.name}'s Defence__**\n{member_data2.soldiers} {sold}\n{member_data2.tanks} {tank}\n{hearts} : `{hp2r}`", color=0xfbc28d)
                          await ctx.send(embed=ground3)

                          ground4 = discord.Embed(description="Not too late to leave with your troops commander, are you sure you want it bloody?", color=0xfbc28d)
                          war = await ctx.send(embed=ground4) 
              
            
                          await war.add_reaction("⚔️")
                          await war.add_reaction("❌")

                          def check(reaction, user):
                            return user == ctx.author

                          reaction = None
                          while True:  
                            if str(reaction) == "⚔️":
                              await war.clear_reactions()
                      
                              #definers    
                              hp1 = int(soldiers.content) - member_data2.soldiers 
                              hp2 = member_data2.soldiers - int(soldiers.content)
                              health1 = hp1 + powert1 - powert2
                              health2 = hp2 + powert2 - powert1

                              async with ctx.typing():
                                anas = discord.Embed(description="Analyzing Attack Results", color=0xfbc28d)
                        
                                anal = await ctx.send(embed=anas)
                                anas2 = discord.Embed(description="⚔️ Analyzing Attack Results ⚔️", color=0xfbc28d)
                                await asyncio.sleep(2)
                                await anal.edit(embed=anas2)
                                anas3 = discord.Embed(description=":shield: ⚔️ Gathering Intel ⚔️ :shield:", color=0xfbc28d)
                                await asyncio.sleep(2)
                                await anal.edit(embed=anas3)
                                anas4 = discord.Embed(description="⚔️ :shield: ⚔️ Collecting *Dead* Bodies ⚔️ :shield: ⚔️", color=0xfbc28d)
                                await asyncio.sleep(2)
                                await anal.edit(embed=anas4)
                                anas5 = discord.Embed(description="⚔️ :shield: ⚔️ Collecting *Dead* Bodies ⚔️ :shield: ⚔️", color=0xfbc28d)
                                await asyncio.sleep(2)
                                await anal.edit(embed=anas5)
                                anas6 = discord.Embed(description="⚔️ :shield: ⚔️ Finalizing Calculations ⚔️ :shield: ⚔️", color=0xfbc28d)
                                await asyncio.sleep(2)
                                await anal.edit(embed=anas6)
                                await asyncio.sleep(2)

                              if hp1r > hp2r:

                                if hp1t < hp2t:
                                  hp1t = 0
                            
                                  hpa = hp1 - hp2t * 10
                                  half2 = member_data2.resources - hp1 * 2 
                                  result = hp2t * 10 + member_data2.soldiers
                                  half3 = hp1 * 2 + hp1t * 6
                            
                                  win = discord.Embed(description=f"**__Commander {ctx.author.name}'s Offence__**\n{hpa} {sold}\n{dead} {tank}\n{hearts} : `{health1}`\n**__Commander {victim.name}'s Defence__**\n{dead} {sold}\n{dead} {tank}\n{hearts} : `0`", color=0xfbc28d)
                            
                                  await ctx.send(embed=win)
                            
                                  winner1 = discord.Embed(title="Attack Completed Successfully", description=F"**Commander {ctx.author.name}** wins the battle with {hpa} {sold} left!", color=0x567d46)
                            
                                  if half2 <= 0:
                                    winner1.add_field(name="__Rewards:__", value=f"{member_data2.resources} {res}")
                                    
                                    await ctx.send(embed=winner1)
                                    member_data.resources += member_data2.resources
                                    member_data.strikes -= 1
                                    member_data2.soldiers = 0 
                                    member_data.soldiers -= int(result)
                                    member_data.tanks -= int(tanks.content)
                                    member_data2.tanks = 0
                                    member_data2.resources = 0
                                    member_data.medals += 1
                                    
                                    save_member_data(ctx.author.id, member_data)
                                    save_member_data(victim.id, member_data2)
                                    
                                    await victim.send(embed=emergency3)
                                  
                                  
                                    return
                                  else:
                                    member_data2.resources -= int(round(half3))
                                    member_data.soldiers -= int(result)
                                    member_data.tanks -= int(tanks.content)
                                    member_data2.soldiers = 0 
                                    member_data2.tanks = 0
                                    member_data.resources += int(round(half3))
                                    member_data.strikes -= 1
                                    member_data.medals += 1
                                    
                                    save_member_data(ctx.author.id, member_data)
                                    save_member_data(victim.id, member_data2)
                              

                                    winner1.add_field(name="__Rewards:__", value=f"{round(half2)} {res}")
                                    
                                    await ctx.send(embed=winner1)
                                    emergency3 = discord.Embed(description=f"**Emergency**\n-\nYou have been attacked by commander `{ctx.author.name} ({ctx.author.id})`\n-\nYour defences lost, and your troops are dead", color=red)
                                    await victim.send(embed=emergency3)
                                    return





                                if hp1 < hp2:
                                  hp1 = 0
                            
                                  hpa_f = hp2 / 10 # 10 / 10
                                  hpa = int(tanks.content) - member_data2.tanks - hpa_f
                              
                                  killerz = member_data2.resources - hpa * 6
                                  killer = hpa * 6 

                                  final =  member_data2.tanks - hp2t + hp2t + hp2 / 10
                              
                              
                             
                            
                                  win = discord.Embed(description=f"**__Commander {ctx.author.name}'s Offence__**\n{dead} {sold}\n{int(round(hpa))} {tank}\n{hearts} : `{health1}`\n**__Commander {victim.name}'s Defence__**\n{dead} {sold}\n{dead} {tank}\n{hearts} : `0`", color=0xfbc28d)
                            
                                  await ctx.send(embed=win)
                            
                                  winner1 = discord.Embed(title="Attack Completed Successfully", description=F"**Commander {ctx.author.name}** wins the battle with {round(hpa)} {tank} left!", color=0x567d46)
                            
                                  if killerz <= 0:
                                    winner1.add_field(name="__Rewards:__", value=f"{member_data2.resources} {res}")
                                    
                                    await ctx.send(embed=winner1)
                                    member_data.resources += member_data2.resources
                                    member_data.strikes -= 1
                                    member_data2.soldiers = 0 
                                    member_data.soldiers -= int(soldiers.content)
                                    member_data.tanks -= int(round(final))
                                    member_data2.tanks = 0
                                    member_data2.resources = 0
                                    member_data.medals += 1
                                    
                                    save_member_data(ctx.author.id, member_data)
                                    save_member_data(victim.id, member_data2)
                                    emergency3 = discord.Embed(description=f"**Emergency**\n-\nYou have been attacked by commander `{ctx.author.name} ({ctx.author.id})`\n-\nYour defences lost, and your troops are dead", color=red)
                                    await victim.send(embed=emergency3)
                                  
                                  
                                    return
                                  else:
                                    member_data2.resources -= int(round(killer))
                                    member_data.soldiers -= int(tanks.content)
                                    member_data.tanks -= int(round(final))
                                    member_data2.soldiers = 0 
                                    member_data2.tanks = 0
                                    member_data.resources += int(round(killer))
                                    member_data.strikes -= 1
                                    member_data.medals += 1
                                    
                                    save_member_data(ctx.author.id, member_data)
                                    save_member_data(victim.id, member_data2)
                              

                                    winner1.add_field(name="__Rewards:__", value=f"{round(killer)} {res}")
                                    
                                    await ctx.send(embed=winner1)
                                    emergency3 = discord.Embed(description=f"**Emergency**\n-\nYou have been attacked by commander `{ctx.author.name} ({ctx.author.id})`\n-\nYour defences lost, and your troops are dead", color=red)
                                    await victim.send(embed=emergency3)
                                    return
                                if hp1t > hp2t:
                            

                                  half2 = member_data2.resources - hp1 * 2 + hp1t * 6 
                                  result = member_data2.soldiers - hp1 + hp1
                                  result2 = member_data2.tanks - hp1t + hp1t
                                  half3 = hp1 * 2 + hp1t * 6
                            
                                  win = discord.Embed(description=f"**__Commander {ctx.author.name}'s Offence__**\n{hp1} {sold}\n{hp1t} {tank}\n{hearts} : `{health1}`\n**__Commander {victim.name}'s Defence__**\n{dead} {sold}\n{dead} {tank}\n{hearts} : `0`", color=0xfbc28d)
                            
                                  await ctx.send(embed=win)
                            
                                  winner1 = discord.Embed(title="Attack Completed Successfully", description=F"**Commander {ctx.author.name}** wins the battle with {hp1} {sold} & {hp1t} {tank} left!", color=0x567d46)
                            
                                  if half2 <= 0:
                                    winner1.add_field(name="__Rewards:__", value=f"{member_data2.resources} {res}")
                                   
                                    await ctx.send(embed=winner1)
                                    member_data.resources += member_data2.resources
                                    member_data.strikes -= 1
                                    member_data2.soldiers = 0 
                                    member_data.soldiers -= int(result)
                                    member_data.tanks -= int(result2)
                                    member_data2.tanks = 0
                                    member_data2.resources = 0
                                    member_data.medals += 1
                                    
                                    save_member_data(ctx.author.id, member_data)
                                    save_member_data(victim.id, member_data2)
                                    emergency3 = discord.Embed(description=f"**Emergency**\n-\nYou have been attacked by commander `{ctx.author.name} ({ctx.author.id})`\n-\nYour defences lost, and your troops are dead", color=red)
                                    await victim.send(embed=emergency3)
                                  
                                  
                                    return
                                  else:
                                    member_data2.resources -= int(round(half3))
                                    member_data.soldiers -= int(result)
                                    member_data.tanks -= int(result2)
                                    member_data2.soldiers = 0 
                                    member_data2.tanks = 0
                                    member_data.resources += int(round(half3))
                                    member_data.strikes -= 1
                                    member_data.medals += 1
                                    
                                    save_member_data(ctx.author.id, member_data)
                                    save_member_data(victim.id, member_data2)
                              

                                    winner1.add_field(name="__Rewards:__", value=f"{round(half3)} {res}")
                                    
                                    await ctx.send(embed=winner1)
                                    emergency3 = discord.Embed(description=f"**Emergency**\n-\nYou have been attacked by commander `{ctx.author.name} ({ctx.author.id})`\n-\nYour defences lost, and your troops are dead", color=red)
                                    await victim.send(embed=emergency3)
                                    return
                            


                          
                              if hp1r == hp2r:
                                draw = discord.Embed(description=f"**__Commander {ctx.author.name}'s Offence__**\n{dead} {sold}\n{dead} {tank}\n{hearts} : `0`\n**__Commander {victim.name}'s Defence__**\n{dead} {sold}\n{dead} {tank}\n{hearts} : `0`", color=0xfbc28d)
                                await ctx.send(embed=draw)  
                                winner1tt = discord.Embed(title="Draw!", description=F"**Commander {ctx.author.name}** stalemates with **commander {victim.name}**", color=yellow)
                            
                                    
                               
                                await ctx.send(embed=winner1tt)
                                  
                                member_data.soldiers -= int(soldiers.content)
                                member_data.tanks -= int(tanks.content)
                                member_data2.soldiers = 0 
                                member_data2.tanks = 0
                                member_data.strikes -= 1
                              
                                save_member_data(ctx.author.id, member_data)
                                save_member_data(victim.id, member_data2)
                                    
                               
                            
                                  

                                emergency5 = discord.Embed(description="**Emergency**\n-\nYou have been attacked!\n-\nYour defences made it a draw, however your troops are dead", color=yellow)
                                

                                await victim.send(embed=emergency5)
                                return

                              if hp2r > hp1r:
                                if hp2 > hp1:
                                  hp1 = 0

                              

                              
                            
                              
                            
                                  win = discord.Embed(description=f"**__Commander {ctx.author.name}'s Offence__**\n{dead} {sold}\n{hp1t} {tank}\n{hearts} : `0`\n**__Commander {victim.name}'s Defence__**\n{hp2} {sold}\n{dead} {tank}\n{hearts} : `{health2}`", color=0xfbc28d)
                            
                                  await ctx.send(embed=win)
                            
                                  winner1 = discord.Embed(title="Attack Failed!", description=F"**Commander {victim.name}** defended the attack with {hp2} {sold} left!", color=0xFF0000)
                                  

                              
                                  await ctx.send(embed=winner1) 
                                
                                  
                                  
                             
                                
                                  member_data.soldiers -= int(tanks.content)
                                  member_data.tanks -= int(tanks.content)
                                  member_data2.soldiers -= int(hp2) 
                                  member_data2.tanks = 0
                                
                                  member_data.strikes -= 1
                                
                                  
                                  save_member_data(ctx.author.id, member_data)
                                  save_member_data(victim.id, member_data2)
                              

                               
                              
                                  emergency3 = discord.Embed(description=f"**Emergency**\n-\nYou have been attacked!\n-\nYour defences won with {hp2} {sold} & {hp2t} {tank} left", color=red)
                                  await victim.send(embed=emergency3)
                                  return
                                if hp2t < hp1t:
                                  hp2t = 0
                            
                                  hpa = hp2 - hp1t * 10
                               
                                  result = member_data.soldiers - hp2 + hp2
                                  result2 = member_data.tanks - hp2t + hp2t

                            
                                  win = discord.Embed(description=f"**__Commander {ctx.author.name}'s Offence__**\n{dead} {sold}\n{dead} {tank}\n{hearts} : `0`\n**__Commander {victim.name}'s Defence__**\n{hpa} {sold}\n{dead} {tank}\n{hearts} : `{health2}`", color=0xfbc28d)
                            
                                  await ctx.send(embed=win)
                            
                                  winner2 = discord.Embed(title="Attack Failed", description=F"**Commander {victim.name}** defended the attack with {hpa} {sold} left!", color=0xFF0000)
                            
                              
                                  await ctx.send(embed=winner2)
                                
                                  member_data.strikes -= 1
                                  member_data.soldiers -= int(soldiers.content)
                                  member_data.tanks -= int(tanks.content)
                                  member_data2.tanks -= int(result2) 
                                  member_data2.soldiers -= int(result) 
                         
                                 
                                  save_member_data(ctx.author.id, member_data)
                                  save_member_data(victim.id, member_data2)
                                  emergency3 = discord.Embed(description=f"**Emergency**\n-\nYou have been attacked by commander `{ctx.author.name} ({ctx.author.id})`\n-\nYour defences lost, and your troops are dead", color=red)    
                                  await victim.send(embed=emergency3)
                                  
                                  
                                  return
                              
                              

                                
                                  emergency3 = discord.Embed(description=f"**Emergency**\n-\nYou have been attacked!\n-\nYour defences won with {hpa} {sold} left", color=red)
                                  await victim.send(embed=emergency3)
                                  return
                            

                                if hp2t > hp1t:
                                  hp2 = 0
                                  win = discord.Embed(description=f"**__Commander {ctx.author.name}'s Offence__**\n{dead} {sold}\n{dead} {tank}\n{hearts} : `0`\n**__Commander {victim.name}'s Defence__**\n{dead} {sold}\n{hp2t} {tank}\n{hearts} : `{health2}`", color=0xfbc28d)
                            
                                  await ctx.send(embed=win)
                            
                                  winner1 = discord.Embed(title="Attack Failed", description=F"**Commander {victim.name}** defended the attack with {hp2t} {tank} left!", color=0xFF0000)
                            
                            
                                  
                                  await ctx.send(embed=winner1)
                            
                              
                                  member_data.strikes -= 1
                                  member_data2.soldiers = 0
                                  member_data.soldiers -= int(soldiers.content)
                                  member_data.tanks -= int(tanks.content)
                                  member_data2.tanks = int(hp2t)
                                  save_member_data(ctx.author.id, member_data)
                                  save_member_data(victim.id, member_data2)
                                  emergency3 = discord.Embed(description=f"**Emergency**\n-\nYou have been attacked!\n-\nYour defences won with {hp2t} {tank} left", color=red)
                                  await victim.send(embed=emergency3)
                                  
                                  
                                  return
                            
                            

                            
                          




                            
                            elif str(reaction) == "❌":
                              await war.clear_reactions()
                              Cancel = discord.Embed(description='**Attack cancelled**\n-\n"War does not determine who is right - only who is left" -Anonymous', color=yellow)    
                              member_data.strikes -= 1
                              save_member_data(ctx.author.id, member_data)
                              await ctx.send(embed=Cancel)
                              break
                      
                            try:
                              reaction, user = await self.client.wait_for("reaction_add", timeout=35.0, check=check)
                              await war.remove_reaction(reaction, user)
                              ctx.command.reset_cooldown(ctx)
                            except:
                              break
                  
                      else:
                        error = discord.Embed(title="ERROR", description=f"You don't have that much {tank}! cancelling the attack.", color=yellow)
                        await ctx.send(embed=error)
                        ctx.command.reset_cooldown(ctx)
                        return

                    else:
                      error = discord.Embed(title="ERROR", description=f"The amount of {sold} you entered is out of range from what you currently have, **cancelling the attack sequence**", color=yellow)
                      await ctx.send(embed=error)
                      ctx.command.reset_cooldown(ctx)
                      return
                  elif str(reaction) == "❌":
                    await firm.clear_reactions()
                    vuala = discord.Embed(title="Retreat!", description=f"Attack cancelled, peace should always come first commander :white_check_mark:", color=green)
                    await firm.edit(embed=vuala)
                    ctx.command.reset_cooldown(ctx)
                    return

                  try:
                    reaction, user = await self.client.wait_for("reaction_add", timeout=35.0, check=check)
                    await firm.remove_reaction(reaction, user)
                    ctx.command.reset_cooldown(ctx)
                  except:
                    break
                    
        else:
          await ctx.reply(f"Commander {ctx.author.name}, you can't attack a bot.")
          ctx.command.reset_cooldown(ctx)


  
    @commands.command()
    @commands.guild_only()
    @cooldown(1, per_sec=45, type=commands.BucketType.user)
    async def spy(self, ctx, commander:discord.Member):
      member_data2 = load_member_data(ctx.author.id)
      if member_data2.spy <= 0:
            fail = discord.Embed(title="ERROR", description="**Action failed**, no :detective: available.", color=0xFFD700)
            await ctx.reply(embed=fail)
            ctx.command.reset_cooldown(ctx)
      if member_data2.spy > 0:
        button_c = Button(label="✔", style=discord.ButtonStyle.green)
        button_x = Button(label = "❌", style=discord.ButtonStyle.red)
    
        view = View()
        view.add_item(button_c)
        view.add_item(button_x)
        confirmation = discord.Embed(description=f"Commander, are you sure that you want to spy on {commander.name}'s base?", color=green)
        message = await ctx.reply(embed=confirmation, view=view)
        
        async def button_c_c(interaction):
          if interaction.user == ctx.author:
            await ctx.message.delete()
            member_data2.spy -= 1
            save_member_data(ctx.author.id, member_data2)
            member_data = load_member_data(commander.id)
            health1 = member_data.soldiers * 1
            health2 = member_data.soldiers * 1 + member_data.tanks * 10
      
              
            embeds = discord.Embed(title=f"{commander.name}'s Base", color=red)
        
            embeds.add_field(name="Protection", value=f"{str(member_data.wall)} {wall}\n{member_data.strikes} {strike}", inline = False)
            embeds.add_field(name="Army", value=f"{str(member_data.soldiers)} {sold}\n{str(member_data.tanks)} {tank}\n{str(member_data.spy)} :detective:", inline = False)
            embeds.add_field(name="Specials", value=f"{member_data.ca} {ca}\n{member_data.crate} {crate}", inline = False)
            embeds.add_field(name="Wealth", value=f"{str(member_data.resources)} {res}", inline = False)
            embeds.add_field(name="Total HP", value=f"{health2} {hearts}", inline = False)
  
            embeds.set_thumbnail(url="https://media.discordapp.net/attachments/814828851724943361/995035645053513829/ezgif.com-gif-maker.jpg")
  
              
            await interaction.response.send_message(embed=embeds, ephemeral=True)
            await message.delete()
            return
          else:
            await interaction.response.send_message("This option is not for you!", ephemeral=True)
        async def button_x_c(interaction):
          if interaction.user == ctx.author:
            await ctx.message.delete()
            await message.delete()
            await interaction.response.send_message("Cancelled spy operation :white_check_mark:", ephemeral=True)
            ctx.command.reset_cooldown(ctx)
            return
          else:
            await interaction.response.send_message("This option is not for you!", ephemeral=True)
        button_c.callback = button_c_c
        button_x.callback = button_x_c
          
      


  
    # @commands.command()
    # @commands.guild_only()
    # async def apply(self, ctx):
    #   applications = discord.Embed(title="Army Of Freedom’s Brigadier General application.", description="Hello commander, thank you for supporting Army of Freedom by applying for brigadier general.\n-\nClick the check mark to proceed", color=green)
    #   ap = await ctx.reply(embed=applications)
    #   await ap.add_reaction("✅")
    #   await ap.add_reaction("❌")

    #   def check(reaction, user):
    #       return user == ctx.author
    #   reaction = None

      
    #   while True:
    #     if str(reaction) == "✅":
    #       await ap.clear_reactions()
    #       confirm = discord.Embed(description="Are you sure you want to proceed with the application ?\n-\n**Note: Fooling around/troll submiting/speedruns will not be tolerated and will be facing consequences**", color=yellow)
    #       await ap.edit(embed=confirm)
    #       await ap.add_reaction("✅")
    #       await ap.add_reaction("❌")

    #       def check(reaction, user):
    #         return user == ctx.author
    #       reaction = None

    #       while True:
    #         if str(reaction) == "✅":
    #           await ap.clear_reactions()
    #           guild = ctx.guild
    #           overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False,send_messages=False, add_reactions=False,read_message_history=True,),guild.me: discord.PermissionOverwrite(send_messages=True, view_channel=True),ctx.author: discord.PermissionOverwrite(read_messages=True, send_messages=True)}
    #           channel1 = await guild.create_text_channel(name="fill-the-form", overwrites=overwrites)
    #           suc = discord.Embed(description=f"Please check {channel1.mention} to complete the application :white_check_mark:", color=green)
    #           await ap.edit(embed=suc)
    #           q1 = discord.Embed(title="Question 1",description="What is your current rank in the army?", color=green)
    #           await channel1.send(f"{ctx.author.mention}", embed=q1)
    #           q1a = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == channel1.id,)
    #           q2 = discord.Embed(title="Question 2",description="What are you willing to contribute to the army?", color=green)
    #           await channel1.send(f"{ctx.author.mention}", embed=q2)
    #           q2a = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == channel1.id,)
    #           q3 = discord.Embed(title="Question 3",description="How would you break up an argument between members ?", color=green)
    #           await channel1.send(f"{ctx.author.mention}", embed=q3)
    #           q3a = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == channel1.id,)
    #           q4 = discord.Embed(title="Question 4",description="How do you discuss ideas you disagree with?", color=green)
    #           await channel1.send(f"{ctx.author.mention}", embed=q4)
    #           q4a = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == channel1.id,)
    #           q5 = discord.Embed(title="Question 5",description="Do you have any experience using moderating bots ?  (like mee6, dyno , carl)", color=green)
    #           await channel1.send(f"{ctx.author.mention}", embed=q5)
    #           q5a = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == channel1.id,)
    #           q6 = discord.Embed(title="Question 6",description="Do you have ideas that could help us improve you want to add in future updates?", color=green)
    #           await channel1.send(f"{ctx.author.mention}", embed=q6)
    #           q6a = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == channel1.id,)
    #           q7 = discord.Embed(title="Question 7",description="In what role exactly would you be interested in doing the most, if you got accepted?\n-\n:white_circle:Writer\n\n:white_circle:Designer\n\n:white_circle:Alpha Tester\n\n:white_circle:None, just heavy moderation", color=green)
    #           await channel1.send(f"{ctx.author.mention}", embed=q7)
    #           q7a = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == channel1.id,)
    #           q8 = discord.Embed(title="Question 8",description="What is your time zone ?", color=green)
    #           await channel1.send(f"{ctx.author.mention}", embed=q8)
    #           q8a = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == channel1.id,)
    #           q9 = discord.Embed(title="Question 9",description="How active, on average, are you a day ? (Hours)", color=green)
    #           await channel1.send(f"{ctx.author.mention}", embed=q9)
    #           q9a = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == channel1.id,)


    #           result = discord.Embed(title=f"{ctx.author.name}'s applcation form", description=f"Q1: `What is your current rank/role in the army?`\nA: **{q1a.content}**\n-\nQ2: `What are you willing to contribute to the army?`\nA: **{q2a.content}**\n-\nQ3: `How would you break up an argument between members ?`\nA: **{q3a.content}**\n-\nQ4: `How do you discuss ideas you disagree with, with other Generals?`\nA: **{q4a.content}**\n-\nQ5: `Do you have any experience using moderating bots ?  (like mee6, dyno , carl)`\nA: **{q5a.content}**\n-\nQ6: `Do you have ideas that could help us improve you want to add in future updates?`\nA: **{q6a.content}**\n-\nQ7: `In what role exactly would you be interested in doing the most, if you got accepted?\n-\nWriter\nDesigner\nAlpha Tester\nNone, just heavy moderation`\nA: **{q7a.content}**\n-\nQ8: `What is your time zone ?`\nA: **{q8a.content}**\n-\nQ9: `How active, on average, are you a day ? (Hours)`\nA: **{q9a.content}**", color=yellow)
              
    #           # owner1 = self.client.get_user(569970865744248837)
    #           # owner2 = self.client.get_user(798280308071596063)
    #           system = self.client.get_channel(1028221011503616020)
              
    #           await system.send(embed=result)
             


              
    #           done = discord.Embed(description="Thank you for filling the appication, it will be evaluated and we will reach out to you if you got accepted.\n-\n**This channel will be deleted in 15 seconds**", color=green)
    #           await channel1.send(embed=done)
    #           await asyncio.sleep(15)
    #           await channel1.delete()
    #           break



    #         elif str(reaction) == "❌":
    #           await ap.clear_reactions()
    #           cancel2 = discord.Embed(description="Cancelled application :white_check_mark:!", color=red)
    #           await ap.edit(embed=cancel2)

    #         try:
    #               reaction, user = await self.client.wait_for("reaction_add", timeout=35.0, check=check)
    #               await ap.remove_reaction(reaction, user)
    #         except:
    #           pass
            
              


    #     elif str(reaction) == "❌":
    #       await ap.clear_reactions()
    #       cancel = discord.Embed(description="Cancelled application :white_check_mark:", color=red)
    #       await ap.edit(embed=cancel)
    #     try:
    #           reaction, user = await self.client.wait_for(
    #             "reaction_add", timeout=35.0, check=check
    #         )
    #           await ap.remove_reaction(reaction, user)
    #     except:
    #       pass

  
    @commands.command()
    @commands.guild_only()
    async def trade(self, ctx, member:discord.Member, trader_op, trader_oi, user_op, user_oi):
      if member == ctx.author:
        error1 = discord.Embed(description="Apologies!! we cannot initiate the trade on the same commander, mention seomone else instead!", color=0xFF0000)
        await ctx.reply(embed=error1)
        return
      if trader_oi == "soldiers" or trader_oi =="soldier":
        trader_oemoji = sold
      if trader_oi == "tanks" or trader_oi =="tank":
        trader_oemoji = tank
      if trader_oi == "rspy" or trader_oi =="spy":
        trader_oemoji = spy
      if trader_oi == "wall" or trader_oi =="walls":
        trader_oemoji = wall
      if trader_oi == "strike" or trader_oi =="strikes":
        trader_oemoji = strike
      if trader_oi == "resource" or trader_oi =="resources":
        trader_oemoji = res
      if trader_oi == "crate" or trader_oi == "crates":
        trader_oemoji = crate
      if trader_oi == "ca" or trader_oi == "Ca":
        trader_oemoji = ca

      #-------

      if user_oi == "soldiers" or user_oi =="soldier":
        user_oemoji = sold
      if user_oi == "tanks" or user_oi =="tank":
        user_oemoji = tank
      if user_oi == "rspy" or user_oi =="spy":
          user_oemoji = spy
      if user_oi == "wall" or user_oi =="walls":
          user_oemoji = wall
      if user_oi == "strike" or user_oi =="strikes":
          user_oemoji = strike
      if user_oi == "resource" or user_oi =="resources":
          user_oemoji = res
      if user_oi == "crate" or user_oi == "crates":
        user_oemoji = crate
      if user_oi == "ca" or user_oi == "Ca":
        user_oemoji = ca

        
      
      
      conf1 = discord.Embed(title=f"{ctx.author.name}, please confirm the trade", description=f"**Your offer:\n{trader_op} {trader_oemoji}\n-\nFor {member.name}'s:\n {user_op} {user_oemoji}**", color=yellow)
      conf2 = await ctx.reply(embed=conf1)
      await conf2.add_reaction("✅")
      await conf2.add_reaction("❌")

      def check(reaction, user):
        return user == ctx.author
      reaction = None

      
      while True:
        if str(reaction) == "✅":
          await conf2.clear_reactions()
          conf3 = discord.Embed(title=f"{member.name}, please confirm the trade", description=f"**{ctx.author.name} offers:\n{trader_op} {trader_oemoji}\n-\nFor your:\n{user_op} {user_oemoji}**", color=yellow)

          
          await conf2.edit(embed=conf3)
          await conf2.add_reaction("✅")
          await conf2.add_reaction("❌")
          def check(reaction, user):
            return user == member
          reaction = None
          while True:
            if str(reaction) == "✅":
                await conf2.clear_reactions()
                member_data = load_member_data(ctx.author.id)
              
                user_data = load_member_data(member.id)

                trade = discord.Embed(title="Trade Completed", description=f"{ctx.author.name} traded:\n{trader_op} {trader_oemoji}\n-\nFor {member.name}'s\n{user_op} {user_oemoji}", color=green)

                if trader_oi == "soldier" or trader_oi == "soldiers":
                  if member_data.soldiers < int(trader_op):
                    error = discord.Embed(description=f"You do not have that much {sold}", color=yellow)
                    await conf2.edit(embed=error)
                    return
                  else:
                    if user_oi == "soldier" or user_oi == "soldiers":
                      if member_data2.soldiers < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {sold}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.soldiers -= int(trader_op)
                        user_data.soldiers += int(trader_op)
                        
                        user_data.soldiers -= int(user_op)
                        member_data.soldiers += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "tanks" or user_oi == "tank":
                      if user_data.tanks < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {tank}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.soldiers -= int(trader_op)
                        user_data.soldiers += int(trader_op)
                        
                        user_data.tanks -= int(user_op)
                        member_data.tanks += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "spy" or user_oi == "rspy":
                      if user_data.spy < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {spy}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.soldiers -= int(trader_op)
                        user_data.soldiers += int(trader_op)
                        user_data.spy -= int(user_op)
                        member_data.spy += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "wall" or user_oi == "walls":
                      if user_data.wall < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {wall}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.soldiers -= int(trader_op)
                        user_data.soldiers += int(trader_op)
                        user_data.wall -= int(user_op)
                        member_data.wall += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "strike" or user_oi == "strikes":
                      if user_data.strikes < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {strike}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.soldiers -= int(trader_op)
                        user_data.soldiers += int(trader_op)
                        user_data.strikes -= int(user_op)
                        member_data.strikes += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "resource" or user_oi == "resources":
                      if user_data.resources < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {res}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.soldiers -= int(trader_op)
                        user_data.soldiers += int(trader_op)
                        
                        user_data.resources -= int(user_op)
                        member_data.resources += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                    
              
                elif trader_oi == "tanks" or trader_oi == "tank":
                  if member_data.tanks < int(trader_op):
                    error = discord.Embed(description=f"You do not have that much {tank}", color=yellow)
                    await conf2.edit(embed=error)
                    return
                  else:
                    if user_oi == "soldier" or user_oi == "soldiers":
                      if user_data.soldiers < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {sold}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.tanks -= int(trader_op)
                        user_data.tanks += int(trader_op)
                        user_data.soldiers -= int(user_op)
                        member_data.soldiers += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "tanks" or user_oi == "tank":
                      if user_data.tanks < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {tank}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.tanks -= int(trader_op)
                        user_data.tanks += int(trader_op)
                        user_data.tanks -= int(user_op)
                        member_data.tanks += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "spy" or user_oi == "rspy":
                      if user_data.spy < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {spy}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.tanks -= int(trader_op)
                        user_data.tanks += int(trader_op)
                        user_data.spy -= int(user_op)
                        member_data.spy += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "wall" or user_oi == "walls":
                      if user_data.wall < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {wall}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.tanks -= int(trader_op)
                        user_data.tanks += int(trader_op)
                        user_data.wall -= int(user_op)
                        member_data.wall += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "strike" or user_oi == "strikes":
                      if user_data.strikes < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {strike}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.tanks -= int(trader_op)
                        user_data.tanks += int(trader_op)
                        user_data.strikes -= int(user_op)
                        member_data.strikes += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "resources" or user_oi == "resource":
                      if user_data.resources < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {res}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.tanks -= int(trader_op)
                        user_data.tanks += int(trader_op)
                        user_data.resources -= int(user_op)
                        member_data.resources += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    
                  
                elif trader_oi == "spy" or trader_oi == "rspy":
                  if member_data.spy < int(trader_op):
                    error = discord.Embed(description=f"You do not have that much {spy}", color=yellow)
                    await conf2.edit(embed=error)
                    return
                  else:
                    if user_oi == "soldier" or user_oi == "soldiers":
                      if user_data.soldiers < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {sold}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.spy -= int(trader_op)
                        user_data.spy += int(trader_op)
                        user_data.soldiers -= int(user_op)
                        member_data.soldiers += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "tanks" or user_oi == "tank":
                      if user_data.tanks < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {tank}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.spy -= int(trader_op)
                        user_data.spy += int(trader_op)
                        user_data.tanks -= int(user_op)
                        member_data.tanks += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "spy" or user_oi == "rspy":
                      if user_data.spy < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {spy}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.spy -= int(trader_op)
                        user_data.spy += int(trader_op)
                        user_data.spy -= int(user_op)
                        member_data.spy += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "wall" or user_oi == "walls":
                      if user_data.wall < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {wall}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.spy -= int(trader_op)
                        user_data.spy += int(trader_op)
                        user_data.wall -= int(user_op)
                        member_data.wall += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "strike" or user_oi == "strikes":
                      if user_data.strikes < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {strike}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.spy -= int(trader_op)
                        user_data.spy += int(trader_op)
                        user_data.strikes -= int(user_op)
                        member_data.strikes += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "resource" or user_oi == "resources":
                      if user_data.resources < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {res}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.spy -= int(trader_op)
                        user_data.spy += int(trader_op)
                        user_data.resources -= int(user_op)
                        member_data.resources += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    
                  
                elif trader_oi == "wall" or trader_oi == "walls":
                  if member_data.wall < int(trader_op):
                    error = discord.Embed(description=f"You do not have that much {wall}", color=yellow)
                    await conf2.edit(embed=error)
                    return
                  else:
                    if user_oi == "soldier" or user_oi == "soldiers":
                      if user_data.soldiers < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {sold}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.wall -= int(trader_op)
                        user_data.wall += int(trader_op)
                        user_data.soldiers -= int(user_op)
                        member_data.soldiers += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "tanks" or user_oi == "tank":
                      if user_data.tanks < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {tank}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.wall -= int(trader_op)
                        user_data.wall += int(trader_op)
                        user_data.tanks -= int(user_op)
                        member_data.tanks += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "spy" or user_oi == "rspy":
                      if user_data.spy < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {spy}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.wall -= int(trader_op)
                        user_data.wall += int(trader_op)
                        user_data.spy -= int(user_op)
                        member_data.spy += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "wall" or user_oi == "walls":
                      if user_data.wall < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {wall}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.wall -= int(trader_op)
                        user_data.wall += int(trader_op)
                        user_data.wall -= int(user_op)
                        member_data.wall += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "strike" or user_oi == "strikes":
                      if user_data.strikes < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {strike}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.wall -= int(trader_op)
                        user_data.wall += int(trader_op)
                        user_data.strikes -= int(user_op)
                        member_data.strikes += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "resource" or user_oi == "resources":
                      if user_data.resources < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {res}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.wall -= int(trader_op)
                        user_data.wall += int(trader_op)
                        user_data.resources -= int(user_op)
                        member_data.resources += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    
                  
                elif trader_oi == "strike" or trader_oi == "strikes":
                  if member_data.strikes < int(trader_op):
                    error = discord.Embed(description=f"You do not have that much {strike}", color=yellow)
                    await conf2.edit(embed=error)
                    return
                  else:
                    if user_oi == "soldier" or user_oi == "soldiers":
                      if user_data.soldiers < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {sold}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.strikes -= int(trader_op)
                        user_data.strikes += int(trader_op)
                        user_data.soldiers -= int(user_op)
                        member_data.soldiers += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "tanks" or user_oi == "tank":
                      if user_data.tanks < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {tank}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.strikes -= int(trader_op)
                        user_data.strikes += int(trader_op)
                        user_data.tanks -= int(user_op)
                        member_data.tanks += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "spy" or user_oi == "rspy":
                      if user_data.spy < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {spy}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.strikes -= int(trader_op)
                        user_data.strikes += int(trader_op)
                        user_data.spy -= int(user_op)
                        member_data.spy += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "wall" or user_oi == "walls":
                      if user_data.wall < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {wall}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.strikes -= int(trader_op)
                        user_data.strikes += int(trader_op)
                        user_data.wall -= int(user_op)
                        member_data.wall += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "strike" or user_oi == "strikes":
                      if user_data.strikes < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {strike}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.strikes -= int(trader_op)
                        user_data.strikes += int(trader_op)
                        user_data.strikes -= int(user_op)
                        member_data.strikes += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "resource" or user_oi == "resources":
                      if user_data.resources < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {res}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.strikes -= int(trader_op)
                        user_data.strikes += int(trader_op)
                        user_data.resources -= int(user_op)
                        member_data.resources += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    
                  
                elif trader_oi == "resource" or trader_oi == "resources":
                  if member_data.resources < int(trader_op):
                    error = discord.Embed(description=f"You do not have that much {res}", color=yellow)
                    await conf2.edit(embed=error)
                    return
                  else:
                    if user_oi == "soldier" or user_oi == "soldiers":
                      if user_data.soldiers < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {sold}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.resources -= int(trader_op)
                        user_data.resources += int(trader_op)
                        user_data.soldiers -= int(user_op)
                        member_data.soldiers += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "tanks" or user_oi == "tank":
                      if user_data.tanks < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {tank}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.resources -= int(trader_op)
                        user_data.resources += int(trader_op)
                        user_data.tanks -= int(user_op)
                        member_data.tanks += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "spy" or user_oi == "rspy":
                      if user_data.spy < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {spy}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.resources -= int(trader_op)
                        user_data.resources += int(trader_op)
                        user_data.spy -= int(user_op)
                        member_data.spy += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "wall" or user_oi == "walls":
                      if user_data.wall < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {wall}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.resources -= int(trader_op)
                        user_data.resources += int(trader_op)
                        user_data.wall -= int(user_op)
                        member_data.wall += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "strike" or user_oi == "strikes":
                      if user_data.strikes < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {strike}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.resources -= int(trader_op)
                        user_data.resources += int(trader_op)
                        user_data.strikes -= int(user_op)
                        member_data.strikes += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "resource" or user_oi == "resources":
                      if user_data.resources < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {res}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.resources -= int(trader_op)
                        user_data.resources += int(trader_op)
                        user_data.resources -= int(user_op)
                        member_data.resources += int(user_op)
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return




                  





              
                    if user_oi == "crate" or user_oi == "crates":
                      if user_data.crate < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {res}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.resources -= int(trader_op)
                        user_data.resources += int(trader_op)
                        user_data.crate -= int(user_op)
                        member_data.crate += int(user_op)
                        
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                elif trader_oi == "crate" or trader_oi == "crates":
                  if member_data.crate < int(trader_op):
                    error = discord.Embed(description=f"You do not have that much {res}", color=yellow)
                    await conf2.edit(embed=error)
                    return
                  else:
                    if user_oi == "soldier" or user_oi == "soldiers":
                      if user_data.soldiers < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {sold}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.crate -= int(trader_op)
                        user_data.crate += int(trader_op)
                        user_data.soldiers -= int(user_op)
                        member_data.soldiers += int(user_op)
                
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "tanks" or user_oi == "tank":
                      if user_data.tanks < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {tank}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.crate -= int(trader_op)
                        user_data.crate += int(trader_op)
                        user_data.tanks -= int(user_op)
                        member_data.tanks += int(user_op)
                        
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "spy" or user_oi == "rspy":
                      if user_data.spy < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {spy}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.crate -= int(trader_op)
                        user_data.crate += int(trader_op)
                        user_data.spy -= int(user_op)
                        member_data.spy += int(user_op)
                        
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "wall" or user_oi == "walls":
                      if user_data.wall < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {wall}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.crate -= int(trader_op)
                        user_data.crate += int(trader_op)
                        user_data.wall -= int(user_op)
                        member_data.wall += int(user_op)
                        
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "strike" or user_oi == "strikes":
                      if user_data.strikes < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {strike}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.crate -= int(trader_op)
                        user_data.crate += int(trader_op)
                        user_data.strikes -= int(user_op)
                        member_data.strikes += int(user_op)
                        
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
                  
                    if user_oi == "resource" or user_oi == "resources":
                      if user_data.resources < int(user_op):
                        error = discord.Embed(description=f"{member.name} does not have that much {res}", color=yellow)
                        await conf2.edit(embed=error)
                        return
                      else:
                        
                        await conf2.edit(embed=trade)
                        member_data.crate -= int(trader_op)
                        user_data.crate += int(trader_op)
                        user_data.resources -= int(user_op)
                        member_data.resources += int(user_op)
                        
                        save_member_data(ctx.author.id, member_data)
                        save_member_data(member.id, user_data)
                        return
            
            elif str(reaction) == "❌":
                await conf2.clear_reactions()
                cancel = discord.Embed(description=f"Sorry {ctx.author.mention}, {member.mention} refused to trade", color=red)
                await conf2.edit(embed=cancel)
                return

            try:
                reaction, user = await self.client.wait_for(
                "reaction_add", timeout=35.0, check=check
              )
                await conf2.remove_reaction(reaction, user)
            except:
              pass

        elif str(reaction) == "❌":
            await conf2.clear_reactions()
            cancel = discord.Embed(description="Cancelled trade :white_check_mark:", color=red)
            await conf2.edit(embed=cancel)
            return
        try:
              reaction, user = await self.client.wait_for(
                "reaction_add", timeout=35.0, check=check
            )
              await conf2.remove_reaction(reaction, user)
        except:
          pass
    @commands.command()
    @commands.guild_only()
    async def sell(self, ctx, amount, item):
      member_data = load_member_data(ctx.author.id)
      guild = ctx.guild
      with open("prefix.json", "r", encoding="utf-8") as fp:
        custom_prefixes = json.load(fp)
        prefix = custom_prefixes[f"{guild.id}"]

      if not amount[0].isnumeric():
        invamount = discord.Embed(title="Invalid Amount", description=f"Sorry, `{amount}` is an invalid integer/number, please include an integer and nothing else.\n`Ex. {prefix}sell 1 {item}`", color=red)
        await ctx.reply(embed=invamount)
        return

      if item not in ["tanks", "tank", "spy", "rspy", "wall", "walls", "strike", "strikes"]:
        notin = discord.Embed(title="Invalid Item", description="Sorry this item has not been identified, available items are; `[tank, spy, wall, strike]`", color=red)
        await ctx.reply(embed=notin)
        return
      
      if item == "tanks" or item == "tank":
        if member_data.tanks < int(amount):
          error = discord.Embed(description=f"you do not have that much {tank}", color=red)
          await ctx.reply(embed=error)
          return
        else:
          
          
          gain = 35 * int(amount)

          conf = discord.Embed(description=f"Commander {ctx.author.name}, are you sure you want to sell {amount} {item} for {int(gain)} {res}?", color=green)

          conf2 = await ctx.reply(embed=conf)

          await conf2.add_reaction("✅")
          await conf2.add_reaction("❌")

          def check(reaction, user):
            return user == ctx.author

          reaction = None
          while True:  
            if str(reaction) == "✅":
              await conf2.clear_reactions()
              member_data.tanks -= int(amount)
              member_data.resources += int(gain)
              save_member_data(ctx.author.id, member_data)
              done = discord.Embed(description=f"**You have succesfully sold {amount} {item} for {int(gain)} {res}**", color=green)
              await conf2.edit(embed=done)
              return
              
              
            elif str(reaction) == "❌":
                await conf2.clear_reactions()
                cancel = discord.Embed(description="Cancelled the sell command", color=red)
                await conf2.edit(embed=cancel)

            try:
                reaction, user = await self.client.wait_for(
                "reaction_add", timeout=35.0, check=check
              )
                await conf2.remove_reaction(reaction, user)
            except:
              pass



          
          
        
      if item == "spy" or item == "rspy":
        if int(amount) > member_data.spy:
          error = discord.Embed(description=f"you do not have that much {spy}", color=red)
          await ctx.reply(embed=error)
          return
        else:
          gain2 = 60 * int(amount)
          conf3 = discord.Embed(description=f"Commander {ctx.author.name}, are you sure you want to sell {amount} {item} for {int(gain2)} {res}?", color=green)

          conf2 = await ctx.reply(embed=conf3)

          await conf2.add_reaction("✅")
          await conf2.add_reaction("❌")

          def check(reaction, user):
            return user == ctx.author

          reaction = None
          while True:
            if str(reaction) == "✅":
              await conf2.clear_reactions()
              await conf2.clear_reactions()
              
              member_data.spy -= int(amount)
              member_data.resources += int(gain2)
              save_member_data(ctx.author.id, member_data)
              done = discord.Embed(description=f"**You have succesfully sold {amount} {item} for {int(gain2)} {res}**", color=green)
              await conf2.edit(embed=done)
              return
            elif str(reaction) == "❌":
                await conf2.clear_reactions()
                cancel = discord.Embed(description="Cancelled the sell command", color=red)
                await conf2.edit(embed=cancel)

            try:
                reaction, user = await self.client.wait_for(
                "reaction_add", timeout=35.0, check=check
              )
                await conf2.remove_reaction(reaction, user)
            except:
              pass

        
      if item == "wall" or item == "walls":
        if int(amount) > member_data.wall:
          error = discord.Embed(description=f"you do not have that much {wall}", color=red)
          await ctx.reply(embed=error)
          return
        else:
          gain3 = 350 * int(amount)
          conf4 = discord.Embed(description=f"Commander {ctx.author.name}, are you sure you want to sell {amount} {item} for {int(gain3)} {res}?", color=green)

          conf2 = await ctx.reply(embed=conf4)

          await conf2.add_reaction("✅")
          await conf2.add_reaction("❌")

          def check(reaction, user):
            return user == ctx.author

          reaction = None
          while True:
            if str(reaction) == "✅":
              await conf2.clear_reactions()
              member_data.wall -= int(amount)
              member_data.resources += int(gain3)
              save_member_data(ctx.author.id, member_data)
              done = discord.Embed(description=f"**You have succesfully sold {amount} {item} for {int(gain3)} {res}**", color=green)
              await conf2.edit(embed=done)
              return
            elif str(reaction) == "❌":
                await conf2.clear_reactions()
                cancel = discord.Embed(description="Cancelled the sell command", color=red)
                await conf2.edit(embed=cancel)

            try:
                reaction, user = await self.client.wait_for(
                "reaction_add", timeout=35.0, check=check
              )
                await conf2.remove_reaction(reaction, user)
            except:
              pass
        
      if item == "strike" or item == "strikes":
        if int(amount) > member_data.strikes:
          error = discord.Embed(description=f"you do not have that much {strike}", color=red)
          await ctx.reply(embed=error)
          return
        else:
          gain4 = 475 * int(amount)
          conf5 = discord.Embed(description=f"Commander {ctx.author.name}, are you sure you want to sell {amount} {item} for {int(gain4)} {res}?", color=green)

          conf2 = await ctx.reply(embed=conf5)

          await conf2.add_reaction("✅")
          await conf2.add_reaction("❌")

          def check(reaction, user):
            return user == ctx.author

          reaction = None
          while True:
            if str(reaction) == "✅":
          
              await conf2.clear_reactions()
              member_data.strikes -= int(amount)
              member_data.resources += int(gain4)
              save_member_data(ctx.author.id, member_data)
              done = discord.Embed(description=f"**You have succesfully sold {amount} {item} for {int(gain4)} {res}**", color=green)
              await conf2.edit(embed=done)
              return
            elif str(reaction) == "❌":
                  await conf2.clear_reactions()
                  cancel = discord.Embed(description="Cancelled the sell command", color=red)
                  await conf2.edit(embed=cancel)

            try:
                reaction, user = await self.client.wait_for(
                "reaction_add", timeout=35.0, check=check
              )
                await conf2.remove_reaction(reaction, user)
            except:
              pass
          
      
      
    
           
      
















async def setup(client):
    await client.add_cog(actions(client))   

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



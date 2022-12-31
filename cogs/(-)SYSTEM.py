import discord
from discord.ext import commands
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
import json
import time
from emojis import red, green, yellow, inv


class errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    def better_time(self, cd:int):
        time = f"{cd}s"
        if cd > 60:
            minutes = cd - (cd % 60)
            seconds = cd - minutes
            minutes = int(minutes/ 60)
            time = f"{minutes}m {seconds}s"
            if minutes > 60:
                hoursglad = minutes -(minutes % 60)
                hours = int(hoursglad/ 60)
                minutes = minutes - (hours*60)
                time = f"{hours}h {minutes}m {seconds}s"
        return time

    def determine_prefix(bot, msg):
      DEFAULT_PREFIX = ">"
      guild = msg.guild
      base = [DEFAULT_PREFIX]

      with open("prefix.json", "r", encoding="utf-8") as fp:
          custom_prefixes = json.load(fp)

      if guild:
        try:
            prefix = custom_prefixes[f"{guild.id}"]
            return prefix
        except KeyError:
            return base
            return prefix

      return base

    @commands.command(aliases=["Change_prefix", "change_prefix","cp"])
    @commands.has_permissions(manage_guild=True)
    async def prefix(self, ctx, prefixes: str = None):
      with open("prefix.json", "r", encoding="utf-8") as fp:
        custom_prefixes = json.load(fp)  
      try:
        custom_prefixes[f"{ctx.guild.id}"] = prefixes  
      except KeyError: 
        new = {ctx.guild.name: prefixes}
        custom_prefixes.update(new)  
      await ctx.send(f"Prefix is now `{prefixes}` on the server.")
      await ctx.guild.me.edit(nick=f"{prefixes} | Theta")

      with open("prefix.json", "w", encoding="utf-8") as fpp:
        json.dump(custom_prefixes, fpp, indent=2)



  

    @commands.Cog.listener()
    async def on_guild_join(self, guild):        
        
        owner = self.client.get_user(798280308071596063)
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                embed = discord.Embed(title=f"Greetins '{guild.name}'!", color=red)
                embed.add_field(name="Configuration :arrow_heading_down:",value=f"Hello there and thank you guys for inviting me in! my default prefix is `>` and say `>help` to get a list of commands that you can use! **You can change my prefix by saying `>change_prefix [prefix]` if you wish to**",inline=False)
                embed.set_thumbnail(url=guild.icon)

                with open("prefix.json", "r") as f:
                    prefixes = json.load(f)
                    prefixes[str(guild.id)] = f">"
                with open("prefix.json", "w") as f:
                    json.dump(prefixes, f, indent=4)

                
            await channel.send(embed=embed)

            join = discord.Embed(title="Server Report On Join", description=f"`Guild Name`: {guild.name} ({guild.id})\n`Owner`: {guild.owner} ({guild.owner.id})\n`Member Count`: {guild.member_count}", color=green)
        
            await owner.send(embed=join)
            break

#------------------------------------------------------------------------
  
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        owner = self.client.get_user(798280308071596063)
        with open("prefix.json", "r") as f:
            prefixes = json.load(f)

            prefixes.pop(str(guild.id))

            with open("prefix.json", "w") as f:
                json.dump(prefixes, f, indent=4)
              
        report = discord.Embed(title="Server Report On Leave", description=f"{guild.name}" ,color=red) 
      
        report.add_field(name="Owner:", value=f"{guild.owner} ({guild.owner.id})", inline=True)
        report.add_field(name="Guild ID", value=f"{guild.id}", inline = True)
      
        report.add_field(name="Member Count:", value=f"{guild.member_count}", inline = True)
        await owner.send(embed=report)



    











   



  
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        
        owner = self.client.get_user(798280308071596063)

        default_log = discord.utils.get(self.client.get_all_channels(), id=1057356641911181373)

        
        

        if isinstance(error, commands.NotOwner):
            staff = discord.Embed(title="Developer/staff-only Command", description="Apologies, this command can only be accessed by the bot's staff/developers", color=red)
            await ctx.reply(embed=staff)

          
        # elif isinstance(error, MissingPermissions):
        #   perms = discord.Embed(title="Missing Permissions", description=f"Hey there **{ctx.author.name}**, I'm sorry but i can't let you perform this command as you need ``{error.missing_perms}`` permission for it!", color=red)    
        #   await ctx.reply(embed=perms)
          
        
        elif isinstance(error, MissingRequiredArgument):
          arg = discord.Embed(title="Missing Argument", description=f"Hey there **{ctx.author.name}**, You missed an __argument__ while trying to perform this command, you need to mention ``{error.param.name}``, refer back to **theta's help guide** to discover the needed arguments!", color=red)
          await ctx.reply(embed=arg)
          ctx.command.reset_cooldown(ctx)

          
        elif isinstance(error, CommandNotFound):
            #com = discord.Embed(title="Unkown Command", description=f"Sorry, this command was not found in the bot", color=red)
            #await ctx.reply(embed=com)
            await ctx.message.add_reaction("❌")

        elif isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
            if cd == 0:
              cd = 1
            # cool = discord.Embed(description='**Action failed**, this action can’t be done at the moment, it’s estimated that this action can be done <t:{}:R>.'.format(int(time.time() + error.retry_after)), color=red)
            em = discord.Embed(title="Cooldown",description=f"**due to cooldown, you can retry this command in** ` {self.better_time(cd)} `", color=red)
            await ctx.reply(embed=em)

        elif isinstance(error, commands.MemberNotFound):
          er = discord.Embed(description=f"**Invalid Member**, please mention a valid member inside of the server, ex. `@{owner}`", color=red)
          await ctx.reply(embed=er)

        elif isinstance(error, commands.DisabledCommand):
          main = discord.Embed(title="Maintenance in prefix commands", description=f"Hey there {ctx.author.mention}!\n-\n> **We are on maintenance!**, which means that some commands will be offline/not working till we finish the maintenance process. If you're curious to check the maintenance status then don't forget to join us at [The Official Theta](https://discord.gg/82Jf7uEqDs) server!", color=yellow)
          await ctx.reply(embed=main)
        
        
        
        else:
            error_message = discord.Embed(title=f"An Error Occured", description=f"> **This is a script error**, an issue ticket has been made for the __development team__ to fix this issue.\n-\n> As the issue is being resolved, please make sure you are using the correct arguments required for the command.\n-\nBest Regards,\nTheta's Development Team", color=red)
            # em.add_field(
            #     name="Terminal error :arrow_heading_down:",
            #     value=f"``{str(error)}``",
            #     inline=True,
            # )
            await ctx.send(embed=error_message)
            ctx.command.reset_cooldown(ctx)
            try:
              await ctx.message.add_reaction("⚠")
            except:
              pass

            



            system_error = discord.Embed(title=f"Script Error in '{ctx.guild.name}'", description=f"`{str(error)}`\n-\nCommand Executer: {ctx.author}({ctx.author.id})\nServer ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nCommand Message: [Error here]({ctx.message.jump_url})", color=inv)

            await default_log.send("<@&1047250525323808788>", embed=system_error)

            raise error
          
            

#------------------------------------------------------------------------------------------------

    

async def setup(client):
    await client.add_cog(errors(client))

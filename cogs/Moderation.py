import discord
from discord.ext import commands


class Moderation(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready')


    @commands.command()
    async def clear(self, ctx, amount=0):
        authorperms = ctx.author.permissions_in(ctx.channel)
        if authorperms.manage_messages:
            if amount == 0:
                await ctx.send('Give me an amount u fuck')
            else:
                await ctx.channel.purge(limit=amount + 1)
        else:
            await ctx.send("I dont think u have the facilities for that, big man")
      

    @commands.command()
    async def kick(self, ctx, member : discord.Member=None, *,reason=None):
        authorperms = ctx.author.permissions_in(ctx.channel)
        if authorperms.manage_messages:
            if member == None:
                await ctx.send('Give me someone to kick u fuck')
            else:
                await member.kick(reason=reason)
                await ctx.send(f'Succesfully kicked the retard {member.mention} for {reason}')
        else:
            await ctx.send("I dont think u have the facilities for that, big man")
      
        
    @commands.command()
    async def ban(self, ctx, member : discord.Member=None, *,reason=None):
        authorperms = ctx.author.permissions_in(ctx.channel)
        if authorperms.manage_messages:
            if member == None:
                await ctx.send('Give me someone to ban u fuck')
            else:
                await member.ban(reason=reason)
                await ctx.send(f'Succesfully banned the retard {member.mention} for {reason}')
        else:
            await ctx.send("I dont think u have the facilities for that, big man")
        
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unban(self, ctx, *, member):
        await ctx.send('Unban him yourself through server settings, cant get this to work.')
                
    @commands.command()
    async def mute(self, ctx, member: discord.Member=None, reason=None):
        authorperms = ctx.author.permissions_in(ctx.channel)
        if authorperms.manage_messages:
            if member == None:
                await ctx.send('Give me someone to mute u fuck')
            else:
                role = discord.utils.get(ctx.guild.roles, name="Muted") # retrieves muted role returns none if there isn't 
                await member.add_roles(role) # adds already existing muted role
                await ctx.send(f"{member.mention} has been muted for {reason}")
        else:
            await ctx.send("I dont think u have the facilities for that, big man")
        

    @commands.command()
    async def unmute(self, ctx, member: discord.Member=None):
        authorperms = ctx.author.permissions_in(ctx.channel)
        if authorperms.manage_messages:
            if member == None:
                await ctx.send('Give me someone to unmute u fuck')
            else:
                await member.remove_roles(discord.utils.get(ctx.guild.roles, name="Muted")) # removes muted role
                await ctx.send(f"{member.mention} has been unmuted")
        else:
            await ctx.send("I dont think u have the facilities for that, big man")

    @commands.command()
    @commands.is_owner()
    async def diebitch(self, ctx):
        await ctx.send('About to kill myself, cya')
        await ctx.bot.logout()

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        if message.content.startswith('how do i join', ) or message.content.startswith('How do i join'):
            await channel.send('Fuck outta here kid, this aint no clan')
            await message.add_reaction('🇸')
            await message.add_reaction('🇹') 
            await message.add_reaction('🇺') 
            await message.add_reaction('🇵') 
            await message.add_reaction('🇮') 
            await message.add_reaction('🇩')
    
    
def setup(bot):
    bot.add_cog(Moderation(bot))
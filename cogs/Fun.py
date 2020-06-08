import discord
from discord.ext import commands
from discord.utils import get
import random
import youtube_dl
import os
import shutil
from os import system
import urllib.parse, urllib.request, re


class Fun(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def youtube(self, ctx, *, search):

        query_string = urllib.parse.urlencode({
            'search_query': search
        })
        htm_content = urllib.request.urlopen(
            'http://www.youtube.com/results?' + query_string
        )
        search_results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
        await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

        
    @commands.command()
    async def wubkub(self, ctx):
        await ctx.send('Issa retard')

    @commands.command()
    async def say(self, ctx, *, arg):
        authorperms = ctx.author.permissions_in(ctx.channel)
        if authorperms.manage_messages:
            channel = self.bot.get_channel(487323849126576131)
            await channel.send(arg)
        else:
            await ctx.send("I dont think u have the facilities for that big man")
        
    
    @commands.command()
    async def dm(self, ctx):
        await ctx.author.send('Ur mum')


    
def setup(bot):
    bot.add_cog(Fun(bot))
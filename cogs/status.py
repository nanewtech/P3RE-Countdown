import discord
from discord.ext import commands
from discord import app_commands
import psutil,os
import math
import datetime
import time

botPfp = 'https://media.discordapp.net/attachments/692413957910298935/1249014322185900102/image.png?ex=6665c2bb&is=6664713b&hm=35d9341bd8ff2dff4625c99b8eda6ad391f701bf555171b627a7b33596d78747&=&format=webp&quality=lossless'
succesColor = discord.Colour.from_rgb(36,54,99)


class statuscmd(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.startupTIME = math.floor(time.time())

    @app_commands.command(name='status', description='Gives you some stats about the bot')
    async def status(self, interaction:discord.Interaction):
        process = psutil.Process(os.getpid())
        usage = (process.memory_info().rss / 1048576) * 10 
        usage = math.ceil(usage) / 10
        
        
        embed = discord.Embed(title='P3R Episode Aigis Countdown#8145', description=f'requested by <@{interaction.user.id}>', timestamp=datetime.datetime.now(), color=succesColor)
        embed.add_field(name='Bot created by: nanewtech#0', value=f'**Bot Version:** v2.0 - [changelog](https://github.com/nanewtech/P3RE-Countdown/releases)\n**Python Version:** 3.9.13\n**discord.py Version:** 2.1.0\n**Memory Usage:** {usage} MB\n**Active servers:** {len(self.bot.guilds)}\n**Current Session online since:** <t:{self.startupTIME}:f>')
        embed.set_thumbnail(url=botPfp)
        embed.set_footer(text=f'P3R Episode Aigis Countdown Bot', icon_url=botPfp)
        
        await interaction.response.send_message(embed=embed)


async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(statuscmd(bot))
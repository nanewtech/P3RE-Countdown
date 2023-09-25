import discord
from discord.ext import commands
from discord import app_commands
import psutil,os
import math
import datetime
import time

botPfp = 'https://media.discordapp.net/attachments/778613210773323776/1143973038296154142/image.png'
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
        
        
        embed = discord.Embed(title='PERSONA 3 RELOAD COUNTDOWN#8145', description=f'requested by <@{interaction.user.id}>', timestamp=datetime.datetime.now(), color=succesColor)
        embed.add_field(name='Bot created by: nanewtech#0', value=f'**Bot Version:** v1.5 - [changelog](https://github.com/nanewtech/P3Reload-Countdown-Bot/releases) - Updated <t:1695656608:R>\n**Python Version:** 3.9.13\n**discord.py Version:** 2.1.0\n**Memory Usage:** {usage} MB\n**Active servers:** {len(self.bot.guilds)}\n**Current Session online since:** <t:{self.startupTIME}:f>')
        embed.set_thumbnail(url=botPfp)
        embed.set_footer(text=f'PERSONA 3 RELOAD COUNTDOWN BOT', icon_url=botPfp)
        
        await interaction.response.send_message(embed=embed)


async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(statuscmd(bot))
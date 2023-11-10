import discord
from discord.ext import commands
from discord import app_commands
import datetime

botPfp = 'https://media.discordapp.net/attachments/778613210773323776/1143973038296154142/image.png'
succesColor = discord.Colour.from_rgb(36,54,99)

class about(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @app_commands.command(name='about', description='gives you basic information about the bot')
    async def about(self, interaction:discord.Interaction):
        embed = discord.Embed(title='P3RE Countdown#8145', timestamp=datetime.datetime.now(), color=succesColor)
        embed.add_field(name='What is "P3RE Countdown"?',
value=
"""
P3RE Countdown is an [open source](https://github.com/nanewtech/P3RE-Countdown) discord bot fully written in python made to tell you in exactly how many days Persona 3 Reload releases!
along with that it also has a leaderboard to tell you exactly who is the most excited for P3RE! (based on requests sent to the bot)
""",inline= False)
        
        embed.add_field(name='How do i get started?"',
value=
"""
Try out the /help command and see what commands you want to use. If you have any other questions feel free to send me a dm on [Twitter](https://twitter.com/nanewtech) or discord (nanewtech)!
""",inline= False)
        embed.set_thumbnail(url=botPfp)
        embed.set_footer(text=f'PERSONA 3 RELOAD COUNTDOWN BOT', icon_url=botPfp)
        
        await interaction.response.send_message(embed=embed)

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(about(bot))
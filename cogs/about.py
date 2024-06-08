import discord
from discord.ext import commands
from discord import app_commands
import datetime

botPfp = 'https://media.discordapp.net/attachments/692413957910298935/1249014322185900102/image.png?ex=6665c2bb&is=6664713b&hm=35d9341bd8ff2dff4625c99b8eda6ad391f701bf555171b627a7b33596d78747&=&format=webp&quality=lossless'
succesColor = discord.Colour.from_rgb(36,54,99)

class about(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @app_commands.command(name='about', description='gives you basic information about the bot')
    async def about(self, interaction:discord.Interaction):
        embed = discord.Embed(title='P3R Episode Aigis Countdown#8145', timestamp=datetime.datetime.now(), color=succesColor)
        embed.add_field(name='What is "P3R Episode Aigis Countdown"?',
value=
"""
P3R Episode Aigis Countdown is an [open source](https://github.com/nanewtech/P3RE-Countdown) discord bot fully written in python made to tell you in exactly how many days Persona 3 Reload: Episode Aigis releases!
Episode Aigis is a DLC for Persona 3 Reload, which is an Epilogue to the main story.
along with that it also has a leaderboard to tell you exactly who is the most excited for P3R: Episode Aigis! (based on requests sent to the bot)
""",inline= False)
        
        embed.add_field(name='"How do i get started?"',
value=
"""
Try out the /help command and see what commands you want to use. If you have any other questions feel free to send me a dm on [Twitter](https://twitter.com/nanewtech) or discord (nanewtech)!
""",inline= False)
        embed.set_thumbnail(url=botPfp)
        embed.set_footer(text=f'P3R Episode Aigis Countdown Bot', icon_url=botPfp)
        
        await interaction.response.send_message(embed=embed)

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(about(bot))
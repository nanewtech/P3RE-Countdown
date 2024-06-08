import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
import datetime

botPfp = 'https://media.discordapp.net/attachments/692413957910298935/1249014322185900102/image.png?ex=6665c2bb&is=6664713b&hm=35d9341bd8ff2dff4625c99b8eda6ad391f701bf555171b627a7b33596d78747&=&format=webp&quality=lossless'
succesColor = discord.Colour.from_rgb(36,54,99)

class help(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @app_commands.command(name='help', description='responds with general help or specifics about a single command')
    @app_commands.describe(command='command to get more help on')
    @app_commands.choices(command=[
        Choice(name='about', value=1),
        Choice(name='help', value=2), 
        Choice(name='leaderboard', value=3),
        Choice(name='status', value=5),
        Choice(name='weeks', value=6),
        Choice(name='when', value=7)
    ])
    async def about(self, interaction:discord.Interaction, command:app_commands.Choice[int] = None):
        
        if command is None:
            title = 'General help' 
            fieldWhatname = 'How to use the bot'
            fieldWhatvalue = 'This bot uses **slash commans**, meaning that all the commands the bot has are accessed by typing "/" and then choosing one of the many commands the bot has to offer. \n**Try these commands:** /when, /weeks, /leaderboard'
        elif command.value == 1:
            title = '"about" command help' 
            fieldWhatname = 'How to use the command'
            fieldWhatvalue = '/about - Gives you general information about the bot, what it is and how to get started!'
        elif command.value == 2:
            title = '"help" command help' 
            fieldWhatname = 'How to use the command'
            fieldWhatvalue = '/help <command> - replies with specifics on how to use the specified command (you just did this while specifying the "help" command)'
        elif command.value == 3:
            title = '"leaderboard" command help' 
            fieldWhatname = 'How to use the command'
            fieldWhatvalue = '/leaderboard - sends you the top 10 leaderboard with the people that used the bot the most! (based on requests asking for the release)'
        elif command.value == 4:
            title = '"news" command help' 
            fieldWhatname = 'How to use the command'
            fieldWhatvalue = '/news - fetches the latest news about Persona 3 Reload. Updated manually and tries to be as up-to-date as possible!'
        elif command.value == 5:
            title = '"status" command help' 
            fieldWhatname = 'How to use the command'
            fieldWhatvalue = '/status - gets some interesting runtime information about the bot'
        elif command.value == 6:
            title = '"weeks" command help' 
            fieldWhatname = 'How to use the command'
            fieldWhatvalue = '/weeks - calculates the time until Persona 3 Reload: Episode Aigis is released, formatted into weeks and days only'
        elif command.value == 7:
            title = '"when" command help' 
            fieldWhatname = 'How to use the command'
            fieldWhatvalue = '/when - calculates the time until Persona 3 Reload: Episode Aigis is released, percision up to the nanosecond! (last 2 or 3 digits are always a fraction of 8)'
        elif command.value == 8:
            title = '"vote" command help' 
            fieldWhatname = 'How to use the command'
            fieldWhatvalue = '/vote - sends the link to vote for the bot on top.gg'
        embed = discord.Embed(title=title, timestamp=datetime.datetime.now(), color=succesColor)
        embed.add_field(name=fieldWhatname, value=fieldWhatvalue, inline= False)
        if command is None:
            embed.add_field(name='List of commands', value='```/about\n/help\n/leaderboard\n/status\n/weeks\n/when```', inline= False)
        embed.set_thumbnail(url=botPfp)
        embed.set_footer(text=f'P3R Episode Aigis Countdown Bot', icon_url=botPfp)
        
        await interaction.response.send_message(embed=embed)

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(help(bot))
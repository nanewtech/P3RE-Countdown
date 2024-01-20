import discord
from discord.ext import commands
from discord import app_commands

class vote(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @app_commands.command(name='vote', description='sends the link to vote for the bot on top.gg') 
    async def news(self, interaction:discord.Interaction):
        await interaction.response.send_message('Voting is not rewarded at all but it would help a lot, even if the bot wont be up for much longer. heres the link to vote: https://top.gg/bot/1143972748654280806/vote')

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(vote(bot))
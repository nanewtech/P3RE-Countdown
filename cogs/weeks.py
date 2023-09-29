import discord
from discord.ext import commands
from discord import app_commands
import getDate
import database



class weeks(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @app_commands.command(name='weeks', description='Tells you when Persona 3 Reload comes out in weeks and days only')
    async def weeks(self, interaction:discord.Interaction):
        time = getDate.getWeeksDays()
        await interaction.response.send_message(f'<@{interaction.user.id}> Persona 3 Reload comes out in {time}.')
        database.incrementReq(interaction.user.id)


async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(weeks(bot))
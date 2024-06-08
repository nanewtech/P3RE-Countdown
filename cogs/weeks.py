import discord
from discord.ext import commands
from discord import app_commands
import getDate
import database



class weeks(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @app_commands.command(name='weeks', description='Tells you when P3R: Episode Aigis releases in weeks and days only')
    async def weeks(self, interaction:discord.Interaction):
        time = getDate.getWeeksDays()
        if time == 0:
            await interaction.response.send_message(f'<@{interaction.user.id}> Persona 3 Reload: Episode Aigis IS RELEASED! GO PLAY IT RIGHT NOW')
        await interaction.response.send_message(f'<@{interaction.user.id}> Persona 3 Reload: Episode Aigis releases in {time}.')
        database.incrementReq(interaction.user.id)


async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(weeks(bot))
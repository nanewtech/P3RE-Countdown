import discord
from discord.ext import commands
from discord import app_commands
import getDate
import database



class when(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @app_commands.command(name='when', description='Tells you the amount of days until P3R: Episode Aigis releases. Precisely up until the second.')
    async def when(self, interaction:discord.Interaction):
        time = getDate.getDaysExact()
        if time == 0:
            await interaction.response.send_message(f'<@{interaction.user.id}> Persona 3 Reload: Episode Aigis IS RELEASED! GO PLAY IT RIGHT NOW')
        else:
            await interaction.response.send_message(f'<@{interaction.user.id}> Persona 3 Reload: Episode Aigis releases in {time}.')
        database.incrementReq(interaction.user.id)


async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(when(bot))
import discord
from discord.ext import commands
from discord import app_commands
import getDate



class news(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @app_commands.command(name='news', description='gives you the most recent news on Persona 3 Reload! updated as often as possible') 
    async def news(self, interaction:discord.Interaction):
        channel = await self.bot.fetch_channel(1143998627967144056)
        msg = await channel.fetch_message(1166347440400646184)
        await interaction.response.send_message(msg.content)

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(news(bot))
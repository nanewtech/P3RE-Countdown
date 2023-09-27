import discord
from discord.ext import commands
from discord import app_commands
import datetime
import jsonlib

botPfp = 'https://media.discordapp.net/attachments/778613210773323776/1143973038296154142/image.png'
succesColor = discord.Colour.from_rgb(36,54,99)

class leaderboard(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @app_commands.command(name='leaderboard', description='Gives you the top 10 most exited people for Persona 3 Reload. user arg for finding position') 
    async def leaderboard(self, interaction:discord.Interaction, user:discord.Member = None):
        placements = ['🥇', '🥈', '🥉', '4th', '5th', '6th', '7th', '8th', '9th', '10th']
        DICT = jsonlib.lib.read()
        if user == None:
            uid = interaction.user.id
        else:
            uid = user.id
        sortedDICT = dict(sorted(DICT.items(), key=lambda x:x[1], reverse=True))
        embed = discord.Embed(title='Excitement Leaderboard', description=f'Total users: {len(sortedDICT)}', color=succesColor, timestamp=datetime.datetime.now())
        i = -1
        for s in list(sortedDICT.keys()):
            i += 1
            p = placements[i]
            user = await self.bot.fetch_user(int(s))
            embed.add_field(name=p, value=f'{user.name} - {DICT.get(s)} Requests', inline=False)
        if str(uid) in list(sortedDICT.keys()):
            embed.add_field(name=f'User Position: {list(sortedDICT.keys()).index(str(uid)) + 1} ', value=f'<@{uid}> - {DICT.get(str(uid))} Requests', inline=False)
        else:
            embed.add_field(name=f'User Position: N/A ', value=f'<@{uid}> -  User not on Leaderboards.', inline=False)
        embed.set_thumbnail(url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.emojiterra.com%2Ftwitter%2Fv12%2F512px%2F1f3c6.png&f=1&nofb=1&ipt=acb30529deeae03b8a47fb8cd4dec498ea52d15a86dc814f280d01bb564ebfa9&ipo=images')
        embed.set_footer(text=f'PERSONA 3 RELOAD COUNTDOWN BOT', icon_url=botPfp)
        await interaction.response.send_message(embed=embed)

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(leaderboard(bot))
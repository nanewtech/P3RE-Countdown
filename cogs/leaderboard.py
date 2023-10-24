import discord
from discord.ext import commands
from discord import app_commands
import datetime
import database

botPfp = 'https://media.discordapp.net/attachments/778613210773323776/1143973038296154142/image.png'
loading = 'https://www.wpfaster.org/wp-content/uploads/2013/06/loading-gif.gif'
trophy = 'https://images.emojiterra.com/twitter/v12/512px/1f3c6.png'
succesColor = discord.Colour.from_rgb(36,54,99)

class leaderboard(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @app_commands.command(name='leaderboard', description='Gives you the top 10 most exited people for Persona 3 Reload. user arg for finding position') 
    async def leaderboard(self, interaction:discord.Interaction, user:discord.Member = None):
        #make loading embed
        loadembed = discord.Embed(title='Excitement Leaderboard', description='Loading Leaderboard', color=succesColor, timestamp=datetime.datetime.now())
        loadembed.add_field(name='Loading may take some time. Be patient!', value='if this persists for a few minutes over multiple tries create an issue [here](https://github.com/nanewtech/P3RE-Countdown/issues/new), add the bug label and describe the issue!')
        loadembed.set_thumbnail(url=loading)
        loadembed.set_footer(text=f'PERSONA 3 RELOAD COUNTDOWN BOT', icon_url=botPfp)
        await interaction.response.send_message(embed=loadembed)
        #TODO: add pages to the leaderboard
        placements = ['🥇', '🥈', '🥉', '4th', '5th', '6th', '7th', '8th', '9th', '10th']
        #check get uid of given user
        if user == None:
            uid = interaction.user.id
        else:
            uid = user.id

        db = database.getReqOrdered()
        users = database.getAmmountUsers()
        embed = discord.Embed(title='Excitement Leaderboard', description=f'Total users: {users}', color=succesColor, timestamp=datetime.datetime.now())
        i = -1
        for s in db:
            i += 1
            p = placements[i]
            user = await self.bot.fetch_user(s[0])
            embed.add_field(name=p, value=f'{user.name} - {s[1]} Requests', inline=False)
        #TODO: add back user position thing 
        #if uid in list(sortedDICT.keys()):
        #    embed.add_field(name=f'User Position: {list(sortedDICT.keys()).index(str(uid)) + 1} ', value=f'<@{uid}> - {DICT.get(str(uid))} Requests', inline=False)
        #else:
        #    embed.add_field(name=f'User Position: N/A ', value=f'<@{uid}> -  User not on Leaderboards.', inline=False)
        embed.set_thumbnail(url=trophy)
        embed.set_footer(text=f'PERSONA 3 RELOAD COUNTDOWN BOT', icon_url=botPfp)
                
        await interaction.edit_original_response(embed=embed)

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(leaderboard(bot))
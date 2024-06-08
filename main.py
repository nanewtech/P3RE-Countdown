import discord
from discord.ext import commands
import getDate
import database
import os

token = os.getenv("BOT_TOKEN")


class bot(commands.Bot): #commands.AutoShardedBot for when guilds > 1000
    def __init__(self):
        super().__init__(command_prefix='!', intents=discord.Intents.default(), help_command=None)
        self.synced = False
        self.cogslist = [
        'cogs.when',
        'cogs.status',
        'cogs.leaderboard',
        'cogs.weeks',
        'cogs.about',
        'cogs.help'
        ]
    
    async def on_ready(self):
        await self.tree.sync()
        self.synced = True
        
        await self.change_presence(activity=discord.Activity(name="Persona 3 Reload | /help", type=discord.ActivityType.playing), status=discord.Status.idle)
        print(f'logged in as {self.user}')

    async def setup_hook(self):
        for cog in self.cogslist:
            await self.load_extension(cog)


bot = bot()

@bot.event
async def on_message(message:discord.Message):
    if message.author == bot.user:
        return
    if '<@1143972748654280806>' in message.content:
        time = getDate.getDaysExact()
        if time == 0:
            await message.channel.send(f'<@{message.author.id}> Persona 3 Reload: Episode Aigis IS RELEASED! GO PLAY IT RIGHT NOW')
        else:
            await message.channel.send(f'<@{message.author.id}> Persona 3 Reload: Episode Aigis releases in {time}.')
        
        database.incrementReq(message.author.id)
    if not message.guild:
        try:
            time = getDate.getDaysExact()
            if time == 0:
                await message.channel.send(f'<@{message.author.id}> Persona 3 Reload: Episode Aigis IS RELEASED! GO PLAY IT RIGHT NOW')
            else:
                await message.channel.send(f'<@{message.author.id}> Persona 3 Reload: Epsiode Aigis releases in {time}.')
        
            database.incrementReq(message.author.id)
        except discord.errors.Forbidden:
            pass
    else:
        pass


@bot.event
async def on_guild_join(self):
    print('joined a new server')
@bot.event
async def on_guild_remove(self):
    print('left a server')

bot.run(token)
import discord
import random
from discord.ext import commands
from discord.ext import tasks

intents = discord.Intents().all()
# set the command_prefix to the command prefix
client = commands.Bot(command_prefix="!", intents=intents)

# edit to change the list of statuses it randomly chooses
statuses = [""]
# time between statuses change in second
statuse_change_time = 300
# cooldown before another response in seconds float
cooldown_time = 1

is_cooldown = True


@client.event
async def on_ready():
    print("bot up")
    statuse_change.start()
    reset_cooldown.start()


@tasks.loop(seconds=statuse_change_time)
async def statuse_change():
    await client.change_presence(activity=discord.Game(str(random.choice(statuses))))


@tasks.loop(seconds=cooldown_time)
async def reset_cooldown():
    global is_cooldown
    is_cooldown = True


# delete this if you dont want a ping fuction

@client.command()
async def ping(ctx):
    global is_cooldown
    if is_cooldown:
        await ctx.send(str(round(client.latency * 1000)) + "ms")
        is_cooldown = False


# edit after here for commands make sure to add a cooldown

@client.command()
async def hi(ctx):
    global is_cooldown
    if is_cooldown:
        await ctx.send("hello!")
        is_cooldown = False


# add bot token
token = ""
client.run(token)

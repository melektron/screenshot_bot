#from randimage import get_random_image, show_array
#from matplotlib import image as plt_image
from discord import app_commands as apc
from discord.ext import commands as cmds
import discord
import os
import image_capture
from dotenv import dotenv_values


CONFIG = dotenv_values("./.env")

class Make(apc.Group):
    """Manage general commands"""
    def __init__(self, bot: cmds.Bot):
        super().__init__()
        self.bot = bot

    @apc.command()
    async def screenshot(self, interaction: discord.Interaction, file_name: str = "ss1.png"):
        file_name = file_name.strip().replace(" ", "")

        if not os.path.isdir("./captures"):
            os.mkdir("./captures")
        if not os.path.isfile(f"./captures/{file_name}"):
            image_capture.take_picture(file="./captures/" + file_name)

        await interaction.response.send_message("Uploading...")
        file = discord.File(fp=f"./captures/{file_name}")
        await interaction.channel.send("Her ya go!", file=file)

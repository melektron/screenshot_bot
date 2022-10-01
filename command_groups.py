#from randimage import get_random_image, show_array
#from matplotlib import image as plt_image
from discord import app_commands as apc
from discord.ext import commands as cmds
import discord
import os
import image_capture
import time
from dotenv import dotenv_values


CONFIG = dotenv_values("./.env")

class Make(apc.Group):
    """Manage general commands"""
    def __init__(self, bot: cmds.Bot):
        super().__init__()
        self.bot = bot

    @apc.command()
    async def screenshot(self, interaction: discord.Interaction, image_name: str = "ss1", image_type: str = "png"):
        file_name = image_name.strip().replace(" ", "_") + time.strftime("_%Y%m%d-%H%M%S.") + image_type

        if not os.path.isdir("./captures"):
            os.mkdir("./captures")
        if not os.path.isfile(f"./captures/{file_name}"):
            image_capture.take_picture(file="./captures/" + file_name)

        await interaction.response.send_message("Uploading...")
        file = discord.File(fp=f"./captures/{file_name}")
        await interaction.channel.send("Her ya go!", file=file)
    
    @apc.command()
    async def load(self, interaction: discord.Interaction, file_path: str = "./ss1.jpg"):
        file_name = file_path.strip().replace(" ", "_")

        await interaction.response.send_message("Uploading...")
        file = discord.File(fp=f"./{file_name}")
        await interaction.channel.send("Her ya go!", file=file)

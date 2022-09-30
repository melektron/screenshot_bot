#from randimage import get_random_image, show_array
#from matplotlib import image as plt_image
from discord import app_commands as apc
import discord
import os
import image_capture
from dotenv import dotenv_values


CONFIG = dotenv_values("./.env")

class Make(apc.Group):
    """Manage general commands"""
    def __init__(self, bot: discord.ext.commands.Bot):
        super().__init__()
        self.bot = bot

    @apc.command()
    async def screenshot(self, interaction: discord.Interaction, file_name: str = "ss.png"):
        file_name = file_name.strip().replace(" ", "")

        # if image exists, delete it
        if os.path.isfile(f"./{file_name}"):
            os.remove(f"./{file_name}")

 #       img_size = (512, 512)
 #       img = get_random_image(img_size)  # returns numpy array
 #       plt_image.imsave(file_name, img)

        if not file_name.lower().endswith(".png"):
            file_name += ".png"

        await interaction.response.send_message("Just a moment...")

        file_path = image_capture.take_picture() #"countries.png"
        # await interaction.response.send_message(f"making screenshot... ({file_name})")
        file = discord.File(fp=f"{file_path}")
        await this.bot.get_channel(CONFIG["CH_ID"]).send(f"Her ya go!", file=file)
        os.system(f"rm {file}")

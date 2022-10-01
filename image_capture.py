"""
ELEKTRON © 2022
Written by Nilusink and melektron
www.elektron.work
30.09.22, 13:57

Module to handle capturing screenshots from the external video device
"""

import os
import shutil
import asyncio

DEVICE_ID = 0

asyncio.create_subprocess_exec()


async def take_picture(x=1920, y=1080, format="yuyv422", file="./new.png") -> str:
    #shutil.copy("./new.png", file)
    # ffmpeg -f v4l2 -video_size 1920x1080 -input_format yuyv422 -r 1 -i /dev/video0 -update 1 -frames 1 -y new.png
    #os.system(f"ffmpeg -f v4l2 -video_size {x}x{y} -input_format {format} -i /dev/video{DEVICE_ID} -update 1 -frames 1 -y {file}")
    # run ffmpeg in an async subprocess
    process = await asyncio.create_subprocess_exec(
        "ffmpeg", 
        "-f", "v2l2", 
        "-video_size", f"{x}x{y}",
        "-input_format", format,
        "-i", f"/dev/video{DEVICE_ID}",
        "-update", "1",
        "-frames", "1",
        "-y",
        file)
    await process.wait()
    return file

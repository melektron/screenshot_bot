# Warning

You are looking at the version 2 development branch. The goal of this is to create a new version of the bot with new hardware and a better, more reliable (possibly multi-step) software stack. This is not complete and functional jet.

# ScreenShot Bot

A simple discord bot enabeling the user to take screenshots of any HDMI display intercepted by a USB capture card or webcam.
The bot is intended to be run on a Raspberry Pi (Zero) directly connected to the capture card.

## Requirements

Required python libs (can be installed using ```requirements.txt```):
 - discord.py
 - python-dotenv
 - ... (to be added and corrected)

## Secrets and Setup

A ```.env``` file on the project root is required containing the allowed guild ID and bot token:
```
BOT_TOKEN=<bot_token>
GUILD_ID=<guild_id>
```

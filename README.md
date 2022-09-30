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

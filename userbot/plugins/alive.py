"""Check if userbot alive..."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet, check pinned in @XtraTgBot"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`**PARANOID BOT Info:**\n\nTelethon Version: 6.6.6 \nPython Version: 3.7.3\n`"
                     "`Selinux Status: Enforcing!\n\n`"
                     "`My PRO Owner:` @Jprimero15")

import os
import sys
from pyrogram import Client, filters
from config import Config

@Client.on_message(filters.command("restart") & filters.user(Config.ADMIN))
async def restart_bot(client, message):
    await message.reply_text("🔄 Bot Restarting...")
    os.execl(sys.executable, sys.executable, *sys.argv)

import os
import sys
import asyncio
from StarXSpam import Star, DEV,  HEROKU_API_KEY, HEROKU_APP_NAME
from .. import CMD_HNDLR as hl
from telethon import events
from time import time
from datetime import datetime
import heroku3

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
 
 
@Star.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
async def logs(legend):
    if legend.sender_id in DEV:
        if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
            return await legend.reply(
                legend.chat_id,
                "First Set These Vars In Heroku :  `HEROKU_API_KEY` And `HEROKU_APP_NAME`.",
            )
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            app = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            return await legend.reply(
                "Make Sure Your Heroku API Key & App Name Are Configured Correctly In Heroku."
            )
        logs = app.get_log()
        start = datetime.now()
        fetch = await legend.reply("__Fetching Logs...__")
        end = datetime.now()
        ms = (end-start).seconds
        await asyncio.sleep(1)
        await fetch.delete()
        logfile = open("StarXSpamLogs.txt", "w")
        logfile.write("⚡ Star X Spam ⚡ [ IDSpam Logs ]\n\n" + logs)
        logfile.close()
        await Star.send_file(legend.chat_id, "IDSpamLogs.txt", caption=f"⚡ 𝐒𝐭𝐚𝐫 𝐗 𝐒𝐩𝐚𝐦 𝐋𝐨𝐠𝐬 ⚡\n**Time Taken :** `{ms} Seconds`")
    else:
        await legend.reply("Sorry, Only Owner & FullSudo Users Can Access This Command.")



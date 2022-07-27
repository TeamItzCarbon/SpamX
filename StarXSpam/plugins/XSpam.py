async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import asyncio
import base64
import os
import random
import telethon.utils
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from StarXSpam import Star, Star2, Star3, Star4, Star5 , Star6, Star7, Star8, Star9, Star10, Star11, Star12, Star13, Star14, Star15, Star16, Star17, Star18, Star19, Star20, Star21, Star22, Star23, Star24, Star25, Star26, Star27, Star28, Star29, Star30, Star31, Star32, Star33, Star34, Star35, Star36, Star37, Star38, Star39, Star40, SUDO_USERS
from .. import CMD_HNDLR as hl
from resources.data import StarxBoi, GROUP, PORMS

# spam

@Star.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Star2.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Star3.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Star4.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Star5.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Star6.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Star7.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Star8.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Star9.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Star10.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Star11.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Star12.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Star13.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Star14.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Star15.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Star16.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Star17.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Star18.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Star19.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Star20.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
async def spam(e):
    usage = f"**MODULE NAME : SPAM**\n\nCommand :\n\n{hl}spam <count> <message to spam>\n\n{hl}spam <count> <reply to a message>\n\nCount must be an integer."
    error = f"__Spam Module can only be used till 100 count. For bigger spams use BigSpam.__"
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        StarX = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(StarX) == 2:
            message = str(StarX[1])
            counter = int(StarX[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(StarX[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(StarX[0])
            if counter > 100:
                return await e.reply(error)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage)


#bigspam

@Star.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Star2.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Star3.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Star4.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Star5.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Star6.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Star7.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Star8.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Star9.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Star10.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Star11.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Star12.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Star13.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Star14.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Star15.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Star16.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Star17.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Star18.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Star19.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Star20.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
async def spam(e):
    usage = f"**MODULE NAME : BIG SPAM**\n\nCommand :\n\n{hl}bigspam <count> <message to spam>\n\n{hl}bigspam <count> <reply to a message>\n\nCount must be an integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        StarX = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(StarX) == 2:
            message = str(StarX[1])
            counter = int(StarX[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(StarX[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(StarX[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage)

#delayspam

@Star.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Star2.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Star3.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Star4.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Star5.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Star6.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Star7.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Star8.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Star9.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Star10.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Star11.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Star12.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Star13.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Star14.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Star15.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Star16.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Star17.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Star18.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Star19.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Star20.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
async def spam(e):
    usage = f"**MODULE NAME : DELAY SPAM**\n\nCommand :\n\n{hl}delayspam <sleep time> <count> <message to spam>\n\n{hl}delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be an integer."     
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        smex = await e.get_reply_message()
        StarX = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        StarXsexy = StarX[1:]
        if len(StarXsexy) == 2:
            message = str(StarXsexy[1])
            counter = int(StarXsexy[0])
            sleeptime = float(StarX[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:
            counter = int(StarXsexy[0])
            sleeptime = float(StarX[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(StarXsexy[0])
            sleeptime = float(StarX[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage)

#abuse

@Star.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Star2.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Star3.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Star4.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Star5.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Star6.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Star7.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Star8.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Star9.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Star10.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Star11.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Star12.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Star13.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Star14.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Star15.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Star16.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Star17.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Star18.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Star19.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Star20.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
async def spam(e):
    usage = f"**MODULE NAME : DM SPAM**\n\nCommand :\n\n{hl}dmspam <count> <username> <message to spam>\n\n{hl}dmspam <count> <username> <reply to a message>\n\nCount must be an integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        StarX = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 2)
        StarXsexy = StarX[1:]
        smex = await e.get_reply_message()
        if len(StarXsexy) == 2:
            user = str(StarXsexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in StarXBoi:
                text = f"I Can't Dm To StarXBoi's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                message = str(StarXsexy[1])
                counter = int(StarX[0])
                await e.reply("😈 Dm Spam Started 😈")
                for _ in range(counter):
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, message)
                        await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:
            user = str(StarXsexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in StarXBoi:
                text = f"I Can't Dm To StarXBoi's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:           
                 counter = int(StarX[0])
                 await e.reply("😈 Dm Spam Started 😈")
                 for _ in range(counter):
                     async with e.client.action(g, "document"):
                        smex = await e.client.send_file(g, smex, caption=smex.text)
                        await gifspam(e, smex) 
                        await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            user = str(StarXsexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in StarXBoi:
                text = f"I Can't Dm To StarXBoi's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                counter = int(StarX[0])
                await e.reply("😈 Dm Spam Started 😈")
                for _ in range(counter):
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, message)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)       

# LΣGΣΠD | @Hey_LEGEND

@Star.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star2.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star3.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star4.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star5.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star6.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star7.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star8.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star9.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star10.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star11.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star12.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star13.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star14.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star15.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star16.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star17.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star18.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star19.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star20.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star21.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star22.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star23.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star24.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star25.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star26.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star27.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star28.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star29.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star30.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star31.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star32.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star33.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star34.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star35.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star36.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star37.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star38.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star39.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Star40.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
async def pspam(e):
    usage = f"**MODULE NAME : PORN SPAM** \n\ncommand : `{hl}pornspam <count>`"
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        StarX = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(StarX) == 1:
            counter = int(StarX[0])
            if int(e.chat_id) in GROUP:
                text = f"Sorry !! I Can't Spam Here. 🌚"
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                 porrn = random.choice(PORMS)
                 for _ in range(counter):
                     async with e.client.action(e.chat_id, "document"):
                         smex = await e.client.send_file(e.chat_id, porrn)
                         await gifspam(e, smex) 
                     await asyncio.sleep(0.4)
        else:
            await e.reply(usage)

# By - LΣGΣΠD | @Hey_LEGEND
# For StarXBoiSpam | @StarXBoiSpam
# From Kangers Import Madafaka
# Keep Credits Madafaka !!

@Star.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star2.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star3.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star4.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star5.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star6.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star7.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star8.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star9.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star10.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star11.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star12.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star13.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star14.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star15.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star16.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star17.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star18.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star19.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star20.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star21.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star22.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star23.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star24.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star25.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star26.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star27.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star28.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star29.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star30.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star31.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star32.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star33.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star34.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star35.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star36.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star37.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star38.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star39.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Star40.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
async def ppspam(e):
    usage = f"**MODULE NAME : PRIVATELY PORM SPAM** \n\ncommand : {hl}ppspam <count> <group or account's username>\nInfo : give command from your personal group or from anywhere & spam pormography in target group or person's DM/PM\n\n**Note :**Your Spambots Should Be in Both Chats (Obviously)"
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage)
        StarX = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(StarX) == 2:
            user_chat = str(StarX[1])
            uc = await e.client.get_peer_id(user_chat)
            if int(uc) in StarXBoi:
                legend = f"Sorry, I Can't Spam StarXBoi's Owner"
                await e.reply(legend, parse_mode=None, link_preview=None )
            elif int(uc) in GROUP:
                legend = f"Sorry, I Can't Spam There !! 🌚"
                await e.reply(legend, parse_mode=None, link_preview=None )
            else:
                counter = int(StarX[0])
                await e.reply("😈 Starting PormSpam !! 😈")
                for _ in range(counter):
                    p0rn = random.choice(PORMS)
                    async with e.client.action(uc, "document"):
                        await e.client.send_file(uc, p0rn)
                        await asyncio.sleep(0.4)
        else:
            await e.reply(usage)

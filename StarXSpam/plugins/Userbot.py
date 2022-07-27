# Kang With Credits Madafaka !!
 
import os
import sys
from StarXSpam import Star, Star2, Star3, Star4, Star5 , Star6, Star7, Star8, Star9, Star10, Star11, Star12, Star13, Star14, Star15, Star16, Star17, Star18, Star19, Star20, Star21, Star22, Star23, Star24, Star25, Star26, Star27, Star28, Star29, Star30, Star31, Star32, Star33, Star34, Star35, Star36, Star37, Star38, Star39, Star40, SUDO_USERS, OWNER_ID
from StarXSpam import ALIVE_NAME, ALIVE_PIC, ALIVE_TEXT, starversion, mention
from .. import CMD_HNDLR as hl
from telethon import events, version
from telethon.tl.functions.users import GetFullUserRequest
from time import time
from datetime import datetime
 
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
 
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
 
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
 
    time_list.reverse()
    ping_time += ":".join(time_list)
 
    return ping_time
 
@Star.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star11.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star12.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star13.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star14.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star15.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star16.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star17.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star18.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star19.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star20.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star21.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star22.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star23.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star24.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star25.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star26.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star27.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star28.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star29.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star30.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star31.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star32.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star33.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star34.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star35.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star36.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star37.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star38.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star39.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Star40.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
            start = datetime.now()
            check = await e.reply("𝙋𝙤𝙣𝙜!")
            end = datetime.now()
            ms = (end-start).microseconds / 1000
            user = await e.client(GetFullUserRequest(e.sender_id))
            firstname = user.user.first_name
            userid = user.user.id
    if userid == OWNER_ID:
        await check.edit(f"█▀█ █▀█ █▄░█ █▀▀\n█▀▀ █▄█ █░▀█ █▄█\n\n    ⚡ 𝐒𝐭𝐚𝐫 𝐗 𝐒𝐩𝐚𝐦 ⚡\n\n𝐏𝐢𝐧𝐠 : `{ms}` ᴍs\n𝐎𝐰𝐧𝐞𝐫 : {mention}")
    else:
        await check.edit(f"█▀█ █▀█ █▄░█ █▀▀\n█▀▀ █▄█ █░▀█ █▄█\n\n    ⚡ 𝐒𝐭𝐚𝐫 𝐗 𝐒𝐩𝐚𝐦 ⚡\n\n𝐏𝐢𝐧𝐠 : `{ms}` ᴍs\n𝐒𝐮𝐝𝐨 𝐔𝐬𝐞𝐫 : [{firstname}](tg://user?id={userid})")
 
# ALIVE
 
Star_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/8c9cb2a7b29ecc0cd8e74.jpg"
 
Star_TEXT = ALIVE_TEXT if ALIVE_TEXT else "╚»★ 𝗦𝘁𝗮𝗿𝗫𝗦𝗽𝗮𝗺 𝗶𝘀 𝗛𝗲𝗿𝗲 ★«╝"
 
 
 
   
@Star.on(events.NewMessage(incoming=True, pattern=r"\%salive" % hl))
async def alive(event):
    if event.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "𝘊𝘩𝘦𝘤𝘬𝘪𝘯𝘨..."
        check = await event.reply(text, parse_mode=None, link_preview=None)
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await check.delete()
        await Star.send_file(event.chat_id, Star_PIC, caption=f"{Star_TEXT}\n\n════════════════════\n⚡ 𝐏𝐢𝐧𝐠 : {ms}ᵐˢ\n⚡ 𝐎𝐰𝐧𝐞𝐫 : {mention}\n⚡ 𝐒𝐭𝐚𝐫 𝐗 𝐒𝐩𝐚𝐦 : `{starversion}`\n⚡ 𝐏𝐲𝐭𝐡𝐨𝐧 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `3.9.6`\n⚡ 𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `{version.__version__}`\n⚡ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 : [𝗝𝗼𝗶𝗻](t.me/Best_FriendsFor_Ever)\n⚡ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : [𝗝𝗼𝗶𝗻](t.me/its_star_network)\n════════════════════\n\n                  ✨ [𝐑𝐄𝐏𝐎](https://github.com/Starboihacks369/SpamX) ✨")
        
        
   
# help
 
HELP_PIC = "https://telegra.ph/file/8c9cb2a7b29ecc0cd8e74.jpg"
 
StarxBoi = "╚»★ 𝗦𝘁𝗮𝗿 𝗫 𝗦𝗽𝗮𝗺 𝗛𝗲𝗹𝗽 ★«╝\n\n"
 
StarxBoi += f"__ᴄᴍᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ sᴛᴀʀ x sᴘᴀᴍ__\n\n"
 
StarxBoi += f"𝙐𝙨𝙚𝙧𝘽𝙤𝙩 𝘾𝙢𝙙𝙨\n\n"
 
StarxBoi += f" `{hl}ping` - `{hl}alive` - `{hl}setpic` - `{hl}delpic` - `{hl}setname` - `{hl}setbio` - `{hl}inviteall` - `{hl}restart` - `{hl}update` - `{hl}stats` - `{hl}addsudo` - `{hl}logs` \n\n"
 
StarxBoi += f"𝙅𝙤𝙞𝙣/𝙇𝙚𝙖𝙫𝙚 𝘾𝙢𝙙𝙨\n\n"
 
StarxBoi += f" `{hl}join` - `{hl}pjoin` - `{hl}leave`\n\n"
 
StarxBoi += f"𝙎𝙥𝙖𝙢/𝙍𝙖𝙞𝙙 𝘾𝙢𝙙𝙨\n\n"
 
StarxBoi += f" `{hl}spam` - `{hl}bigspam` - `{hl}delayspam` - `{hl}ppspam` \n\n `{hl}abuse` \n\n `{hl}raid` - `{hl}replyraid` - `{hl}dreplyraid` - `{hl}delayraid` \n\n"
 
StarxBoi += f"𝘿𝙈/𝙀𝙘𝙝𝙤 𝘾𝙢𝙙𝙨\n\n"
 
StarxBoi += f" `{hl}dm` - `{hl}dmraid` - `{hl}dmspam` \n\n `{hl}addecho` - `{hl}rmecho` \n"
 
StarxBoi += f"\n[𝘒𝘯𝘰𝘸 𝘔𝘰𝘳𝘦 𝘈𝘣𝘰𝘶𝘵 𝘛𝘩𝘦𝘴𝘦 𝘊𝘔𝘋𝘚](t.me/Spam_Resources/3)\n\n"
 
StarxBoi += f"[✨ Updates ✨](t.me/its_star_network)       [✨ Support ✨](t.me/Best_FriendsFor_Ever)\n"
 
@Star.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Star.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=StarxBoi)                                                         
 
 
@Star.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star10.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star11.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star12.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star13.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star14.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star15.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star16.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star17.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star18.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star19.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star20.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star21.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star22.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star23.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star24.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star25.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star26.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star27.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star28.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star29.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star30.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star31.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star32.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star33.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star34.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star35.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star36.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star37.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star38.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star39.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Star40.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "𝗥𝗲𝘀𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗦𝘁𝗮𝗿𝗫𝗦𝗽𝗮𝗺...\nPlease Wait For Few Seconds !!"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await Star.disconnect()
        except Exception:
            pass
        try:
            await Star2.disconnect()
        except Exception:
            pass
        try:
            await Star3.disconnect()
        except Exception:
            pass
        try:
            await Star4.disconnect()
        except Exception:
            pass
        try:
            await Star5.disconnect()
        except Exception:
            pass
        try:
            await Star6.disconnect()
        except Exception:
            pass
        try:
            await Star7.disconnect()
        except Exception:
            pass
        try:
            await Star8.disconnect()
        except Exception:
            pass
        try:
            await Star9.disconnect()
        except Exception:
            pass
        try:
            await Star10.disconnect()
        except Exception:
            pass
        try:
            await Star11.disconnect()
        except Exception:
            pass
        try:
            await Star12.disconnect()
        except Exception:
            pass
        try:
            await Star13.disconnect()
        except Exception:
            pass
        try:
            await Star14.disconnect()
        except Exception:
            pass
        try:
            await Star15.disconnect()
        except Exception:
            pass
        try:
            await Star16.disconnect()
        except Exception:
            pass
        try:
            await Star17.disconnect()
        except Exception:
            pass
        try:
            await Star18.disconnect()
        except Exception:
            pass
        try:
            await Star19.disconnect()
        except Exception:
            pass
        try:
            await Star20.disconnect()
        except Exception:
            pass
        try:
            await Star21.disconnect()
        except Exception:
            pass
        try:
            await Star22.disconnect()
        except Exception:
            pass
        try:
            await Star23.disconnect()
        except Exception:
            pass
        try:
            await Star24.disconnect()
        except Exception:
            pass
        try:
            await Star25.disconnect()
        except Exception:
            pass
        try:
            await Star26.disconnect()
        except Exception:
            pass
        try:
            await Star27.disconnect()
        except Exception:
            pass
        try:
            await Star28.disconnect()
        except Exception:
            pass
        try:
            await Star29.disconnect()
        except Exception:
            pass
        try:
            await Star30.disconnect()
        except Exception:
            pass
        try:
            await Star31.disconnect()
        except Exception:
            pass
        try:
            await Star32.disconnect()
        except Exception:
            pass
        try:
            await Star33.disconnect()
        except Exception:
            pass
        try:
            await Star34.disconnect()
        except Exception:
            pass
        try:
            await Star35.disconnect()
        except Exception:
            pass
        try:
            await Star36.disconnect()
        except Exception:
            pass
        try:
            await Star37.disconnect()
        except Exception:
            pass
        try:
            await Star38.disconnect()
        except Exception:
            pass
        try:
            await Star39.disconnect()
        except Exception:
            pass
        try:
            await Star40.disconnect()
        except Exception:
            pass
 
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
 

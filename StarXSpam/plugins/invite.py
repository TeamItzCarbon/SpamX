# For StarXSpam | @its_star_network
# From Kangers Import Madafaka
# Keep Credits Madafaka !!

import os
import sys
import random
from os import execl
import asyncio
import telethon.utils
from requests import get
from StarXSpam import Star, Star2, Star3, Star4, Star5 , Star6, Star7, Star8, Star9, Star10, Star11, Star12, Star13, Star14, Star15, Star16, Star17, Star18, Star19, Star20, Star21, Star22, Star23, Star24, Star25, Star26, Star27, Star28, Star29, Star30, Star31, Star32, Star33, Star34, Star35, Star36, Star37, Star38, Star39, Star40, DEV
from .. import CMD_HNDLR as hl
from telethon.tl import functions, types
from telethon import events
 
 
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.events import NewMessage
from telethon.tl.types import Channel, Chat, User
from telethon.tl.functions.channels import GetFullChannelRequest, InviteToChannelRequest, GetParticipantsRequest
from telethon.errors import FloodWaitError
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from urllib.error import HTTPError


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid Channel/Group`")
            return None
        except ChannelPrivateError:
            await event.reply("`This is a Private Channel/Group or I Am Banned From There`")
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or Supergroup Doesn't Exist`")
            return None
        except (TypeError, ValueError) as err:
            await event.reply("`Invalid Channel/Group`")
            return None
    return chat_info



def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = ' '.join(names)
    return full_name

            
@Star.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star2.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star3.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star4.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star5.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star6.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star7.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star8.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star9.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star10.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star11.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star12.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star13.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star14.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star15.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star16.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star17.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star18.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star19.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star20.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star21.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star22.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star23.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star24.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star25.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star26.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star27.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star28.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star29.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star30.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star31.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star32.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star33.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star34.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star35.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star36.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star37.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star38.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star39.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Star40.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
async def get_users(event):
    usage = f"**MODULE NAME : INVITEALL**\n\nCommand :\n\n{hl}inviteall <group username/id/link>"
    if event.sender_id in DEV:
        sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        legend = await event.reply("__Processing... 🌚__")
    else:
    	legend = await event.edit("__Processing... 🌚__")
    legendop = await get_chatinfo(event) ; chat = await event.get_chat()
    if event.is_private:
              return await legend.edit("`Sorry, Can't Add Users Here..!`")    
    s = 0 ; f = 0 ; error = 'None'   
  
    await legend.edit("⚡ 𝐒𝐭𝐚𝐫 𝐗 𝐒𝐩𝐚𝐦 ⚡\n\n🔥 **Terminal Status** 🔥\n\n`Collecting Users..!! ✨`")
    async for user in event.client.iter_participants(legendop.full_chat.id):
                try:
                    if error.startswith("Too"):
                        return await legend.edit(f"⚡ 𝐒𝐭𝐚𝐫 𝐗 𝐒𝐩𝐚𝐦 ⚡\n\n**Terminal Finished With Error :**\n(`May Got Limit Error From Telethon Please Try Again Later`)\n**Error** : \n`{error}`\n\n🎉 Invited `{s}` People \n⚠️ Failed To Invite `{f}` People")
                    await asyncio.sleep(5)
                    await event.client(functions.channels.InviteToChannelRequest(channel=chat,users=[user.id]))
                    s = s + 1                                                    
                    await legend.edit(f"⚡ 𝐒𝐭𝐚𝐫 𝐗 𝐒𝐩𝐚𝐦 ⚡\n\n🔥 **Terminal Running...** 🔥\n\n🎉 Invited `{s}` People \n⚠️ Failed To Invite `{f}` People\n\n**‼️LastError :** `{error}`")                
                except Exception as e:
                    error = str(e) ; f = f + 1             
    return await legend.edit(f"⚡ 𝐒𝐭𝐚𝐫 𝐗 𝐒𝐩𝐚𝐦 ⚡\n\n🔥 **Terminal Finished** 🔥\n\n✨ Successfully Invited `{s}` People \n❌ Failed To Invite `{f}` People")
    
 

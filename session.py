from telethon.sessions import StringSession
from telethon.sync import TelegramClient


print(
    """\n.##.....##.####..######...##.....##.########.##....##
.###...###..##..##....##..##.....##....##.....##..##.
.####.####..##..##........##.....##....##......####..
.##.###.##..##..##...####.#########....##.......##...
.##.....##..##..##....##..##.....##....##.......##...
.##.....##..##..##....##..##.....##....##.......##...
.##.....##.####..######...##.....##....##.......##..."""
)

print("\n • Telethon String Session •")

print("\n\nEnter Your Valid Details To Continue!\n\n")

        
APP_ID = int(input("\nEnter APP ID Here : "))
API_HASH = input("\nEnter API HASH Here : ")


try:
   with TelegramClient(StringSession(), APP_ID, API_HASH) as StarX:
       print("\nSTRING SESSION GENERATED SUCCESSFULLY !!\nCHECK YOUR SAVED MASSAGES.\nString is a Sensitive Data, Don't Share it With Anyone. ")
       StarX.send_message("me", f"**Star X Spam Session :**\n\n`{Star.session.save()}`\n\n__Don't Share it With Anyone.__")
       
except Exception as e:
    print(f"{e}") 

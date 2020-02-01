import sys
import telethon
import socket
mode = "private"
async def main(client, event):
    print(".alive has been called")
    replytxt = "`KKSJ_userbot\n" +\
    "I am alive, Young man!\n\n" +\
    "Python Version: " + sys.version.split(' ')[0] + "\n" +\
    "Telethon Version: " + telethon.__version__ + "\n" +\
    "Server Hostname: " + socket.gethostname() + "\n" +\
    "Owner: Kokosei J`"
    print(replytxt)
    await event.reply(replytxt)
    return
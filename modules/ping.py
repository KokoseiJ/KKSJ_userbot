import subprocess
from subprocess import PIPE, STDOUT

mode = "private"

async def main(client, event):
    print("ping command has been called")
    try:
        address = event.raw_text[1:].split(' ')[1:]
        if not address:
            address = ["google.com"]
        process = subprocess.run(["ping"] + address + ["-c 4"], stdout = PIPE, stderr = STDOUT)
        avr_ping = process.stdout.decode("utf-8").split("\n")[-2].split("/")[-3]
    
        replytxt ="`pong!\n\n" +\
        "average ping time to " + address[0] + " is " + avr_ping + ".`"
    
        print(replytxt)
    
        await event.reply(replytxt)
    except Exception as e:
        replytxt = "`An exception has been occured.\n\n" +\
        "stdout:" + process.stdout.decode("utf-8") + "`"
        print(replytxt)
        await event.reply(replytxt)
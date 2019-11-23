import subprocess

mode = "private"

async def main(client, event):
    print("ping command has been called")
    address = event.raw_text[1:].split(' ')[1:]
    if not address:
        address = ["google.com"]
    process = subprocess.run(["ping"] + address + ["-c 4"], capture_output = True)
    avr_ping = process.stdout.decode("utf-8").split("\n")[-2].split("/")[-3]

    replytxt ="`pong!\n\n" +\
    "average ping time to " + address[0] + " is " + avr_ping + ".`"

    event.reply(replytxt)
import subprocess

mode = "private"

async def main(client, event):
    print("execute command has been called")
    try:
        command = event.raw_text[1:].split(' ')[1:]
        if command:
            process = subprocess.run(command, capture_output = True)
            replytxt = "`" + process.stdout.decode("utf-8") + "`"

        else:
            replytxt = "`Seems like you didn't provide a command`"

        print(replytxt)

        await event.reply(replytxt)

    except Exception as e:
        replytxt = "`An exception has been occured.\n\n" +\
        "stdout:" + process.stdout.decode("utf-8") + "`"
        print(replytxt)
        await event.reply(replytxt)
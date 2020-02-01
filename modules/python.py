import subprocess
from subprocess import PIPE, STDOUT

mode = "private"

async def main(client, event):
    print("python command has been called")
    try:
        commands = event.raw_text.split(' ')[1:]
        command = " ".join(commands).replace("\\n", "\n")
        if command:
            print(command)
            process = subprocess.run(["python3", "-c" + command], stdout = PIPE, stderr = STDOUT)
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

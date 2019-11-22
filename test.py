import os, telethon
from telethon import TelegramClient, events

try:
    api_key = open("api", 'r').readlines()
    print("Found an api file, use it as a key")
    api_id = api_key[0]
    api_hash = api_key[0]

except Exception as e:
    print(e)
    print("api file was not found from the path. setting a new one...")
    api_id = input("Telegram API ID: ")
    api_hash = input("Telegram API HASH: ")
    with open("api", "w") as f:
        f.write(api_id + "\n" + api_hash)
    print("Saved api file.")

client = TelegramClient('meow', api_id, api_hash)
print("Succesfully logged in.")
print("Loading modules...")

public_command = []
private_command = []

for x in os.listdir("modules"):
    if "__" in x:
        continue
    module_name = x.split('.')[0]
    exec("from modules import " + module_name)
    module_mode = eval(module_name + ".mode")
    if module_mode == "public":
        public_command.append(module_name)
    elif module_mode == "private":
        private_command.append(module_name)
    else:
        continue
    print("imported", module_mode, "module", module_name)

@client.on(events.NewMessage)
async def _(event):
    print(event.raw_text)
    if event.raw_text[0] == ".":
        if event.sender.is_self:
            command = event.raw_text[1:].split(' ')[0]
            if command in private_command:
                print("running private command", command, "...")
                await globals()[command].main(event)

client.start()
client.run_until_disconnected()

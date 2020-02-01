import os, telethon, importlib
from telethon import TelegramClient, events

try:
    api_key = open("api", 'r').read().split("/")
    print("Found an api file, use it as a key")
    api_id = api_key[0]
    api_hash = api_key[1]

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

modules = {}

public_command = []
private_command = []

for x in os.listdir("modules"):
    if "__" in x:
        continue
    module_name = x.split('.')[0]
    modules[module_name] = importlib.import_module("modules." + module_name)
    module_mode = modules[module_name].mode
    if module_mode == "public":
        public_command.append(module_name)
    elif module_mode == "private":
        private_command.append(module_name)
    elif module_mode == "multi":
        public_command.append(module_name)
        private_command.append(module_name)
    else:
        continue
    print("imported", module_mode, "module", module_name)

@client.on(events.NewMessage)
async def normal_command_handler(event):
    if event.raw_text[0] == "." and event.sender.is_self:
        command = event.raw_text[1:].split(' ')[0]
        if command in private_command:
            print("running private command", command, "...")
            await modules[command].main(client, event)
    elif event.raw_text[0] == "!":
        command = event.raw_text[1:].split(' ')[0]
        if command in public_command:
            print("running public command", command, "...")
            await modules[command].main(client, event)
    elif event.raw_text == "owo":
        await event.reply("uwu")

client.start()
client.run_until_disconnected()

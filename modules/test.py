mode = "public"
test = "this script is for testing\n"
appendtxt = "test string\n"

async def main(client, event):
    global test
    global appendtxt
    print("Test script has been called.")
    await event.reply(test)
    test += appendtxt

mode = "private"
async def main(event):
	print(".alive has been called")
	await event.reply("`I am alive, Young man!\n\n" + \
	"Python Version: " + sys.version.split(' ')[0] + "\n" + \
	"Telethon version: " + telethon.__version__ + "`" \
	)
	return
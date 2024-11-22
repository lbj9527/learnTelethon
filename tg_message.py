from telethon import TelegramClient, events
import python_socks
import cryptg
from data import *

client = TelegramClient('anon', api_id, api_hash, proxy=(python_socks.ProxyType.SOCKS5, '127.0.0.1', 1089))

#所有网络请求的调用,必须前面加await
#定义函数前加async
# @client.on(events.NewMessage)
# async def my_event_handler(event):
#     if 'hello' in event.raw_text:
#         await event.reply('hi')

@client.on(events.NewMessage(outgoing=True, pattern=r'\\pre'))
async def handler(event):
    if event.is_reply:
        replied = await event.get_reply_message()
        sender = replied.sender
        await client.download_profile_photo(sender)
        await event.respond('Saved your photo {}'.format(sender.username))

client.start()
client.run_until_disconnected()



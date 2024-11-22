from telethon import TelegramClient
import python_socks
import cryptg

# Use your own values from my.telegram.org
api_id = 25448404
api_hash = '0c910748a61fc30bb14e073a31933fb6'

client = TelegramClient('anon', api_id, api_hash, proxy=(python_socks.ProxyType.SOCKS5, '127.0.0.1', 1089))

# 时间循环中向我的收藏夹发送消息
# with client:
#     client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))



async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    # print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    # username = me.username
    # print(username)
    # print(me.phone)

    # # 打印客户内所有的对话
    # async for dialog in client.iter_dialogs():
    #     print(dialog.name, 'has ID', dialog.id)

    # 发给自己
    # await client.send_message('me', 'Hello, myself!')
    # 通过聊天ID发信息
    # await client.send_message(-4571651723, 'Hello, group!')
    # 通过电话发信息
    # await client.send_message('+34600123123', 'Hello, friend!')
    # 通过用户名发消息
    # await client.send_message('@link95274', 'Testing Telethon!')

    # 发有标记的信息:
    # message = await client.send_message(
    #     'me',
    #     'This message has **bold**, `code`, __italics__ and '
    #     'a [nice website](https://example.com)!',
    #     link_preview=False
    # )

    # # Sending a message returns the sent message object, which you can use
    # print(message.raw_text)

    # 获取message对象，自己发消息自己回消息
    # message = await client.send_message('@link95274', 'Hello, myself!')
    # await message.reply('Cool!')

    # # Or send files, songs, documents, albums...
    #await client.send_file('me', 'D:\\python-project\\learnTelethon\\src\\2.jpg')

    # You can print the message history of any chat:
    async for message in client.iter_messages('me'):
        print(message.id, message.text)

        # You can download media from messages, too!
        # The method will return the path where the file was saved.
        if message.photo:
            path = await message.download_media()
            print('File saved to', path)  # printed after download is done

with client:
    client.loop.run_until_complete(main())

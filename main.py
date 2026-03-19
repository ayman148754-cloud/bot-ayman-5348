
import asyncio
from telethon import TelegramClient, events

# بيانات الحساب
client = TelegramClient('session', 35424446, '6450a3ada7217cde91ce6e09bcc17864')

@client.on(events.NewMessage(outgoing=True, pattern=r'\\.فحص'))
async def check(event):
    await event.edit("✅ السورس مستضاف وشغال!")

async def start():
    await client.start(phone='+17859102884')
    await client.run_until_disconnected()

if name == '__main__':
    asyncio.run(start())

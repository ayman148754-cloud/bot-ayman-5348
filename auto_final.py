import os

# بياناتك
USER = "ayman148754-cloud"
REPO = "bot-ayman-5348"

print("🛠️ جاري بناء سورس 'الاستضافة الذاتية'...")

# 1. ملف البوت (بدون تعقيدات name)
with open("main.py", "w") as f:
    f.write("""
import asyncio
from telethon import TelegramClient, events

# بياناتك
client = TelegramClient('session', 35424446, '6450a3ada7217cde91ce6e09bcc17864')

@client.on(events.NewMessage(outgoing=True, pattern=r'\\.فحص'))
async def check(event):
    await event.edit("✅ السورس مستضاف وشغال 100%!")

async def start_bot():
    await client.start(phone='+17859102884')
    print("🚀 BOT IS LIVE ON SERVER")
    await client.run_until_disconnected()

if name == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
""")

# 2. ملفات "الأتمتة" للاستضافة (حتى ما تسألك عن أوامر)
with open("requirements.txt", "w") as f:
    f.write("telethon\n")

with open("Procfile", "w") as f:
    f.write("worker: python main.py\n")

with open("runtime.txt", "w") as f:
    f.write("python-3.10.12\n")

# 3. الرفع التلقائي لـ GitHub
os.system(f'git config --global user.email "ayman@auto.com"')
os.system(f'git config --global user.name "{USER}"')
os.system("git init -q")
os.system("git add .")
os.system('git commit -m "auto deploy setup" -q')
os.system("git branch -M main")

print("\n📤 جاري الرفع لـ GitHub...")
os.system(f"git push https://github.com/{USER}/{REPO}.git main --force")

print("\n✅ مبروك! السورس صار جاهز للاستضافة.")

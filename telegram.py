import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

# Replace with your bot's API token
API_TOKEN = '7938210788:AAEUufFYA5VYtfOhsv5L2BpkiS1spdVyCUk'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=['start']))
async def start(message: Message):
    await message.reply("Buxoriylar maktabi BOT ga xush kelibsiz!")

async def send_notification(chat_id, message_text):
    await bot.send_message(chat_id, message_text)

async def main():
    await dp.start_polling(bot)  # Start polling directly without including dispatcher as a router

if __name__ == "__main__":
    asyncio.run(main())

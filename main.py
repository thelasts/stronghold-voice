import logging

import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)
load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer("stronghold voice initiate")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

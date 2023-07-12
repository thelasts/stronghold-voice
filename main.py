import logging

import os
from dotenv import load_dotenv

import random

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


sounds = os.listdir(os.getenv("SOUNDS_DIR"))


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer("stronghold voice initiate")


@dp.message_handler(commands=['send_voice'])
async def send_voice(message: types.Message):
    temp = 'link for your audio is ' + random.choice(sounds)
    await message.answer(temp)
    # await bot.send_voice(chat_id=message.chat.id,
    #                      voice=random.choice(sounds))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

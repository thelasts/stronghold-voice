import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

API_TOKEN = "6360260720:AAEgFrYkkH3JW5OWJvHOTcFEQPyx2-q1S3w"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer("stronghold voice initiate")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
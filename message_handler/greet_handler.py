import aiogram
from aiogram import types
from loader import *


@dp.message_handler(text='hi')
async def greet(message: types.Message):
    await message.answer('hi')


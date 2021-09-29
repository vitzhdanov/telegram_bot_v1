from aiogram.types import CallbackQuery
from data.db.db import horoscope_db

from keyboard.inline.callback_data import sign_callback

from keyboard.inline.inline_key_horoscope import choose_sign
from aiogram import types
from loader import dp, bot

from aiogram.utils.markdown import hbold, hunderline

from utils.horoscope import dict_hor


@dp.message_handler(commands='horoscope')
async def horoscope(message: types.Message):
    choose = hunderline('Выбери знак').center(22)
    await message.answer(text=choose, reply_markup=choose_sign)
    await bot.delete_message(message.chat.id, message.message_id)


@dp.callback_query_handler(sign_callback.filter())
async def callback_hor(call: CallbackQuery):
    horoscope_db(call.from_user.id, call.from_user.full_name, call.data.replace('choose:', ''))
    await call.message.answer(dict_hor[call.data.replace('choose:', '')])
    await call.message.edit_reply_markup()



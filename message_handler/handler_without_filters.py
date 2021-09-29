from random import choice

from gif_pic_other.phrase.phrase import random_phrase
from loader import dp, bot
from aiogram import types

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from aiogram.utils.callback_data import CallbackData

google_callback = CallbackData('choose', 'req')


@dp.message_handler()
async def google(message: types.Message):
    m = message.text.lower()
    if message.from_user.id == 392631263:
        await message.answer('тестер мамкин пришёл')
    if 'бот покажи' in m:
        if len(m.replace('бот покажи ', '').split()) > 1:
            phrase = m.replace('бот покажи ', '').replace(' ', '+')
        else:
            phrase = m.replace('бот покажи ', '').replace(' ', '')
        link = f'https://www.google.com/search?hl=ru&sxsrf=ALeKk002cSUdJ7BpEIz0S881b-PdTXNKLA:1616530491587&q={phrase}&' \
               f'sa=X&ved=2ahUKEwjyoeCtncfvAhWhl4sKHUImCZEQkeECKAB6BAgBEDU'

        google_callback = CallbackData('choose', 'req')

        google_key = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text='🔍', callback_data=google_callback.new(req='req'), url=link)
            ]
        ])
        await message.answer(text='😈', reply_markup=google_key)

    if 'бот засвети растамана' in m:

        link = choice(['https://vk.com/makarec','https://vk.com/steelknife23'])

        google_callback = CallbackData('choose', 'req')

        google_key = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text='🔍', callback_data=google_callback.new(req='req'), url=link)
            ]
        ])
        await message.answer(text='🍁 💨', reply_markup=google_key)
        await message.delete()

    if 'бот цель ' in message.text.lower():
        name_mes = message.text.split()[2]
        await message.answer(random_phrase(name_mes))

    if 'русский мс' in m:

        link = 'https://vk.com/meqacore'

        google_callback = CallbackData('choose', 'req')

        google_key = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text='🔍', callback_data=google_callback.new(req='req'), url=link)
            ]
        ])
        await message.answer(text='🔫 💄', reply_markup=google_key)
        await message.delete()



@dp.callback_query_handler(google_callback.filter())
async def clos_google(call: CallbackQuery):
    await call.message.edit_reply_markup()

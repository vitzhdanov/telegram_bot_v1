from aiogram import types
from datetime import datetime

date = datetime.now().strftime('%d.%m.%Y')


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('horoscope', f'Гороскоп на {date}'),
        types.BotCommand('rate', f'Курс валют на {date}'),
        types.BotCommand('weather', f'Погода на {date}')
    ])
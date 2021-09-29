from aiogram.utils import executor
from utils.horoscope import *
from utils.notify_admin import notify
from utils.set_default_command import set_default_commands
from utils.parse_rate import *
from datetime import datetime

date = datetime.now().strftime('%H:%M')


async def on_startup(dp):
    exchange_rate(rate)
    await notify(dp)
    await set_default_commands(dp)
    if date == '00:00':
        get_data()

if __name__ == '__main__':
    from message_handler import dp
    executor.start_polling(dp, on_startup=on_startup)
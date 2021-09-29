from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_data import sign_callback
choose_sign = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Овен ♈', callback_data=sign_callback.new(sign='овен')),
        InlineKeyboardButton(text='Телец ♉', callback_data=sign_callback.new(sign='телец')),
        InlineKeyboardButton(text='Близнецы ♊', callback_data=sign_callback.new(sign='близнецы')),
    ],
    [
        InlineKeyboardButton(text='Рак ♋', callback_data=sign_callback.new(sign='рак')),
        InlineKeyboardButton(text='Лев ♌', callback_data=sign_callback.new(sign='лев')),
        InlineKeyboardButton(text='Дева ♍', callback_data=sign_callback.new(sign='дева')),
     ],
    [
        InlineKeyboardButton(text='Весы ♎', callback_data=sign_callback.new(sign='весы')),
        InlineKeyboardButton(text='Скорпион ♏', callback_data=sign_callback.new(sign='скорпион')),
        InlineKeyboardButton(text='Стрелец ♐', callback_data=sign_callback.new(sign='стрелец')),
     ],
    [
        InlineKeyboardButton(text='Козерог ♑', callback_data=sign_callback.new(sign='козерог')),
        InlineKeyboardButton(text='Водолей ♒', callback_data=sign_callback.new(sign='водолей')),
        InlineKeyboardButton(text='Рыбы ♓', callback_data=sign_callback.new(sign='рыбы'))
    ]
])


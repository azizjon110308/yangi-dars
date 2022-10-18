from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton



new=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="yangilik qo'shish",callback_data="news_add"),
            InlineKeyboardButton(text="yangiliklarni ko'rish",callback_data="nevs_see"),
        ],
    ],
)

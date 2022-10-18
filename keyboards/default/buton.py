from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    [
    [KeyboardButton(text = "User info"),KeyboardButton(text = "register")],
    [KeyboardButton(text = "yangiliklar")]
    ],resize_keyboard=True
)







































cont = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="send contact",request_contact=True)]
    ],
    
)

locat = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="send locatsion",request_location=True)]
    ]
)

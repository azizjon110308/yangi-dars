from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from utils.db_api.postgresql import send_ex



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    try:

        user = send_ex(f"""INSERT INTO users_org (full_name, usernsme, user_id) 
                        VALUES ('{message.from_user.full_name}','{message.from_user.username}',{message.from_user.id}) 
                        returning *""")
        await message.answer(f"Assalomu alaykum {message.from_user.full_name} <b>botga</b> botga xush kelibsiz!\n"
                             f"Здравствуйте {message.from_user.full_name} <b>botga добро пожаловать в бот</b>!")



    except:
        await message.reply(f"Assalomu alaykum {message.from_user.full_name} bizning bazamizda borsiz\n"
                            f"Здравствуйте {message.from_user.full_name} вы в нашей базе")

from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from states.info_state import UserInfo
from aiogram.dispatcher import FSMContext
from keyboards.default.menu_key import contact,location
from aiogram.types import ContentTypes
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(text="Ro'yxatdan o'tish")
async def replyy(msg: types.Message):
    await msg.reply("Marxamat ism familiyangizni yuboring?",reply_markup=ReplyKeyboardRemove())
    await UserInfo.full_name.set()


@dp.message_handler(state=UserInfo.full_name)
async def full_n(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {"ism": name}
    )
    await message.answer("yoshingizni yuboring")
    await UserInfo.next()


@dp.message_handler(state=UserInfo.age)
async def full_a(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(
        {"yosh": age}
    )
    await message.answer("Manzilingizni yuboring",reply_markup=location)
    await UserInfo.next()


@dp.message_handler(content_types=ContentTypes.LOCATION, state=UserInfo.adress)
async def full_ad(message: types.Message, state: FSMContext):
    adress = message.location

    await state.update_data(
        {'location':adress}
    )
    await message.answer("Telefon raqam yuboring",reply_markup=contact)
    await UserInfo.next()

@dp.message_handler(content_types=ContentTypes.CONTACT, state=UserInfo.contact)
async def contact_fun(message: types.Message, state: FSMContext):
    contact_user = message.contact.phone_number
    await state.update_data(
        {'user_contact':contact_user}
    )



    info = await state.get_data()

    ism_fam = info.get("ism")
    yosh = info.get("yosh")
    manzil = info.get("manzil")
    contact = info.get('user_contact')

    await message.answer(f"Ismingiz {ism_fam}\n"
                         f"Yoshingiz {yosh}\n"
                         f"Manzilingiz {manzil}\n"
                         f"Contactingiz {contact}",reply_markup=ReplyKeyboardRemove()                         )
    await state.finish()

from aiogram.dispatcher.filters.state import State, StatesGroup



class UserInfo(StatesGroup):
    full_name = State()
    age = State()
    adress = State()








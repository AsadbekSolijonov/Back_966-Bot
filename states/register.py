from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterState(StatesGroup):
    username = State()
    phone = State()
    address = State()


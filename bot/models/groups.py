from aiogram.filters.state import StatesGroup, State


class SendMessage(StatesGroup):
    groupCategory = State()
    message = State()

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from API.categories import categories_list


def choose_btn():
    categories = categories_list()
    builder = InlineKeyboardBuilder()

    for category in categories:
        builder.add(
            InlineKeyboardButton(
                text=category['name'], callback_data=f"{category['name']}_{category['id']}"
            )
        )
    return builder.as_markup()

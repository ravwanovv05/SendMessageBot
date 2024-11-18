import logging
from aiogram import types, Bot
from aiogram.fsm.context import FSMContext
from API.groups import groups_by_category
from bot.buttons.inline_buttons.choose_category import choose_btn
from bot.models.groups import SendMessage


async def send(message: types.Message, state: FSMContext):
    await state.set_state(SendMessage.groupCategory)
    await message.answer('Choose', reply_markup=choose_btn())

async def get_category(query: types.CallbackQuery, state: FSMContext, bot: Bot):
    await state.update_data(groupCategory=query.data)
    await state.set_state(SendMessage.message)
    await bot.delete_message(query.from_user.id, message_id=query.message.message_id)
    await bot.send_message(query.from_user.id, f'Xabarni yuboring va men uni {query.data.split('_')[0]} ga yuboraman')

async def get_message(message: types.Message, state: FSMContext, bot: Bot):
    await state.update_data(message=message.text)
    data = await state.get_data()
    groups = groups_by_category(data['groupCategory'].split('_')[-1])

    try:
        for group in groups:
            await bot.send_message(group['chat_id'], data['message'])
    except Exception as e:
        logging.info(str(e))
    await state.clear()
    await message.answer('Xabar muvaffaqiyatli yuborildi!')

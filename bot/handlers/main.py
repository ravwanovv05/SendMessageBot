import logging
from aiogram import types, Bot
from API.groups import add_group


async def chat_member(update: types.ChatMemberUpdated, bot: Bot):

    if update.new_chat_member.status in ['member', 'administrator']:
        chat_id = update.chat.id
        chat_title = update.chat.title or 'Unnamed Group'

        logging.info(f'Bot added to group: {chat_title} (ID: {chat_id})')
        add_group(
            chat_title,
            chat_id,
        )

        await bot.send_message(chat_id, 'Thank you for adding me to this group!')

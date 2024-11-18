import os
import asyncio
import logging
import sys

from aiogram.filters import Command
from aiogram.handlers import MessageHandler
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from bot.handlers.main import chat_member
from bot.handlers.messages import send, get_category, get_message
from bot.models.groups import SendMessage

load_dotenv()

token = os.getenv('TOKEN')

async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    bot = Bot(token=token)
    dp = Dispatcher(bot=bot)

    dp.my_chat_member.register(chat_member)

    dp.message.register(send, Command(commands='send'))
    dp.callback_query.register(get_category, SendMessage.groupCategory)
    dp.message.register(get_message, SendMessage.message)


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())

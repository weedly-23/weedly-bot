import logging
from loguru import logger
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from weedly_bot.loader import dp
from weedly_bot.loader import api_client

logger = logging.getLogger(__name__)


main_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='📝 Добавить источники'),
                                           KeyboardButton(text='📖 Читать подписки')],
                                          [KeyboardButton(text='❓ О боте'),
                                           KeyboardButton(text='🔔 Настроить уведомления')],
                                          ], row_width=2
                                )

welcome_text = '*Это Weedly*\n\n'\
               'Как Feedly, только удобнее\n\n'\
               'Хватит залипать в рекомендательных потоках. Читай только то, что действительно важно.\n\n'\
               '*Как это работает:* \n\nПришли ссылки RSS-фидов любимых изданий и сайтов и читай их в Телеграме. '\
               'Получай последние материалы по запросу или сразу после публикации.\n\n'\
               'Можешь прислать ссылку на ютуб-канал и следить за выходящими на нем видео.\n\n'\
               'Настрой уведомления, чтобы ничего не пропустить!'


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    """первое сообщение"""
    user_id = message.from_user.id
    user_name = message.from_user.username
    api_client.users.add_user(uid=user_id, name=user_name)

    logger.debug('юзер %s нажал на старт', message.from_user.id)

    await message.answer(text=welcome_text, reply_markup=main_menu, parse_mode='Markdown')


@dp.callback_query_handler(text_contains='back_to_start')
async def start_2(call: types.CallbackQuery):

    await call.message.answer(text=welcome_text, reply_markup=main_menu, parse_mode='Markdown')

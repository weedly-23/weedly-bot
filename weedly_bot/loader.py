from dotenv import load_dotenv
import os
import logging
from yarl import URL

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from weedly_bot.api.client import ApiClient


load_dotenv('../.env')

API_TOKEN = os.getenv('API_TOKEN')
API_URL = os.getenv('API_URL')
api_client = ApiClient(URL(API_URL))


bot = Bot(token=API_TOKEN, parse_mode='Markdown')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())


# filename='my_final.log'
my_log_format = f'%(asctime)s %(name)s %(levelname)s: %(message)s'

logging.basicConfig(level=logging.DEBUG, format=my_log_format)

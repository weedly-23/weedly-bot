from dotenv import load_dotenv
import os
import logging
import logging.config
from yarl import URL

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from weedly_bot.api.client import ApiClient


load_dotenv('../.env')
API_TOKEN = os.getenv('API_TOKEN')
API_URL = os.getenv('API_URL')
print('API_TOKEN  ----', API_TOKEN)
print('API_URL  ----', API_URL)

api_client = ApiClient(URL(API_URL))


bot = Bot(token=API_TOKEN, parse_mode='Markdown')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())

logging.config.fileConfig('weedly_bot/my_logging.config')

logger = logging.getLogger(__name__)


logger.debug("test debug message")
logger.info("test info message")
logger.warning("test warning message")
logger.error("test error message")
logger.critical("test critical message")

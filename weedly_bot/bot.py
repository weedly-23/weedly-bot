from aiogram import executor
from weedly_bot.paths import dp


if __name__ == '__main__':
    executor.start_polling(dp)

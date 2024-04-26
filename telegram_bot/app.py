from .local_settings import API_KEY
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# Инициализцаия бота, диспетчера
bot = Bot(token=API_KEY, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
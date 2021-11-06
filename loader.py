from aiogram import Bot, Dispatcher, types
import os, dotenv


dotenv.load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

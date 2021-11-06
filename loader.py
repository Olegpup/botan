from aiogram import Bot, Dispatcher, types
import os, dotenv


dotenv.load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CONNECT_STR_MONGO = os.getenv("CONNECT_STR_MONGO")
DATABASE_NAME_MONGO = os.getenv("DATABASE_NAME_MONGO")

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

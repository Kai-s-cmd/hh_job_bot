import logging
from client_authorization import Auth


from tokens import TOKEN

from aiogram import Bot, Dispatcher, executor, types

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привет!\n" "Я бот для поиска работы на hh.ru!\n")


@dp.message_handler(commands=["authorization"])
async def send_auth_link(message: types.Message):
    """
    This handler will be called when user sends `/authorization` command
    """
    user_auth = Auth()
    await message.reply(
        f"Для авторизации Откройте ссылку в браузере: \n{user_auth.send_link()}"
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

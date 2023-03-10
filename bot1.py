print("hello ")
import telebot
import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6299647258:AAFCLCYpRmQVeGn-DnHRX4Mfu5mAPBxvLpA'
wikipedia.set_lang("uz")
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu alaykum wikipimedia botga xush kelisiz")
    await message.reply("Siz uzingizga muhim bo'lgan ma'lumotlaringizni qidirishingiz kerak")


@dp.message_handler()
async def sendwiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
     
    except:
        await message.answer("BUNDAY MA'LUMOT MAVJUD EMAS")





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

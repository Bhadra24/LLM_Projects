import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

# # Load .env file
# success = load_dotenv()
# print("Environment loaded:", success)


# # load_dotenv
# # API_TOKEN=os.getenv("TOKEN")
# # print(API_TOKEN)

# Load the .env file
load_dotenv()

# Fetch the TOKEN from the .env file
API_TOKEN = os.getenv("TOKEN")

# Print the API token
if API_TOKEN:
    print(f"API Token loaded successfully.")
else:
    print("Failed to load API Token. Check .env file or TOKEN environment variable.")


# Configuration
logging.basicConfig(level=logging.INFO)

# Initialize Bot and Dispatcher
bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start`or `/help`  command
    """
    await message.reply(f"Hi\nI am VTelebot24!\nPowered by Aiogram.")

@dp.message_handler(commands=['start','help'])
async def echo(message: types.Message):
    """
    This will return echo
    """
    await message.answer(message.text)






if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)
    





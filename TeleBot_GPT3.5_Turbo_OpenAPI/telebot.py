import sys
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import openai
import os


class Reference:
    '''
    A class to store previous response from the ChatGPT API

    '''

    def __init__(self) -> None:
        self.response = ""


load_dotenv()

# Fetch the TOKEN from the .env file
openai.api_key = os.getenv("OpenAI_API_KEY")
reference = Reference()

TOKEN = os.getenv("TOKEN")

# Model Name
Model_Name = "gpt-3.5-turbo"

# Initialize Bot and Dispatcher
bot=Bot(token=TOKEN)
dp=Dispatcher(bot)

def clear_past():
    '''
    A function to clear the previous conversation and context.

    '''
    reference.response=""

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """
    This handler receives messages with `/start`or `/help`  command
    """
    await message.reply(f"Hi\nI am VTelebot24!\nPowered by Aiogram.How can I assist you")


@dp.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    A handler to clear the previous conversation and context.

    """
    clear_past()
    await message.reply("I've cleared the past conversation and context.")


@dp.message_handler(commands=['help'])
async def helper(message: types.Message):
    """
    A handler to display the help menu.
    """
    help_command = """
    Hi There, I'm chatGPT Telegram bot created by Veer! Please follow these commands - 
    /start - to start the conversation
    /clear - to clear the past conversation and context.
    /help - to get this help menu.
    I hope this helps. :)
    """
    await message.reply(help_command)

@dp.message_handler()
async def chatgpt(message: types.Message):
    """
    A handler to process the user's input and generate a response using the chatGPT API.
    """
    print(f">>> USER: \n\t{message.text}")
    response = openai.ChatCompletion.create(
        model = Model_Name,
        messages = [
            {"role": "assistant", "content": reference.response}, # role assistant
            {"role": "user", "content": message.text} #our query 
        ]
    )
    reference.response = response['choices'][0]['message']['content']
    print(f">>> chatGPT: \n\t{reference.response}")
    await bot.send_message(chat_id = message.chat.id, text = reference.response)

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)

















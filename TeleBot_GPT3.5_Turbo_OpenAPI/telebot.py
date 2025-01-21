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











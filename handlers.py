from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Router 
import keyboards 

from mtranslate import translate

router = Router() 


@router.message(CommandStart()) 
async def cmd_start(message: Message):
    await message.reply('Привет, Это бот переводчик, переводит с одного языка на другой.') 


@router.message(F.text == "/help") 
async def get_help(message: Message):
    await message.reply("Введи текст, и выбери на какой язык нужно его перевести") 


@router.message() 
async def get_help(message: Message): 
    global text
    text = message.text
    await message.reply("Введи на какой язык нужно перевевсти текст", reply_markup = keyboards.main) 
    

@router.callback_query(F.data == "en")
async def en(callback: CallbackQuery): 
    global text
    await callback.message.answer(f"{translate(text, "en", "ru")}") 


@router.callback_query(F.data == "ru")
async def ru(callback: CallbackQuery): 
    global text
    await callback.message.answer(f"{translate(text, "ru", "en")}") 
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder 

main = InlineKeyboardMarkup(inline_keyboard=[  
    [InlineKeyboardButton(text="Русский", callback_data='ru')], 
    [InlineKeyboardButton(text="Англиский", callback_data='en')]])



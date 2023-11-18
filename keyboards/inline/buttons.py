from aiogram.utils.keyboard import InlineKeyboardBuilder,InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
class Format(CallbackData,prefix='ikb567'):
    choose:str
def text_format(choose=None):
    choose = 'TEXT' if choose==None else choose
    btn  = InlineKeyboardBuilder()
    btn.button(text=f"Markup format: {choose}",callback_data=Format(choose=choose))
    return btn.as_markup()
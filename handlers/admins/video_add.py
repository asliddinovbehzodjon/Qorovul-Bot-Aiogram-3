from data.config import ADMINS
from loader import dp,bot
from  aiogram import types,F
from filters import *
from aiogram.filters import Command
from keyboards.default.buttons import *
from keyboards.inline.buttons import *
from states.mystate import VideoState
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from helper import check_url
@dp.message(F.text=='🎞 Video',IsChatAdmin(),IsPrivate())
async def start_create_text_post(message:types.Message,state:FSMContext):
        await message.answer("<b>Post videosini va tekstini yuboring.</b>",reply_markup=back_button())
        await message.answer("Post sozlamalari:",reply_markup=text_format())
        await state.set_state(VideoState.video)
@dp.callback_query(Format.filter(),IsChatAdmin())
async def change_format(call:types.CallbackQuery,callback_data:Format,state:FSMContext):
    choose = 'TEXT' if callback_data.choose=='HTML' else 'HTML'
    await state.update_data({
        'choose':choose
    })
    await call.message.edit_reply_markup(reply_markup=text_format(choose))
@dp.message(F.text=='◀️ Orqaga',IsChatAdmin(),VideoState.video,IsPrivate())
async def get_add_type(message:types.Message,state:FSMContext):
    await message.answer("Qaysi turdagi xabar yuborasiz!\n"
                         "Tanlang👇",reply_markup=add_type())
    await state.clear()

@dp.message(VideoState.video,IsChatAdmin(),IsPrivate())
async def get_text(message:types.Message,state:FSMContext):
    content_type = message.content_type
    if content_type=='video':
            file_id = message.video.file_id
            caption = ''
            if message.caption:
                caption = message.caption
            await state.update_data({
                'file_id': file_id,
                'caption': caption,

            })

            text="Havolani quyidagi formatda yuborish:\n" \
                       "[tugma matni+havola]\n" \
                       "<i>Misol:\n</i>" \
                       "[Tarjimon+https://t.me/Behzod_Asliddinov]\n" \
                       "Bir qatorga bir nechta tugmalar qo'shish uchun yangi qatorga yangi havolalarni yozing.\n" \
                       "<i>Format:\n</i>" \
                       "[Birinchi matn+birinchi havola]\n" \
                       "[Ikkinchi matn+ikkinchi havola]\n"
            await message.answer_video(video=file_id,caption=caption)
            await message.answer(text,reply_markup=need_or_not())
            await state.set_state(VideoState.url)
    else:
            await message.answer("<b>Post videosini va tekstini yuboring.</b>", reply_markup=back_button())
            await message.answer("Post sozlamalari:", reply_markup=text_format())
            await state.set_state(VideoState.video)
@dp.message(F.text=="🆗 Kerakmas",VideoState.url,IsChatAdmin(),IsPrivate())
async def pass_to_url(message:types.Message,state:FSMContext):
    data = await state.get_data()
    await message.answer_video(video=data['file_id'],caption=data.get('caption'))
    await message.answer("Agar tayyor bo'lsa '📤 Yuborish' tugmasini bosing!", reply_markup=send())
    await state.set_state(VideoState.check)
# Cancel
@dp.message(F.text=="⏺ Bekor qilish",VideoState.url,IsChatAdmin(),IsPrivate())
async def pass_to_url(message:types.Message,state:FSMContext):
        await message.answer("Qaysi turdagi xabar yuborasiz!\n"
                             "Tanlang👇", reply_markup=add_type())
        await state.clear()
# Cancel 2
@dp.message(F.text=="⏺ Bekor qilish",VideoState.check,IsChatAdmin(),IsPrivate())
async def pass_to_url(message:types.Message,state:FSMContext):
        await message.answer("Qaysi turdagi xabar yuborasiz!\n"
                             "Tanlang👇", reply_markup=add_type())
        await state.clear()
@dp.message(VideoState.url,IsChatAdmin(),IsPrivate())
async def get_link(message:types.Message,state:FSMContext):
    if message.content_type=='text':
        link = message.text
        urls = check_url(link)
        urls = urls if urls else None
        await state.update_data({
            'buttons': urls
        })
        data = await state.get_data()
        links  = urls.splitlines()
        btn  = InlineKeyboardBuilder()
        for link in links:
            manzil = link[link.rfind('+') + 1:]
            manzil = manzil.strip()
            text = link[:link.rfind('+')]
            text = text.strip()
            btn.row(InlineKeyboardButton(text=text, url=manzil))
        await message.answer_video(video=data['file_id'],caption=data.get('caption',None),reply_markup=btn.as_markup(row_width=1))
        await message.answer("Agar tayyor bo'lsa '📤 Yuborish' tugmasini bosing!",reply_markup=send())
        await state.set_state(VideoState.check)
    else:
            text = "Havolani quyidagi formatda yuborish:\n" \
                   "[tugma matni+havola]\n" \
                   "<i>Misol:\n</i>" \
                   "[Tarjimon+https://t.me/Behzod_Asliddinov]\n" \
                   "Bir qatorga bir nechta tugmalar qo'shish uchun yangi qatorga yangi havolalarni yozing.\n" \
                   "<i>Format:\n</i>" \
                   "[Birinchi matn+birinchi havola]\n" \
                   "[Ikkinchi matn+ikkinchi havola]\n"
            await message.answer(text=message.text)
            await message.answer(text, reply_markup=need_or_not())
            await state.set_state(VideoState.url)
@dp.message(F.text=="📤 Yuborish",VideoState.check,IsChatAdmin(),IsPrivate())
async def check_post(message:types.Message,state:FSMContext):
    data = await state.get_data()
    type = data['send']
    from api import get_users, get_groups
    USERS = get_users() if type == 'user' else get_groups()
    if data.get('buttons',None):
        links = data['buttons'].splitlines()
        btn = InlineKeyboardBuilder()
        for link in links:
            manzil = link[link.rfind('+') + 1:]
            manzil = manzil.strip()
            text = link[:link.rfind('+')]
            text = text.strip()
            btn.row(InlineKeyboardButton(text=text,url=manzil))
        caption = data.get('caption', None)
        video = data['file_id']
        counter = 0
        for i in USERS:
            try:
                await bot.send_video(video=video,chat_id=i['telegram_id'], caption=caption,reply_markup=btn.as_markup(row_width=1))
                counter += 1
            except:
                pass
        await message.answer(f"{counter} kishiga xabar yuborildi!", reply_markup=admin_button())
    else:
        caption = data.get('caption',None)
        video = data['file_id']
        counter = 0
        for i in USERS:
            try:
                await bot.send_video(video=video, chat_id=i['telegram_id'],caption=caption)
                counter+=1
            except:
                pass
        await message.answer(f"{counter} kishiga xabar yuborildi!",reply_markup=admin_button())
    await state.clear()

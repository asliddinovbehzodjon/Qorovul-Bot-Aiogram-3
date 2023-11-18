from aiogram.filters.state import State,StatesGroup
class TextState(StatesGroup):
    text = State()
    url = State()
    check = State()
class ImageState(StatesGroup):
    image = State()
    url = State()
    check = State()
class VideoState(StatesGroup):
    video = State()
    url = State()
    check = State()

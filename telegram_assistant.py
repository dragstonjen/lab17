
from aiogram import Bot, Dispatcher, types, executor
from assistant import Assistant

API_TOKEN = '7599593056:AAGmUNWwGyFmxXb6k9JxR41hBIsbBml9MCA'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
assistant = Assistant()
temp_data = {}

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("/add /list /search")

@dp.message_handler(commands=['add'])
async def add_note_start(message: types.Message):
    temp_data[message.from_user.id] = 'awaiting_note'
    await message.reply("Введіть нотатку:")

@dp.message_handler(commands=['list'])
async def list_notes(message: types.Message):
    notes = assistant.list_notes()
    await message.reply("\n".join(notes) if notes else "Немає нотаток.")

@dp.message_handler(commands=['search'])
async def search_start(message: types.Message):
    temp_data[message.from_user.id] = 'awaiting_search'
    await message.reply("Введіть ключове слово:")

@dp.message_handler()
async def handle_text(message: types.Message):
    uid = message.from_user.id
    if temp_data.get(uid) == 'awaiting_note':
        assistant.add_note(message.text)
        temp_data.pop(uid)
        await message.reply("Нотатку додано.")
    elif temp_data.get(uid) == 'awaiting_search':
        results = assistant.search_notes(message.text)
        temp_data.pop(uid)
        await message.reply("\n".join(results) if results else "Нічого не знайдено.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

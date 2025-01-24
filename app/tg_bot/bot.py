from aiogram import Bot, Dispatcher
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message
from back.services import check_imei
from utility import is_valid_imei
from db.models import find_by_telegram_id
from config import settings
import asyncio

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

class IMEIStates(StatesGroup):
    waiting_for_imei = State()

@dp.message(Command('start'))
async def command_start(message: Message, state: FSMContext):
    '''
    Обрабатывает команду /start от пользователя.
    '''
    user_id = message.from_user.id
    user_in_db = await find_by_telegram_id(user_id)
    if user_in_db:
        await message.answer("Добро пожаловать! Пожалуйста, отправьте ваш IMEI для проверки.")
        await state.set_state(IMEIStates.waiting_for_imei)
    else:
        await message.answer("Вы не зарегистрированы. Обратитесь к администратору.")
    
@dp.message(IMEIStates.waiting_for_imei)
async def process_imei(message: Message, state: FSMContext):
    '''
    Обрабатывает отправленный пользователем IMEI.
    '''
    imei = message.text
    # is_valid_imei(imei)
    if not is_valid_imei(imei):
        await message.answer("Неверный IMEI. Попробуйте снова.")
    else:
        result = await check_imei(imei)
        if result:
            await message.reply(f"Информация об IMEI:\n{result}")
        else:
            await message.reply("Ошибка при проверке IMEI.")
    
async def main():
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())
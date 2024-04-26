from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import *
from .app import dp, bot
from . import messages as msg
from .local_settings import DB_DIRECTORY, BASE_API_URL
import sqlite3
import requests
import json
import asyncio


class Auth(StatesGroup):
    user_found = State()

# Настройки базы данных
TIMEOUT_DELAY = 100

@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    """
    Стартовая команда (/start) - авторизация
    """
    await message.answer(msg.start_message(msg=message))
    await state.set_state(Auth.user_found)

@dp.message(Auth.user_found)
async def logining(message: Message, state: FSMContext):
    """
    Авторизация через логин.
    Проверка на существование такого логина в базе данных.
    """
    
    check_login = 0

    with sqlite3.connect(DB_DIRECTORY, timeout=TIMEOUT_DELAY) as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT COUNT(*) FROM auth_user WHERE username = ?", (message.text,))
        check_login = cursor.fetchone()[0]

    # Если такого логина нет - ошибка
    if check_login == 0:
        await message.reply(msg.LOGINING_FAILED)
        await state.set_state(Auth.user_found)
    
    else:
            
        await message.answer(msg.LOGINING_SUCCESSFULY)

        async def work_check() -> None:
            url = BASE_API_URL

            while True:
                try:
                    response = requests.get(url=url).text
                    
                    response = json.loads(response)

                    for object in response:
                        with sqlite3.connect(DB_DIRECTORY, timeout=TIMEOUT_DELAY) as connect:
                            cursor = connect.cursor()
                            cursor.execute("SELECT id FROM auth_user WHERE username = ?", (message.text, ))

                            if object['student_id'] == cursor.fetchone()[0]:

                                if object['status'] == "Accepted":
                                    await bot.send_message(chat_id=message.chat.id, text=msg.work_accepted(msg=object['work_name']))
                                    requests.delete(url=(BASE_API_URL + str(object["id"])) + "/")

                                elif object['status'] == "Rejected":
                                    await bot.send_message(chat_id=message.chat.id, text=msg.work_rejected(msg=object['work_name']))
                                    requests.patch(url=(BASE_API_URL + str(object["id"])) + "/", data={"status": ""})
                except:
                    pass
                
                await asyncio.sleep(500)
        
        await work_check()
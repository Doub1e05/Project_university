from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import *
from .app import dp, bot
from . import messages as msg
from .local_settings import BASE_API_URL
import sqlite3
import requests
import json
import asyncio


class Auth(StatesGroup):
    authorizhation = State()
    work_status_message = State()




@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    """
    Стартовая команда (/start) - авторизация
    """
    await message.answer(msg.start_message(msg=message))
    await state.set_state(Auth.authorizhation)

@dp.message(Auth.authorizhation)
async def authorizhation(message: Message, state: FSMContext):
    """
    Авторизация через логин и пароль
    """


    try:
        data = {"login": f"{message.text.split()[0]}", 
                "password": f"{message.text.split()[1]}"}
    except:
        data = {}

    responce = requests.post(url='http://127.0.0.1:8000/api/login', data=data)

    if responce.status_code == 200:
        await message.answer(msg.LOGINING_SUCCESSFULY)
        global user
        user = message.text.split()[0] 
        await state.set_state(Auth.work_status_message)
        asyncio.create_task(work_status_message(message))

    else:
        await message.reply(msg.LOGINING_FAILED)


async def work_status_message(message: Message):
    '''
    Ожидание изменений о статусах лабораторных работ определённого пользователя
    '''

    global user

    url = BASE_API_URL

    while True:
        try:
            response = requests.get(url=url).text
            
            response = json.loads(response)

            for objects in response:
                if objects['student']['login'] == user:

                    if objects['status'] == "Accepted":
                        await bot.send_message(chat_id=message.chat.id, text=msg.work_accepted(msg=objects['work']['work_name']))
                        requests.delete(url=(BASE_API_URL + str(objects["id"])) + "/")

                    elif objects['status'] == "Rejected":
                        await bot.send_message(chat_id=message.chat.id, text=msg.work_rejected(msg=objects['work']['work_name']))
                        requests.patch(url=(BASE_API_URL + str(objects["id"])) + "/", data={"status": ""})
        except:
            pass
        
        await asyncio.sleep(500)

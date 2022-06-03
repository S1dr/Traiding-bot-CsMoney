import json
import time
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from main import collect_data
from aiogram.utils.markdown import hbold, hlink
import sqlite3

token = ''

bot = Bot(token= token, parse_mode=types.ParseMode.HTML)


dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def welcome_message(message: types.Message):

    #создаем базу данных и при команде старт добавляем id
    def sql_start():
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
            id INTEGER
        )""")

        connect.commit()
        # добавление данных

        people_id = message.chat.id
        cursor.execute(f"SELECT id FROM login_id WHERE id ={people_id}")

        data = cursor.fetchone()

        if data is None:
            user_id = [message.chat.id]
            cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
            connect.commit()

    await bot.send_message(chat_id=message.chat.id, text=f'Привет,{message.from_user.full_name}.✌\n'
                                                         f'Давай попробуем подыскать тебе что-нибудь на Cs.money по вкусной цене 💰\n')




    sql_start()




    start_buttons = ['Ножи 🔪', 'Перчатки 🖖', 'Пистолеты🔫', 'Пист.пулемёты', 'Винтовки 🍼', 'AWP ☢', 'Дробаши ❌', 'Пулемёты🔭', 'Ключи 🔑' ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('Выберите категорию', reply_markup= keyboard)

    await message.answer('Я буду искать вещи со скидкой в -25%')






# хендлер и функция позволяющая удалить пользоватеся из базы данных самому
@dp.message_handler(commands='delete')
async def delete_user(message: types.Message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    people_id = message.chat.id

    cursor.execute(f"DELETE FROM login_id WHERE id = {people_id}")
    connect.commit()

    #delite from table



#Хендлер для ножей

@dp.message_handler(Text(equals='Ножи 🔪'))
async def get_discount_knives(message:types.Message):
    await message.answer('Пожалуйста подождите...')

    collect_data(cat_type=2 , min=500 , max=800)

    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")} %\n' \
            f'{hbold("Цена: ")}${item.get("item_price")}'

        if index % 20 == 0:
            await message.answer('Что бы нас не заподозрели, сделаю перерыв 3 секунды!')
            time.sleep(3)



        await message.answer(card)

#хендлер для перчаток

@dp.message_handler(Text(equals='Перчатки 🖖'))
async def get_discount_knives(message:types.Message):
    await message.answer('Пожалуйста подождите...')

    collect_data(cat_type=13 , min=500 , max=2000)

    with open('result.json') as file:
        data = json.load(file)

    for index , item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")} %\n' \
            f'{hbold("Цена: ")}${item.get("item_price")}'

        if index % 20 == 0 and index > 10:
            await message.answer('Что бы нас не заподозрели, сделаю перерыв 3 секунды!')
            time.sleep(3)



        await message.answer(card)





#хендлер для пистолетов


@dp.message_handler(Text(equals='Пистолеты🔫'))
async def get_discount_knives(message:types.Message):
    await message.answer('Пожалуйста подождите...')

    collect_data(cat_type=5, min=20 , max=30)

    with open('result.json') as file:
        data = json.load(file)

    for index , item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")} %\n' \
            f'{hbold("Цена: ")}${item.get("item_price")}'

        if index % 20 == 0 and index > 10:
            await message.answer('Что бы нас не заподозрели, сделаю перерыв 3 секунды!')
            time.sleep(3)



        await message.answer(card)


#хендлер для пистолетов Пистолеты-пулемёты


@dp.message_handler(Text(equals='Пист.пулемёты'))
async def get_discount_knives(message:types.Message):
    await message.answer('Пожалуйста подождите...')

    collect_data(cat_type=6, min=5 , max=10)

    with open('result.json') as file:
        data = json.load(file)

    for index , item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")} %\n' \
            f'{hbold("Цена: ")}${item.get("item_price")}'

        if index % 20 == 0 and index > 10:
            await message.answer('Что бы нас не заподозрели, сделаю перерыв 3 секунды!')
            time.sleep(3)



        await message.answer(card)




#хендлер для штурмовых винтовок


@dp.message_handler(Text(equals='Винтовки 🍼'))
async def get_discount_knives(message:types.Message):
    await message.answer('Пожалуйста подождите...')

    collect_data(cat_type=3, min=300 , max=500)

    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")} %\n' \
            f'{hbold("Цена: ")}${item.get("item_price")}'

        if index % 20 == 0 and index > 10:
            await message.answer('Что бы нас не заподозрели, сделаю перерыв 3 секунды!')

            time.sleep(3)

        await message.answer(card)





#хендлер для снайперских винтовок


@dp.message_handler(Text(equals='AWP ☢'))
async def get_discount_knives(message:types.Message):
    await message.answer('Пожалуйста подождите...')

    collect_data(cat_type=4 , min=300 , max=500)

    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")} %\n' \
            f'{hbold("Цена: ")}${item.get("item_price")}'

        if index % 20 == 0 and index > 10:
            await message.answer('Что бы нас не заподозрели, сделаю перерыв 3 секунды!')

            time.sleep(3)

        await message.answer(card)


# хелдлер для дробовиков


@dp.message_handler(Text(equals='Дробаши ❌'))
async def get_discount_knives(message:types.Message):
    await message.answer('Пожалуйста подождите...')

    collect_data(cat_type=7, min=50 , max=80)

    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")} %\n' \
            f'{hbold("Цена: ")}${item.get("item_price")}'

        if index % 20 == 0 and index > 10:
            await message.answer('Что бы нас не заподозрели, сделаю перерыв 3 секунды!')

            time.sleep(3)

        await message.answer(card)

# хендлер для пулеметов


@dp.message_handler(Text(equals='Пулемёты🔭'))
async def get_discount_knives(message:types.Message):
    await message.answer('Пожалуйста подождите...')

    collect_data(cat_type=8 , min=3 , max=8)

    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")} %\n' \
            f'{hbold("Цена: ")}${item.get("item_price")}'

        if index % 20 == 0 and index > 10:
            await message.answer('Что бы нас не заподозрели, сделаю перерыв 3 секунды!')

            time.sleep(3)

        await message.answer(card)


#хендлер для ключей

@dp.message_handler(Text(equals='Ключи 🔑'))
async def get_discount_knives(message:types.Message):
    await message.answer('Пожалуйста подождите...')

    collect_data(cat_type=1)

    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")} %\n' \
            f'{hbold("Цена: ")}${item.get("item_price")}'

        if index % 20 == 0 and index > 10:
            await message.answer('Что бы нас не заподозрели, сделаю перерыв 3 секунды!')

            time.sleep(3)

        await message.answer(card)




#def main():
executor.start_polling(dp)
#
# if __name__ == '__main__':
#     main()


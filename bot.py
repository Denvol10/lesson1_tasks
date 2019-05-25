from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
import time

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

# Создадим функцию greet_user
def greet_user(bot, update): # bot - экземпляр нашего бота, с помощью него даем команды, update - сообщение от telegram
    text = 'Данный бот предназначен для вывода информации о текущем положении планет\
    введите команду в формате /planet "название планеты на английском", например\
    /planet Mars'
    print(text)
    update.message.reply_text(text)

# Создаем функцию talk_to_me:
def talk_to_me(bot, update):
    user_text = 'Привет {}! Ты написал: {}'.format(update.message.chat.first_name, update.message.text)
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username,
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

# Создадим функцию, которая показывает в каком созвездии находится планета, используя модуль ephem
def constell_panet(bot, update):
    planet = update.message.text.split()[-1]
    now_date = time.strftime('%Y/%m/%d')
    print(planet, now_date)
    if planet == 'Mercury':
        ep_planet = ephem.Mercury(now_date)
    elif planet == 'Venus':
        ep_planet = ephem.Venus(now_date)
    elif planet == 'Mars':
        ep_planet = ephem.Mars(now_date)
    elif planet == 'Jupiter':
        ep_planet = ephem.Jupiter(now_date)
    elif planet == 'Saturn':
        ep_planet = ephem.Saturn(now_date)
    elif planet == 'Uranus':
        ep_planet = ephem.Uranus(now_date)
    elif planet == 'Neptune':
        ep_planet = ephem.Neptune(now_date)
    else:
        print('Ввод неверный')
    const = ephem.constellation(ep_planet)
    print(const)
    user_text_const = f'Планета {planet} сегодня находится в созвездии {const}'
    print(user_text_const)
    update.message.reply_text(user_text_const)


# Тело бота, объявляем функцию main()
def main():
    # создаем переменную для взаимодействия с ботом
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    # текст в логе при запуске бота
    logging.info('Bot starts')

    # создание объекта принимающие входящие сообщения и передающий их дальше (обработчик команд)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user)) # 'start' - команда в telegram, greet_user - название функции (любое)

    # добавление команды в бота, которая принимает на вход название планеты
    dp.add_handler(CommandHandler('planet', constell_panet))

    # хэндлер для перехвата текстовых сообщений пользователя
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    # обращаться к телеграмм и проверять наличие сообщений
    mybot.start_polling()

    # mybot будет работать до принудительной остановки
    mybot.idle()

# делаем вызов функции main(), запускаем бота
main()
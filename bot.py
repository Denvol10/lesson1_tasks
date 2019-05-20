from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

# Настройка прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

# Создадим функцию greet_user
def greet_user(bot, update): # bot - экземпляр нашего бота, с помощью него даем команды, update - сообщение от telegram
    text = 'Starting / start'
    print(text)
    update.message.reply_text(text)

# Создаем функцию talk_to_me:
def talk_to_me(bot, update):
    user_text = 'Привет {}! Ты написал: {}'.format(update.message.chat.first_name, update.message.text)
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username,
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

# Тело бота, объявляем функцию main()
def main():
    # создаем переменную для взаимодействия с ботом
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    # текст в логе при запуске бота
    logging.info('Bot starts')

    # создание объекта принимающие входящие сообщения и передающий их дальше (обработчик команд)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user)) # 'start' - команда в telegram, greet_user - название функции (любое)

    # хэндлер для перехвата текстовых сообщений пользователя
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    # обращаться к телеграмм и проверять наличие сообщений
    mybot.start_polling()

    # mybot будет работать до принудительной остановки
    mybot.idle()

# делаем вызов функции main(), запускаем бота
main()
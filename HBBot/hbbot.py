import telebot
import shelve
import datetime
from collections import defaultdict
from threading import Timer
'''Токен'''
bot = telebot.TeleBot('931797065:AAE0aqI1Wpb4Zy6WqQfrQrU31XnUc_HJ84I')
ADD, NAME, DATE, CONFIRMATION, DELETE_USER = range(5)
BIRTHDAY_DATA = dict()

'''взаимодействие с ботом'''
@bot.message_handler(commands=['start']) #Декоратор
def message_start(message): #Реакция на начальное конкретное сообщение
    bot.send_message(message.chat.id, 'Привет, я бот, созданный для напоминания о днях рождения,\
    воспользуйся командой /add для того, чтобы начать добавлять людей или /help, чтобы узнать как мной пользоваться.\n \n \n \
    ✨✨✨POWERED BY @Alexey_Horbunov✨✨✨')
'''инструкция'''
@bot.message_handler(commands=['help'])
def help_function(message):
    bot.send_message(message.chat.id, \
    '🚀 Это бот, созданный для того, чтобы напоминать людям о днях рождения своих коллег/одногруппников, одноклассников и т.д.'\
    'в чате, в котором они находятся. Для начала один человек должен внести весь список участников чата с помощью команды /add-'\
    ' для начала имя и фамилию, а потом дату. Бот будет отправлять в чат группы сообщение о об именнинниках.' \
    ' Также есть функция delete, которая позволяет удалить дату рождения пользователя из базы бота с помощью команды /delete.'\
    ' Вместе с этим можно просмотреть все данные с помощью команды /see\n'\
    '✨В случае появления каких-либо вопросов обращаться к Алексею @Alexey_Horbunov ✨')

'''удаление записи'''
@bot.message_handler(commands=['delete'])
def message_delete_user1(message):
    bot.send_message(message.chat.id, text = '⏩Введите дату, которую хотите удалить вместе с пользователями из базы данных бота.' \
    ' Введите дату в формате "число-месяц".'\
    'Например, у человека день рождения 8 июня, нужно написать "08-06"')
    update_state(message, DELETE_USER)

'''просмотр всей базы'''
@bot.message_handler(commands=['see'])
def message_see(message):
    bot.send_message(message.chat.id, text = format(BIRTHDAY_DATA))


@bot.message_handler(func = lambda message: get_state(message) == DELETE_USER)
def message_delete_user2(message):
    update_object(message.chat.id, 'date', message.text)
    object = get_object(message.chat.id)
    for key in object:
        if object[key] in BIRTHDAY_DATA:
            del BIRTHDAY_DATA[object[key]]
            bot.send_message(message.chat.id, text = '✔Удалено')
        else:
            bot.send_message(message.chat.id, text = '❌Дней рождений у людей с такой датой нет. Попробуй сначала: /delete')
        update_state(message, ADD)

'''процесс добавления'''
@bot.message_handler(func = lambda message: get_state(message) == ADD)
def handle_message(message):
    bot.send_message(message.chat.id, text = '⏩Введите имя и фамилию')
    update_state(message, NAME)

@bot.message_handler(func = lambda message: get_state(message) == NAME)
def handle_name(message):
    update_object(message.chat.id, 'name', message.text)
    bot.send_message(message.chat.id, text = '⏩Введите дату в формате "число-месяц".\
    Например, у человека день рождения 8 июня, нужно написать "08-06"')
    update_state(message, DATE)

@bot.message_handler(func = lambda message: get_state(message) == DATE)
def handle_date(message):
    update_object(message.chat.id, 'date', message.text)
    object = get_object(message.chat.id)
    bot.send_message(message.chat.id, text='Все верно? {}'.format(object))
    update_state(message, CONFIRMATION)

@bot.message_handler(func = lambda message: get_state(message) == CONFIRMATION)
def handle_date(message):
    if 'да' in message.text.lower():
        object = get_object(message.chat.id)
        help_list = [object]
        for i in help_list:
            if i['date'] not in BIRTHDAY_DATA:
                BIRTHDAY_DATA[i['date']] = [i['name']]
            else:
                BIRTHDAY_DATA[i['date']].append(i['name'])
        bot.send_message(message.chat.id, text='✅Записано✅'.format(object))
        update_state(message, ADD)
    if 'нет' in message.text.lower():
        bot.send_message(message.chat.id, text='❌Попробуйте снова, нажмите /add')
        update_state(message, ADD)
    object.clear()
    '''обновление и поздравление'''
    def timed_job():
        Timer(1800, timed_job).start()
        for key in BIRTHDAY_DATA.keys():
            if key == datetime.datetime.now().strftime('%d-%m'):
                for data in BIRTHDAY_DATA[key]:
                    bot.send_message(message.chat.id, text = data + ' сегодня именнинник(ца), поздравляем))))')
    timed_job()



''''состояния ввода'''
USER_STATE = defaultdict(lambda: ADD)


def get_state(message):
    return USER_STATE[message.chat.id]


def update_state(message, state):
    USER_STATE[message.chat.id] = state

'''сохранение информации'''
ALLDATA = defaultdict(lambda: {})

def update_object(user_id, key, value):
    ALLDATA[user_id][key] = value

def get_object(user_id):
    return ALLDATA[user_id]



bot.polling() #Чтобы не закрывался и проверял сообщения

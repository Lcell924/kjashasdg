import telebot
from telebot import types

bot = telebot.TeleBot("8721708217:AAEF_QS-mJeeMhgZsTUxa3YCSuY1jVLDO_U")

@bot.message_handler(commands = ['sites'])
def send_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://t.me/otzivi_meruw'))
    bot.reply_to(message, 'переходи в отзывы', reply_markup=markup)

@bot.message_handler(commands=['start', 'main', 'hello'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')

@bot.message_handler(commands=['go'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Чтобы начать сотрудничество, отправьте «+» одному из менеджеров @Avito_Grig @Alex_meneegerr')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, '<b>По всем вопросам к разработчику </b>  <em><u> @Flow3z </u></em>', parse_mode='HTML')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')
    elif message.text.lower() == "id":
        bot.reply_to(message, f'ID: {message.from_user.id}')

bot.polling(none_stop=True)



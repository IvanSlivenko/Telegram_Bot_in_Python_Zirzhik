import telebot

import const

bot = telebot.TeleBot(str(const.APY_TOKEN))

# Варіанти реакцій на :

# 1 команди типу  /start /help /some
# 2 текст
# Булеві значення
# Типи повідомлень


@bot.message_handler(commands=['start'])
def start_handler(message):
    # print(dir(message.chat))
    bot.send_message(
        message.chat.id,
        f"{message.chat.first_name or ''} ,  Дякуюємо, що вибрали наш сервіс"
    )

bot.infinity_polling()
import os
from django.core.management.base import BaseCommand
from telebot import TeleBot, types

from users.models import User

bot = TeleBot(os.getenv('TG_API'))


@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.InlineKeyboardButton("Start", callback_data='start')
    item2 = types.InlineKeyboardButton("Stop", callback_data='stop')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Hi! I am a tracker of your habits! '
                                      'Press the "Start" button to start me.'
                                      'Press the "Stop" button to shut me down :(',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            chat_id = call.message.chat.id
            if call.data == 'start':
                user = User.objects.filter(username=call.message.chat.username).first()
                if user:
                    user.chat_id = chat_id
                    user.is_sub = True
                    user.save()
                    bot.send_message(chat_id, "Let's start!")

                else:
                    bot.send_message(chat_id, "You have to register first")

            elif call.data == 'stop':
                user = User.objects.filter(chat_id=chat_id).first()
                if user:
                    user.is_sub = False
                    user.save()
                    bot.send_message(chat_id, "See you next time")
                else:
                    bot.send_message(chat_id, "You wasn't registered")

    except Exception as e:
        print(repr(e))


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        print('The application is running')
        bot.polling(none_stop=True)

import os
from datetime import datetime
from telebot import TeleBot
from celery import shared_task

from habits.models import Habit


bot = TeleBot(os.getenv('TG_API'))


@shared_task
def send_message():

    current_time = datetime.now().time()
    habit_list = Habit.objects.filter(time=current_time)

    for habit in habit_list:
        user = habit.user
        chat_id = user.chat_id
        if chat_id:
            try:
                message = f'It is time ({habit.time}) to {habit.action}! ' \
                          f'{habit.location} is the place to do it'
                bot.send_message(chat_id, message, parse_mode="Markdown")

            except Exception:
                raise Exception  # Можно добавить отправку сообщения об ошибке

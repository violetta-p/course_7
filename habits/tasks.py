import os
from datetime import datetime
import telepot
from celery import shared_task

from habits.models import Habit


@shared_task
def send_message(request):
    token = os.getenv('TG_API')
    tg_bot = telepot.Bot(token)
    tg_bot.getMe()
    response = tg_bot.getUpdates()
    chat_id = int(response['result'][0]['message']['chat']['id'])

    current_time = datetime.now().time()
    habit_list = Habit.objects.filter(user=request)

    for habit in habit_list:
        if habit.time == current_time:
            try:
                message = f'It is time ({habit.time}) to {habit.action}! ' \
                          f'({habit.location} is the best place to do it)'
                tg_bot.sendMessage(chat_id, message, parse_mode="Markdown")
            except Exception:
                raise Exception  # Можно добавить отправку сообщения об ошибке админу

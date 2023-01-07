import requests

from telebot.models import TeleSettings


def send_telegram(telegram_name, telegram_phone):
    settings = TeleSettings.objects.get(pk=1)
    token = str(settings.telegram_token)
    chat_id = str(settings.telegram_chat_id)
    text = str(settings.telegram_message)

    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    part_first = text[0:text.find('{')]
    part_second = text[text.find('}')+1:text.rfind('{')]
    part_last = text[text.rfind('}'):-1]

    text_slise = part_first + telegram_name + part_second + telegram_phone + part_last

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text_slise,
    })

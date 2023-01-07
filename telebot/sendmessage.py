import requests

from telebot.models import TeleSettings


def send_telegram(telegram_name, telegram_phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.telegram_token)
        chat_id = str(settings.telegram_chat_id)
        text = str(settings.telegram_message)

        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            part_first = text[0:text.find('{')]
            part_second = text[text.find('}') + 1:text.rfind('{')]
            part_last = text[text.rfind('}'):-1]

            text_slise = part_first + telegram_name + part_second + telegram_phone + part_last
        else:
            text_slise = text

        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slise,
            })
        except:
            pass
        finally:
            if req.status_code != 200:
                print('Ошибка отправки')
            elif req.status_code == 500:
                print('Ошибка сервера')
            else:
                print('Сообщение отправлено')

    else:
        pass

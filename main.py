import requests
import time


API_URL = 'https://api.telegram.org/bot'
API_CATS_URL = 'https://randomfox.ca/floof/'
BOT_TOKEN = '6497527683:AAH4QJxKPs-3WHG1pw4APrsJSmUoLcI1Vu4'
ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('

offset = -2
counter = 0
cat_response: requests.Response
cat_link: str


while True:
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    response = requests.get(f'https://randomfox.ca/floof/')
    print(response.text)
    if updates['result']:
        for result in updates['result']:
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()['image']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')


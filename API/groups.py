import os
from http.client import responses

import requests
from dotenv import load_dotenv

load_dotenv()


def add_group(title: str, chat_id: int):
    url = os.getenv('ADD_GROUP')
    response = requests.post(url, data={'title': title, 'chat_id': chat_id})
    if response.status_code == 201:
        return response.json()


def groups_by_category(category_id):
    url = os.getenv('GROUPS_BY_CATEGORY') + '/' + str(category_id)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
import os
from http.client import responses

import requests
from dotenv import load_dotenv

load_dotenv()

def categories_list():
    url = os.getenv('CATEGORIES_LIST')
    respone = requests.get(url)
    return respone.json()

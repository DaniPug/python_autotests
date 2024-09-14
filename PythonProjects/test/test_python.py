import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '85a09ff54faad8634829af5579531f45'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '10152'

def test_statud_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Test PY' 

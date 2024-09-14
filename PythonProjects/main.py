import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '85a09ff54faad8634829af5579531f45'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}


'''BODY_REGISTRATION = {
    "trainer_token": TOKEN,
    "email": "dani.dubovitii@yandex.ru",
    "password": "Iloveqa123"
}
BODY_CONFIRM = {
    "trainer_token": TOKEN
}'''

''' RESPONS = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = BODY_REGISTRATION)
print(RESPONS.text) '''

'''RESPONS_CONFIRM = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = BODY_CONFIRM)
print(RESPONS_CONFIRM.text)'''

BODY_CREATE_POKEMON = {
    "name": "DOOD",
    "photo_id": 892
}

RESPONS_CREATE_POKEMON = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CREATE_POKEMON) 
'''создали покемона'''
print(RESPONS_CREATE_POKEMON.text) 
'''отобразили инфо ответа строки сверху'''

POKEMON_ID = RESPONS_CREATE_POKEMON.json()['id'] 
'''создали переменную для, в которую падает параметр ранее созданнго покемона'''



BODY_CHANGE_NAME = {
    "pokemon_id": POKEMON_ID,
    "name": "Dood",
    "photo_id": 892
}

RESPONS_CHANGE_NAME = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CHANGE_NAME) 
'''поменяли имя созданному покемону'''
print(RESPONS_CHANGE_NAME.text)
'''отобразили инфо ответа строки сверху'''



BODY_ADD_POKEBALL = {
    "pokemon_id": POKEMON_ID
}

RESPONS_ADD_POKEBALL = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_ADD_POKEBALL)
'''поймали созданного покемона в покебол'''
print(RESPONS_ADD_POKEBALL.text)
'''отобразили инфо ответа строки сверху'''
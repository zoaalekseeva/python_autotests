import requests 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3818743017f95bd8f67b6ae7f9b1b1cd'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '37096'


body_registration = {
    "trainer_token": TOKEN,
    "email": "mail",
    "password": "pass"
}
body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "хрум",
    "photo_id": 492
}

body_transform = {
    "pokemon_id": "299660",
    "name": "пуньк",
    "photo_id": 613
}

body_poceball = {
    "pokemon_id": "299680"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json =body_create)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json =body_create)
print(response_create.text)'''

'''response_transform = requests.put(url = f'{URL}/pokemons', headers = HEADER, json =body_transform)
print(response_transform.text)'''

'''response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json =body_poceball)
print(response_pokeball.text)'''

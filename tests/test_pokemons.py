import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3818743017f95bd8f67b6ae7f9b1b1cd'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '37096'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons',params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons',params = {'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'пуньк'

@pytest.mark.parametrize('key, value',[('name','пуньк'),('trainer_id', TRAINER_ID),('id', "299680")])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons',params = {'trainer_id':TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value

def test_trainer():
    response_trainer = requests.get(url = f'{URL}/trainers',params = {'city':'Москва'})
    assert response_trainer.status_code == 200

def test_name():
    response_name = requests.get(url = f'{URL}/trainers',params = {'trainer_id':TRAINER_ID})
    assert response_name.json()["data"][0]["trainer_name"] == 'Kread'
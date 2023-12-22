import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = 'cb6a56a45ae7e45317d5aeb17da939de'
def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainers_id': 3445})
    assert response.status_code == 200
    
def test_place_body():
    response = requests.get(f'{host}/trainers', params={'trainer_id': 3445})
    assert response.json()['trainer_name'] == 'Noname'
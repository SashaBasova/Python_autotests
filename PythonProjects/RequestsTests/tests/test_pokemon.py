import requests
import pytest

def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200

def test_string():
    response = requests.get('https://pokemonbattle.me:5000/trainers', params={'trainer_id' : '1332'})
    assert response.json()['trainer_name'] == 'Sasha`s'   

def test_part_of_body():
    response = requests.get('https://pokemonbattle.me:5000/pokemons', params={'pokemon_id' : '1664'})
    assert response.json()['name'] == 'МегаПокемон'
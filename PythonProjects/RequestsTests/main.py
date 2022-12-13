import requests

token = '30a39ea4d4a8c356a1660c4d81337143'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "name": "Сосисочка",
    "photo": "https://purepng.com/public/uploads/large/purepng.com-pokemonpokemonpocket-monsterspokemon-franchisefictional-speciesone-pokemonmany-pokemonone-pikachu-1701527786833pqvld.png"
})
print(response.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    "pokemon_id": 1663,
    "name": "Sosisochka",
    "photo": "https://purepng.com/public/uploads/large/purepng.com-pokemonpokemonpocket-monsterspokemon-franchisefictional-speciesone-pokemonmany-pokemonone-pikachu-1701527786833pqvld.png"
})
print(response_put.text)

response_pokeball = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token' : token}, json={
    "pokemon_id": "1663"
})
print(response_pokeball.text)

response_put_1664 = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    "pokemon_id": 1664,
    "name": "МегаПокемон",
    "photo": "https://www.nicepng.com/png/full/62-622403_-.png"
})
print(response_put_1664.text)

response_pokeball_1664 = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token' : token}, json={
    "pokemon_id": "1664"
})
print(response_pokeball_1664.text)
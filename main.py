import requests

trainer_token = "cb6a56a45ae7e45317d5aeb17da939de"

post_pokemons = requests.post('https://api.pokemonbattle.me:9104/pokemons', json = {
    "name": "generate",
    "photo": "generate"
},
headers={"Content-Type":"application/json", "trainer_token":trainer_token})

print(post_pokemons.text)

patch_pokemons = requests.patch('https://api.pokemonbattle.me:9104/pokemons', json = {
    "pokemon_id": "21975",
    "name": "generate"
},
headers={"Content-Type":"application/json", "trainer_token":trainer_token})

print(patch_pokemons.text)

add_pokeball = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', json = {
    "pokemon_id": "21975"
}, headers={"Content-Type":"application/json", "trainer_token":trainer_token})


print(add_pokeball.text)

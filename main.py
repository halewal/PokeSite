import requests 
 
def get_pokemon_info(pokemon_name): 
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}" 
    response = requests.get(url) 
 
    if response.status_code == 200: 
        pokemon_data = response.json() 
        pokemon_info = { 
            "name": pokemon_data["name"], 
            "height": pokemon_data["height"], 
            "weight": pokemon_data["weight"], 
            "abilities": [ability["ability"]["name"] for ability in pokemon_data["abilities"]], 
            "types": [type_data["type"]["name"] for type_data in pokemon_data["types"]] 
        } 
        return pokemon_info 
    else: 
        return None 
 
 
pokemon_name = input("Enter the Pokémon name: ") 
pokemon_info = get_pokemon_info(pokemon_name) 
 
if pokemon_info: 
    print(f"Name: {pokemon_info['name']}") 
    print(f"Height: {pokemon_info['height']}") 
    print(f"Weight: {pokemon_info['weight']}") 
    print(f"Abilities: {', '.join(pokemon_info['abilities'])}") 
    print(f"Types: {', '.join(pokemon_info['types'])}") 
else: 
    print("Pokémon not found!") 

 

Code 

 

Main.py 

 

from flask import Flask, render_template, jsonify 
import requests 
 
app = Flask(__name__) 
 
 
@app.route('/') 
def index(): 
    return render_template('index.html', pokemon="") 
 
 
@app.route('/pokemon/<name>') 
def get_pokemon(name): 
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}") 
    if response.status_code == 200: 
        pokemon_data = response.json() 
        pname = pokemon_data["name"] 
        weight = pokemon_data["weight"] 
        return render_template('index.html', pokemon=pname, 
                               weight=weight) 
 
    else: 
        return render_template('index.html', pokemon="", 
                               weight="") 

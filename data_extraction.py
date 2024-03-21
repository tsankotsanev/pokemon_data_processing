import requests
import json

raw_data_source = "raw_data.json"


def fetch_pokemon_data():
    url = "https://pokeapi.co/api/v2/type/3"

    try:
        response = requests.get(url)
        response.raise_for_status()
        pokemon_data = response.json()["pokemon"][:50]

        for entry in pokemon_data:
            entry.pop("slot", None)

            pokemon_url = entry["pokemon"]["url"]
            pokemon_response = requests.get(pokemon_url)
            pokemon_response.raise_for_status()
            pokemon_details = pokemon_response.json()

            entry["id"] = pokemon_details["id"]
            entry["height"] = pokemon_details["height"]
            entry["weight"] = pokemon_details["weight"]

        return pokemon_data

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to fetch data from API: {str(e)}")


def save_to_file(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file)


try:
    pokemon_data = fetch_pokemon_data()
    print(json.dumps(pokemon_data, indent=4))
    save_to_file(pokemon_data, raw_data_source)
    print(f"Data successfully exported to '{raw_data_source}'!")
except Exception as e:
    print("Error:", str(e))

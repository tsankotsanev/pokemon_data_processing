import json
import sqlite3

transformed_data_source = "transformed_data.json"
database_name = "pokemon.db"


def load_data_from_json(filename):
    with open(filename, "r") as file:
        return json.load(file)


def load_data_into_sqlite(data, db_filename):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    try:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS pokemon_data (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    height REAL,
                    weight REAL,
                    bmi REAL
            )"""
        )

        for pokemon in data:
            cursor.execute(
                """INSERT INTO pokemon_data (id, name, height, weight, bmi)
                   VALUES (?, ?, ?, ?, ?)
                """,
                (
                    pokemon["id"],
                    pokemon["pokemon"]["name"],
                    pokemon["height"],
                    pokemon["weight"],
                    pokemon["bmi"],
                ),
            )

        conn.commit()
        print(
            f"Data loaded into '{database_name}' SQLite database successfully!"
        )
    except Exception as e:
        print("Error:", str(e))
    finally:
        conn.close()


try:
    pokemon_data = load_data_from_json(transformed_data_source)
    load_data_into_sqlite(pokemon_data, database_name)
except Exception as e:
    print("Error:", str(e))

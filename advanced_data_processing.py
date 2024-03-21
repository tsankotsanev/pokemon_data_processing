import sqlite3
import csv
import os


def export_data_to_csv(database_name, table_name, csv_file_path):
    try:
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        with open(csv_file_path, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(
                [description[0] for description in cursor.description]
            )
            csv_writer.writerows(rows)

    except sqlite3.Error as e:
        print(f"Error exporting data to CSV: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def process_csv_data(csv_file_path):

    def print_pokemon_info(pokemon_info):
        print(f"Name: {pokemon_info['name']}")
        print(f"BMI: {pokemon_info['bmi']}")

    try:
        with open(csv_file_path, "r") as file:
            reader = csv.DictReader(file)
            pokemon_data = list(reader)

        total_bmi = sum(float(pokemon["bmi"]) for pokemon in pokemon_data)
        average_bmi = total_bmi / len(pokemon_data)

        print(f"Average BMI of all Pokemon: {round(average_bmi, 2)}")

        pokemon_with_highest_bmi = max(
            pokemon_data, key=lambda x: float(x["bmi"])
        )

        separator = "-" * 30

        print(separator)
        print("Pokemon with the highest BMI:")
        print_pokemon_info(pokemon_with_highest_bmi)

        pokemon_with_lowest_bmi = min(
            pokemon_data, key=lambda x: float(x["bmi"])
        )

        print(separator)
        print("Pokemon with the lowest BMI:")
        print_pokemon_info(pokemon_with_lowest_bmi)
    except FileNotFoundError as e:
        print(f"Error: {e}")


def main():
    database_name = "pokemon.db"
    table_name = "pokemon_data"
    csv_file_path = "pokemon_data.csv"

    if not os.path.exists(csv_file_path):
        export_data_to_csv(database_name, table_name, csv_file_path)
    process_csv_data(csv_file_path)


if __name__ == "__main__":
    main()

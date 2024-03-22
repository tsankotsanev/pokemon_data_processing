# Pokemon Data Processing

This repository contains scripts for extracting, transforming, loading, and processing Pokemon data from the [PokéAPI](https://pokeapi.co/). Follow the instructions below to set up the SQLite database, install dependencies, and run each script.

## Setup

1. **Clone the Repository:**

```
git clone https://github.com/tsankotsanev/pokemon_data_processing.git
```

2. **Navigate to the Repository:**

```
cd pokemon_data_processing
```

3. **Create and activate Python Virtual Environment**:

```
python -m venv venv
```

```
source venv/bin/activate
```

4. **Install Dependencies:**

```
pip install -r requirements.txt
```

## Scripts

It is mandatory the scripts to be run in the listed order for them to function as intended.

### 1. `data_extraction.py`

This script fetches Pokemon data from the PokeAPI prints it in the terminal and saves it to in `raw_data.json`.

-   Run the script:

```
python data_extraction.py
```

### 2. `data_transformation.py`

This script transforms the raw Pokemon data and calculates the BMI for each Pokemon. It then print it in the terminal and exports the transformed data in `transformed_data.json`.

-   Run the script:

```
python data_transformation.py
```

### 3. `data_loading.py`

This script loads the transformed Pokemon data into an SQLite database named `pokemon.db`.

-   Run the script:

```
python data_loading.py
```

### 4. Advanced Data Processing

This script exports the data from the SQLite database to a CSV file and processes it to find the average BMI, as well as the Pokemon with the highest and lowest BMI and prints it in the terminal.

-   Run the script:

```
python advanced_data_processing.py
```

## Visualisation

**[Pokemon Histogram](https://lookerstudio.google.com/reporting/5a8e517d-ead4-4f1b-a84a-e14ed0c06b09/page/XImtD)** showing all BMI of the pokemons in ascending order

**[Pokemon Scatter Plot](https://lookerstudio.google.com/reporting/1ba9e2cf-2fc8-415a-b0fc-16bc579eddd2)** showing the relationship between height and weight

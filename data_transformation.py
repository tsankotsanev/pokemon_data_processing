import json
import apache_beam as beam
import os

raw_data_source = "raw_data.json"
transformed_data_source = "transformed_data.json"


class TransformPokemonData(beam.DoFn):
    def process(self, pokemon):
        pokemon["height"] = round(pokemon["height"] / 10, 2)
        pokemon["weight"] = round(pokemon["weight"] / 10, 2)
        pokemon["bmi"] = round(pokemon["weight"] / (pokemon["height"] ** 2), 2)
        yield pokemon


if not os.path.exists(raw_data_source):
    raise FileNotFoundError(
        f"'{raw_data_source}' not found. Run 'data_extraction.py' to generate it"
    )

with open(raw_data_source, "r") as file:
    raw_data = json.load(file)


with beam.Pipeline() as pipeline:
    _ = (
        pipeline
        | "Create" >> beam.Create(raw_data)
        | "Transform" >> beam.ParDo(TransformPokemonData())
        | "Accumulate into single list" >> beam.combiners.ToList()
        | "Convert to JSON"
        >> beam.Map(lambda x: json.dumps(x, ensure_ascii=True))
        | "Write JSON"
        >> beam.io.WriteToText(
            transformed_data_source,
            shard_name_template="",
        )
    )

with open(transformed_data_source, "r") as file:
    json_data = json.load(file)

print(json.dumps(json_data, indent=4))


print(
    f"Data transformed and exported to '{transformed_data_source}' successfully!"
)

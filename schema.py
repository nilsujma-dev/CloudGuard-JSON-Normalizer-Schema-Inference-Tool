import json
import sys
import pandas as pd
from genson import SchemaBuilder

def get_normalized_df_and_schema(file_path):
    # Load data from JSON file
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Normalize JSON to flat table
    df = pd.json_normalize(data)

    # Infer schema from the data
    builder = SchemaBuilder()
    builder.add_schema({"type": "object", "properties": {}})
    builder.add_object(data)
    schema = builder.to_schema()

    return df, schema

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    df, schema = get_normalized_df_and_schema(file_path)

    # Print the normalized DataFrame
    print(df)

    # Print the inferred schema
    print(json.dumps(schema, indent=4))

if __name__ == "__main__":
    main()


## JSON Data Normalization and Schema Inference Tool

This GitHub repository contains a Python script designed to normalize JSON data into a flat pandas DataFrame and automatically infer its schema using the Genson library. The script processes a JSON file provided as a command-line argument, flattening the nested structures and generating a schema that reflects the data's format.

### Script Features
1. **JSON Data Loading**: Reads the JSON data from a file whose path is provided as a command-line argument.
2. **Data Normalization**:
   - Utilizes `pandas.json_normalize` to convert nested JSON data into a flat table format.
   - Creates a DataFrame (`df`) that represents the normalized data.
3. **Schema Inference**:
   - Employs the Genson library to infer the JSON schema based on the provided data.
   - Generates a schema that describes the structure and types of the JSON data.

### Usage Scenario
This script is particularly useful for data scientists, analysts, and developers working with JSON data. It simplifies the task of transforming nested JSON into a more accessible table format and understanding the data structure through an automatically generated schema.

### Prerequisites
- Python environment with `pandas` and `genson` libraries installed.
- A JSON file with structured data to be normalized and analyzed.

### How to Run the Script
- Run the script from the command line by passing the path to the JSON file as an argument: `python script.py <json_file_path>`.
- The script will output the normalized DataFrame and the inferred JSON schema to the console.

### Security and Best Practices
- Verify the contents of the JSON file before processing, especially if the file originates from an untrusted source.
- Review the inferred schema to ensure it accurately represents the data, making adjustments if necessary.

---

This readme summary provides an overview of the script's functionality and its application in data processing, specifically focusing on JSON data normalization and schema inference. It guides users through using the script for efficient data analysis and understanding complex JSON structures.

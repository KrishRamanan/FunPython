import os
import pandas as pd
import json
import xml.etree.ElementTree as ET

# Function to read CSV file
def extract_csv(file_path):
    return pd.read_csv(file_path)

# Function to read JSON file
def extract_json(file_path):
    with open(file_path, 'r') as file:
        data = [json.loads(line) for line in file]  # Read line by line
    return pd.DataFrame(data)


# Function to read XML file
def extract_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []

    for element in root:
        row = {child.tag: child.text for child in element}
        data.append(row)

    return pd.DataFrame(data)

# Function to detect file type and process accordingly
def process_files(directory):
    all_dataframes = []
    
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        if file.endswith(".csv"):
            print(f"Processing CSV: {file}")
            all_dataframes.append(extract_csv(file_path))
        
        elif file.endswith(".json"):
            print(f"Processing JSON: {file}")
            all_dataframes.append(extract_json(file_path))
        
        elif file.endswith(".xml"):
            print(f"Processing XML: {file}")
            all_dataframes.append(extract_xml(file_path))
        else:
            print(f"Skipping unsupported file: {file}")


    # Merge all data
    final_df = pd.concat(all_dataframes, ignore_index=True)

    # Save to Excel
    output_file = os.path.join(directory, "final_data.xlsx")
    final_df.to_excel(output_file, index=False, engine="openpyxl")

    print(f"Data successfully merged and saved to {output_file}")

# Set directory path (Change this to your actual path)
directory_path = 'C:\Users\Vengata Krishnan R\Downloads\source'

# Run ETL process
process_files(directory_path)

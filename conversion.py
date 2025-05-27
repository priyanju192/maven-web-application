import pandas as pd
import json

def convert_json_to_csv(json_filepath, csv_filepath):
    """
    Converts a JSON file to a CSV file.

    Args:
        json_filepath (str): The path to the input JSON file.
        csv_filepath (str): The path to the output CSV file.
    """
    try:
        with open(json_filepath, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_filepath}")
        return
    except json.JSONDecodeError:
         print(f"Error: Invalid JSON format in {json_filepath}")
         return
    
    df = pd.DataFrame(data)
    df.to_csv(csv_filepath, index=False)
    print(f"Successfully converted {json_filepath} to {csv_filepath}")

if __name__ == "__main__":
    json_filepath = '/var/jenkins_home/reports/trivy-report.json'  
    csv_filepath = '/var/jenkins_home/reports/final-output.csv' 
    convert_json_to_csv(json_filepath, csv_filepath)

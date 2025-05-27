import json
import csv
import sys

def convert_trivy_json_to_csv(json_file_path, csv_file_path):
    """
    Converts a Trivy JSON report to a CSV file.

    Args:
        json_file_path (str): Path to the Trivy JSON report file.
        csv_file_path (str): Path to the output CSV file.
    """
    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_file_path}")
        return
    except json.JSONDecodeError:
         print(f"Error: Invalid JSON format in {json_file_path}")
         return

    vulnerabilities = []
    if isinstance(data, list):
      for result in data:
        if 'Vulnerabilities' in result and result['Vulnerabilities']:
            for vulnerability in result['Vulnerabilities']:
                vulnerability['Target'] = result['Target']
                vulnerabilities.append(vulnerability)
    elif isinstance(data, dict) and 'Results' in data:
        for result in data['Results']:
            if 'Vulnerabilities' in result and result['Vulnerabilities']:
                for vulnerability in result['Vulnerabilities']:
                    vulnerability['Target'] = result['Target']
                    vulnerabilities.append(vulnerability)
    else:
        print("Unexpected JSON structure. Unable to extract vulnerabilities.")
        return

    if not vulnerabilities:
        print("No vulnerabilities found in the JSON report.")
        return
    
    csv_columns = vulnerabilities[0].keys()

    try:
        with open(csv_file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for vulnerability in vulnerabilities:
                writer.writerow(vulnerability)
        print(f"Successfully converted to {csv_file_path}")
    except IOError:
        print(f"I/O error occurred while writing to {csv_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_json_file> <output_csv_file>")
    else:
        json_file_path = /var/jenkins_home/reports/trivy-report.json
        csv_file_path = /var/jenkins_home/reports/tr.csv
        convert_trivy_json_to_csv(json_file_path, csv_file_path)

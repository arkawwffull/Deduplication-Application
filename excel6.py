import csv
from collections import defaultdict
import unicodedata

def normalize(text):
    return unicodedata.normalize("NFC", text)

def remove_duplicates(input_file, output_file):
    seen = set()
    output_data = []

    with open(input_file, 'r', encoding='utf-8-sig') as infile:  
        reader = csv.DictReader(infile)
        for row in reader:
            
            name = normalize(row['Name']).strip().lower()
            email = normalize(row['Email']).strip().lower()
            phone = normalize(row['Phone Number']).strip().lower()
            key = (name, email, phone)
            
            if key not in seen:
                output_data.append(row)
                seen.add(key)

    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:  
        writer = csv.DictWriter(outfile, fieldnames=output_data[0].keys())
        writer.writeheader()
        writer.writerows(output_data)

if __name__ == "__main__":
    input_file = "input_data.csv"
    output_file = "output_data.csv"
    remove_duplicates(input_file, output_file)

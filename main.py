# main.py
from src.loader import load_fitness_data
from src.analysis import compare_formats
from src.converter import convert_file

# -------------------------
# Step 1: Load the data
# -------------------------
csv_df = load_fitness_data("data/fitness.csv")
json_df = load_fitness_data("data/fitness.json")
excel_df = load_fitness_data("data/fitness.xlsx")

print("CSV Data:\n", csv_df.head())
print("JSON Data:\n", json_df.head())
print("Excel Data:\n", excel_df.head())

# -------------------------
# Step 2: Compare file formats
# -------------------------
files = ["data/fitness.csv", "data/fitness.json", "data/fitness.xlsx"]
compare_formats(files)

# -------------------------
# Step 3: Bonus - Convert files
# -------------------------
# Convert CSV → JSON
convert_file("data/fitness.csv", "data/fitness_converted.json", "json")

# Convert JSON → Excel
convert_file("data/fitness.json", "data/fitness_converted.xlsx", "excel")

print("File conversion completed!")

from .loader import load_fitness_data
import pandas as pd

def convert_file(input_file, output_file, output_format):
    df = load_fitness_data(input_file)
    
    if output_format == 'csv':
        df.to_csv(output_file, index=False)
    elif output_format == 'excel':
        df.to_excel(output_file, index=False)
    elif output_format == 'json':
        df.to_json(output_file, orient='records', indent=4)
    else:
        raise ValueError("Unsupported output format")

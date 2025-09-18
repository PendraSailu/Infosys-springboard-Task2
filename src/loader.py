import pandas as pd
import json
import os

def load_fitness_data(file_path, file_type='auto'):
    """
    Load fitness data from CSV, JSON, or Excel
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if file_type == 'auto':
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.csv':
            file_type = 'csv'
        elif ext == '.json':
            file_type = 'json'
        elif ext in ['.xlsx', '.xls']:
            file_type = 'excel'
        else:
            raise ValueError("Unsupported file format.")
    
    try:
        if file_type == 'csv':
            df = pd.read_csv(file_path)
        elif file_type == 'json':
            with open(file_path, 'r') as f:
                data = json.load(f)
            df = pd.json_normalize(data, record_path=['workouts'], meta=['user_id', 'name'])
        elif file_type == 'excel':
            df = pd.read_excel(file_path, engine='openpyxl')
        else:
            raise ValueError("Unsupported file_type parameter")
        
        if df.empty:
            print("Warning: The file is empty.")
        
        return df

    except Exception as e:
        print(f"Error loading file: {e}")
        return pd.DataFrame()

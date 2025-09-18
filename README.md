## Data Format Mastery

## Overview
This project demonstrates handling multiple fitness data formats in Python, including CSV, JSON, and Excel. It focuses on **robust data loading**, **format comparison**, **error handling**, and optional **file conversion** between formats.  

The project is part of a data handling and analysis exercise to strengthen skills in managing real-world data in various formats.

## Features

1. **Universal Data Loader**
   - Loads fitness data from CSV, JSON, and Excel files.
   - Handles nested JSON data.
   - Gracefully handles missing or corrupted files with informative error messages.
   - Ensures consistent column structure across formats.

2. **Format Comparison Analysis**
   - Compares file sizes and loading speeds of different data formats.
   - Generates visualizations using Matplotlib and Seaborn:
     - Load time comparison
     - File size comparison
   - Saves plots in the `reports/` folder.

3. **Error Handling Showcase**
   - Demonstrates robust handling of:
     - Non-existent files
     - Corrupted/malformed files
     - Empty files

4. **Bonus: File Conversion**
   - Converts CSV → JSON and JSON → Excel.
   - Preserves data integrity during conversion.

## Project Structure

<img width="373" height="458" alt="image" src="https://github.com/user-attachments/assets/20fda0db-152c-49f7-8c30-67311f5bc8b7" />

## Install Dependencies
   -pip install pandas openpyxl xlrd matplotlib seaborn
   
## Run the Project 
  - python main.py
**This will show:**
  - Load CSV, JSON, and Excel data.
  - Display loaded data in the console.
  - Generate comparison graphs in reports/.
  - Convert CSV → JSON and JSON → Excel.




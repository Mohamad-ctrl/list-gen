import pandas as pd

def check_for_duplicates(file_path):
    # Load the Excel file into a DataFrame
    df = pd.read_excel(file_path)

    # Check for duplicate rows
    duplicates = df[df.duplicated(keep=False)]

    if not duplicates.empty:
        print(f"Found {len(duplicates)} duplicate rows:")
        print(duplicates)
    else:
        print("No duplicate rows found.")

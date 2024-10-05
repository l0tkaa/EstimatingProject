import pandas as pd
import os

def extract_data_from_excel(file_path):
    """
    Extract non-zero data from Excel, along with the descriptions in the adjacent column.
    
    Args:
        file_path (str): Path to the Excel file.
        
    Returns:
        extracted_data (dict): A dictionary containing extracted data for each spreadsheet.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Read the Excel file
    excel_data = pd.ExcelFile(file_path)
    
    extracted_data = {}

    # Loop through each sheet in the Excel workbook
    for sheet_name in excel_data.sheet_names:
        df = excel_data.parse(sheet_name)  # Parse the current sheet into a DataFrame
        
        sheet_data = []
        
        # Iterate over rows and columns in the DataFrame
        for index, row in df.iterrows():
            for col in df.columns[1:]:  # Start from the second column
                value = row[col]
                
                # Check if the value is non-zero
                if pd.notna(value) and value != 0:
                    description = row[df.columns[0]]  # The description is in the first column
                    sheet_data.append({
                        'description': description,
                        'value': value
                    })
        
        if sheet_data:
            extracted_data[sheet_name] = sheet_data
    
    return extracted_data

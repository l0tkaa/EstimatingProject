# src/main.py

import os
from dotenv import load_dotenv
from data_extractor import extract_data_from_word
from data_extractor import extract_data_from_excel
from file_handler import write_data_to_json

load_dotenv()

def main():
    input_directory = r'C:\Programming Projects\Sample Folder'  # Input folder for Word and Excel files
    output_directory_word = os.getenv(OUTPUT_DIR_WORD)
    output_directory_excel = os.getenv(OUTPUT_DIR_EXCEL)
   

    # initialize flags and data containers
    word_files_found = False
    excel_files_found = False
    all_word_data = []
    all_excel_data=[]

    # Walk through the input directory and its subdirectories
    for root, dirs, files in os.walk(input_directory):
        for filename in files:
            if filename.startswith('~$'):
                continue
            file_path = os.path.join(root, filename)

            if filename.endswith('.docx'):  #check for .docx files
                word_files_found = True
                print(f"Processing {file_path} ...")
                # extract data from the Word document
                extracted_data = extract_data_from_word(file_path)
                all_word_data.extend(extracted_data) # add extracted data to the list


            if filename.endswith('.xlsx'): # check for excel files
                excel_files_found = True 
                print(f"Processing {file_path}) ... ")

                extracted_data = extract_data_from_excel(file_path)
                all_excel_data.extend(extracted_data)



#all word and excel info going to separate json files
   

    all_extracted_data = extracted_data
    

    # check if Word files were found
    if not word_files_found: 
        print("No .doc or .docx files exist in the directory.")
    else: 
    # write all extracted data to json file
        write_data_to_json(all_word_data, output_directory_word)
        print(f"Word data extracted and saved to {output_directory_word}.")
    
    # Check if Excel files were found
    if not excel_files_found:
        print("No .xlsx files exist in the directory.")
    else:
    # write all extracted data to json file
        write_data_to_json(all_excel_data, output_directory_excel)
        print(f"Excel data extracted and saved to {output_directory_excel}.")

if __name__ == "__main__":
    main()



    
   
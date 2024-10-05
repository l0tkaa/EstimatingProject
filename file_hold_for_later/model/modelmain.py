from data_extractor import extract_data_from_excel
from file_handler import write_data_to_json
from model import train_model, predict
import pandas as pd

def main():
    # Step 1: Extract data from Excel file
    input_file = os.getenv(SAMPLE_ESTIMATES)
    features, target = extract_data_from_excel(input_file)
    
    # Step 2: Save extracted data to JSON for future use
    data_dict = {
        'features': features.to_dict(orient='records'),
        'target': target.tolist()
    }
    output_file = 'data/raw.json'
    write_data_to_json(data_dict, output_file)
    
    print(f"Data extracted and saved to {output_file}.")
    
    # Step 3: Train machine learning model
    model = train_model(features, target)
    
    # Step 4: Predict future estimates (dummy example, replace with actual new data)
    new_data = pd.DataFrame({
        'materials_cost': [5000],
        'employees': [3],
        'days_worked': [10],
        'hours_worked': [8],
        'equipment_time': [20],
        'demo': [1]
    })
    
    prediction = predict(model, new_data)
    print(f"Estimated cost: {prediction[0]}")

if __name__ == '__main__':
    main()

import shutil
import os

def load_data(input_file, output_file):
    # Logic to load or preprocess raw data before further processing.
    # For example, this could be about handling missing values, unzipping, etc.
    
    # Simple example: Copying data to a new location for preprocessing
    if not os.path.exists(output_file):
        shutil.copy(input_file, output_file)
    print(f"Data loaded from {input_file} to {output_file}")

if __name__ == "__main__":
    load_data('data/raw.csv', 'data/raw_copy.csv')

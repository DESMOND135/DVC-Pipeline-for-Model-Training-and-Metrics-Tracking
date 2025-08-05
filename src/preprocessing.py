import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(input_file, output_file):
    # Load the raw data
    df = pd.read_csv(input_file)
    
    # One-hot encode categorical columns (e.g., 'sex', 'smoker', 'region')
    df = pd.get_dummies(df, columns=['sex', 'smoker', 'region'], drop_first=True)
    
    # Save the processed data to the output file
    df.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")

if __name__ == "__main__":
    preprocess_data('data/raw_copy.csv', 'data/processed.csv')

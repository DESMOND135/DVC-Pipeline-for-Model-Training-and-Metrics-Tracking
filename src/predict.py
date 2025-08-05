import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import sys

def predict(input_file, model_path):
    # Load the model
    model = joblib.load(model_path)

    # Load the input data
    df = pd.read_csv(input_file)

    # Save original data to include in final output (optional)
    original_data = df.copy()

    # Preprocess: Encode 'sex' and 'smoker'
    df['sex'] = df['sex'].map({'male': 0, 'female': 1})
    df['smoker'] = df['smoker'].map({'no': 0, 'yes': 1})
    df = pd.get_dummies(df, columns=['region'], drop_first=True)

    # Ensure all expected columns are present (in case some dummy columns are missing)
    expected_columns = ['age', 'sex', 'bmi', 'children', 'smoker', 
                        'region_northwest', 'region_southeast', 'region_southwest']
    
    for col in expected_columns:
        if col not in df.columns:
            df[col] = 0  # Add missing dummy columns with 0

    # Reorder columns
    df = df[expected_columns]

    # Scale features (same as training)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)

    # Predict
    predictions = model.predict(X_scaled)

    # Combine predictions with input
    output = original_data.copy()
    output['predicted_charges'] = predictions

    # Save or print results
    output.to_csv('data/predictions.csv', index=False)
    print("Predictions saved to 'data/predictions.csv'")

if __name__ == "__main__":
    # Example usage: python src/predict.py data/test.csv models/model.pkl
    if len(sys.argv) != 3:
        print("Usage: python src/predict.py <input_file> <model_path>")
    else:
        predict(sys.argv[1], sys.argv[2])

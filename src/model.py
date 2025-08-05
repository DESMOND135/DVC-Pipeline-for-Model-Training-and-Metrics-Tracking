import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import json

def train_model(input_file, model_output_path, metrics_output_path):
    # Load the processed data
    df = pd.read_csv(input_file)

    # Separate features and target
    X = df.drop(columns=['charges'])
    y = df['charges']

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train a Linear Regression model
    model = LinearRegression()
    model.fit(X_scaled, y)

    # Make predictions
    y_pred = model.predict(X_scaled)

    # Calculate metrics
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    # Save metrics to JSON file
    metrics = {"MSE": mse, "R2": r2}
    with open(metrics_output_path, 'w') as f:
        json.dump(metrics, f)

    # Save the trained model to a file
    joblib.dump(model, model_output_path)

if __name__ == "__main__":
    # Paths to the input data, output model, and metrics file
    input_file = 'data/processed.csv'
    model_output_path = 'models/model.pkl'
    metrics_output_path = 'metrics.json'

    # Train the model and save the metrics
    train_model(input_file, model_output_path, metrics_output_path)

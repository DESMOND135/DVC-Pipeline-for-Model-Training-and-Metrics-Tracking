import os
import logging
import pandas as pd

def setup_logging(log_file='app.log'):
    """
    Set up logging for the application.
    
    Parameters:
    - log_file: Name of the log file to save the logs
    
    Returns:
    - logger: Configured logger instance
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    
    return logger

def check_data_validity(df):
    """
    Check basic data validity: missing values, datatypes, etc.
    
    Parameters:
    - df: pandas DataFrame
    
    Returns:
    - None: Prints out data validity info
    """
    print("Data Validity Check:")
    
    # Check for missing values
    missing = df.isnull().sum()
    print(f"\nMissing values:\n{missing[missing > 0]}")
    
    # Check for data types
    print(f"\nData Types:\n{df.dtypes}")
    
    # Check basic statistics
    print(f"\nBasic statistics:\n{df.describe()}")

def save_dataframe_to_csv(df, filename):
    """
    Save the DataFrame to a CSV file.
    
    Parameters:
    - df: pandas DataFrame
    - filename: Name of the file to save the DataFrame to
    
    Returns:
    - None
    """
    df.to_csv(filename, index=False)
    print(f"DataFrame saved to {filename}")

def load_dataframe_from_csv(file_path):
    """
    Load a DataFrame from a CSV file.
    
    Parameters:
    - file_path: Path to the CSV file
    
    Returns:
    - df: pandas DataFrame loaded from CSV
    """
    df = pd.read_csv(file_path)
    print(f"DataFrame loaded from {file_path}")
    return df

import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

output = load_data(input("Enter the path to the CSV file: "))
if output is not None:
    print(output.head())


def analyze_data(data):
    """
    Perform basic analysis on the DataFrame.
    
    Parameters:
    data (pd.DataFrame): The DataFrame to analyze.
    
    Returns:
    dict: A dictionary containing basic statistics.
    """
    if data is None or data.empty:
        return {"error": "No data to analyze"}
    
    analysis = {
        "describe": data.describe()
    }
    
    return analysis

analysis_result = analyze_data(output)
if analysis_result:
    print("Analysis Result:")
    print(analysis_result)
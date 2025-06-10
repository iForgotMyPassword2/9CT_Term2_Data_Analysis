import pandas as pd

def main():
    # Create a DataFrame with some sample data
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    
    df = pd.DataFrame(data)
    
    # Display the DataFrame
    print("DataFrame:")
    print(df)

    # Save the DataFrame to a CSV file
    df.to_csv('sample_data.csv', index=False)
    print("\nDataFrame saved to 'sample_data.csv'.")

    # Read the DataFrame from the CSV file
    df_loaded = pd.read_csv('sample_data.csv')

    print("\nDataFrame loaded from 'sample_data.csv':")

    # Display the loaded DataFrame
    print(df_loaded)
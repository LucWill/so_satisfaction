# preprocessing.py

import pandas as pd

def map_column_to_numbers(df, column, mapping_dict):
    """
    Replaces values in a DataFrame column using a given mapping dictionary.

    Args:
        df (pd.DataFrame): DataFrame containing the data.
        column (str): Name of the column to be mapped.
        mapping_dict (dict): Dictionary mapping strings to numerical values.

    Returns:
        pd.Series: The mapped column as a Pandas Series.
    """
    return df[column].replace(mapping_dict)

def clean_years_code(column):
    return column.replace({
        'Less than 1 year': 0,
        'More than 50 years': 60
    }).apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

def count_tools_columns(df, columns):
    """
    Counts the number of tools (or entries) in specified columns 
    and creates new columns with the counts.

    Args:
        df (pd.DataFrame): The DataFrame containing the tool columns.
        columns (list): List of column names to process.

    Returns:
        pd.DataFrame: DataFrame with additional columns '<ColumnName>_Count'.
    """
    for col in columns:
        df[col] = df[col].apply(
            lambda x: str(x).count(';')+1 if pd.notnull(x) else 0
        )
    return df


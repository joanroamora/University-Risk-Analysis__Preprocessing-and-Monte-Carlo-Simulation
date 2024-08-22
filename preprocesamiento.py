import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_plus_signs(df):
    # Eliminar signos "+" en los valores numéricos, sin importar su posición
    df_cleaned = df.replace(to_replace=r'(\d+)\+', value=r'\1', regex=True)
    return df_cleaned

def fill_missing_values(df):
    df_filled = df.apply(lambda col: col.fillna(col.mean()) if col.dtype in ['float64', 'int64'] else col, axis=0)
    return df_filled

def clean_column_names(df):
    df.columns = df.columns.str.strip()
    return df

def save_data(df, output_filepath):
    df.to_csv(output_filepath, index=False)

import pandas as pd
from contract import Vendas
from dotenv import load_dotenv
import os

load_dotenv(".env")

# Read environment variables
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

# Create the database connection URL
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)

        # Check if there are extra columns in the DataFrame
        extra_cols = set(df.columns) - set(Vendas.model_fields.keys())
        if extra_cols:
            return False, f"Extra columns detected in Excel: {', '.join(extra_cols)}"

        # Validate each line with the chosen schema
        for index, row in df.iterrows():
            try:
                _ = Vendas(**row.to_dict())
            except Exception as e:
                raise ValueError(f"Line error {index + 2}: {e}")

        return df, True, None

    except ValueError as ve:
        return df, False, str(ve)
    except Exception as e:
        return df, False, f"Unexpected error: {str(e)}"
    
def excel_to_sql(df):
    df.to_sql('vendas', con=DATABASE_URL, if_exists='replace', index=False)

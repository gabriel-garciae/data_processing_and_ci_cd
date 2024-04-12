import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv(".env")

# Read environment variables
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

# Creates the database connection URL
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

def test_read_data_and_check_schema():
    df = pd.read_sql('SELECT * FROM vendas', con=DATABASE_URL)

    # Check if the DataFrame is not empty
    assert not df.empty, "O DataFrame está vazio."

    # Check the schema (columns and data types)
    expected_dtype = {
        'email': 'object',  # object in Pandas matches string in SQL
        'date': 'datetime64[ns]',
        'value': 'float64',
        'product': 'object',
        'amount': 'int64',
        'category': 'object'
    }
    print(df.dtypes.to_dict())
    assert df.dtypes.to_dict() == expected_dtype, "O schema do DataFrame não corresponde ao esperado."
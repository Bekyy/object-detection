# scripts/load_data.py

import os
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

def load_data_from_postgres(query):
    try:
        # Define your PostgreSQL connection parameters
        connection = psycopg2.connect(
            host="localhost",  # Replace with your host
            port=5432,  # Ensure this is an integer, not a string
            database="md_data",  # Replace with your database name
            user="postgres",  # Replace with your PostgreSQL username
            password="1234"  # Replace with your password
        )
        
        # Load data into a pandas DataFrame
        df = pd.read_sql(query, connection)
        
        # Close the connection
        connection.close()
        
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

from sqlalchemy import create_engine

def load_data_to_postgres(df):
    try:
        # Define your connection string for SQLAlchemy
        connection_string = f"postgresql+psycopg2://postgres:1234@localhost:5432/md_data"
        
        # Create an SQLAlchemy engine
        engine = create_engine(connection_string)

        table_name = 'telegram_medical_data'
        
        # Load DataFrame into the PostgreSQL table
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        
        print(f"Data successfully written to table '{table_name}' in PostgreSQL.")

    except Exception as e:
        print(f"An error occurred: {e}")
        return None



def load_data_using_sqlalchemy(query):
    """
    Connects to the PostgreSQL database and loads data based on the provided SQL query using SQLAlchemy.

    :param query: SQL query to execute.
    :return: DataFrame containing the results of the query.
    """
    try:
        # Create a connection string
        connection_string = f"postgresql+psycopg2://postgres:1234@localhost:5432/md_data"

        # Create an SQLAlchemy engine
        engine = create_engine(connection_string)

        # Load data into a pandas DataFrame
        df = pd.read_sql_query(query, engine)

        return df

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
# def load_data_to_postgres(df):
#     try:
#         # Define your PostgreSQL connection parameters
#         connection = psycopg2.connect(
#             host="localhost",  # Replace with your host
#             port=5432,  # Ensure this is an integer, not a string
#             database="md_data",  # Replace with your database name
#             user="postgres",  # Replace with your PostgreSQL username
#             password="1234"  # Replace with your password
#         )
        
#         table_name = 'telegram_medical_data'
#         df.to_sql(table_name, con=connection, if_exists='replace', index=False)
        
#         # Close the 
#         connection.close()
     
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None
    
    
import pandas as pd
import os
import time
from pathlib import Path
import mysql.connector
from mysql.connector import Error

# Get the directory where the script is located
script_dir = Path(__file__).parent
source_file = script_dir / "Concrete_Data.csv"

dataset = pd.read_csv(source_file)

def parse_data(dataset2):
    dataset2['cement'] = pd.to_numeric(dataset['Cement'], errors='coerce')
    dataset2['blast'] = pd.to_numeric(dataset['Blast'], errors='coerce')
    dataset2['fly_ash'] = pd.to_numeric(dataset['FlyAsh'], errors='coerce')
    dataset2['water'] = pd.to_numeric(dataset['Water'], errors='coerce')
    dataset2['superplasticizer'] = pd.to_numeric(dataset['Superplasticizer'], errors='coerce')
    dataset2['coarse_aggregate'] = pd.to_numeric(dataset['CoarseAggregate'], errors='coerce')
    dataset2['fine_aggregate'] = pd.to_numeric(dataset['FineAggregate'], errors='coerce')
    dataset2['age'] = pd.to_numeric(dataset['Age'], errors='coerce')
    dataset2['strength'] = pd.to_numeric(dataset['Strength'], errors='coerce')
    
    return dataset2[['cement', 'blast', 'fly_ash', 'water', 'superplasticizer', 'coarse_aggregate', 'fine_aggregate', 'age', 'strength']]

def load_data_to_db(data):
    try:
        connection = mysql.connector.connect(
            host='maryska',
            database='beton',
            user='myuser',
            password='my-secret-pw'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS concrete_data (id INT AUTO_INCREMENT PRIMARY KEY, cement FLOAT, blast FLOAT, fly_ash FLOAT, water FLOAT, superplasticizer FLOAT, coarse_aggregate FLOAT, fine_aggregate FLOAT, age FLOAT, strength FLOAT)")
            
            for index, row in data.iterrows():
                cursor.execute("INSERT INTO concrete_data (cement, blast, fly_ash, water, superplasticizer, coarse_aggregate, fine_aggregate, age, strength) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                               (row['cement'], row['blast'], row['fly_ash'], row['water'], row['superplasticizer'], row['coarse_aggregate'], row['fine_aggregate'], row['age'], row['strength']))
            
            connection.commit()
            print("Data loaded successfully into the database.")      
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")  


def wait_for_db(host, user, password, database, timeout=120, interval=3):
    start_time = time.time()
    while True:
        try:
            conn = mysql.connector.connect(
                host=host,
                database=database,
                user=user,
                password=password
            )
            conn.close()
            print("Database is available.")
            return
        except Error as e:
            elapsed = time.time() - start_time
            if elapsed >= timeout:
                raise RuntimeError(f"Could not connect to DB after {timeout} seconds: {e}")
            print(f"DB not ready yet ({e}), retrying in {interval}s...")
            time.sleep(interval)


if __name__ == "__main__":
    data = parse_data(dataset)
    wait_for_db('maryska', 'myuser', 'my-secret-pw', 'beton')
    load_data_to_db(data)
    
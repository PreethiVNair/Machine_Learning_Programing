import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv


class EmployeeDataLoader:

    def __init__(self):
        load_dotenv()
        self.database_url = os.getenv("DATABASE_URL")

        if not self.database_url:
            raise ValueError("DATABASE_URL was not found in the .env file")

    def load_data(self):
        conn = psycopg2.connect(self.database_url)

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees;")

        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        df = pd.DataFrame(rows, columns=columns)

        cursor.close()
        conn.close()

        return df
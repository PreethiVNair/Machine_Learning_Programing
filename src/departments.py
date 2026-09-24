import os
import psycopg2
from dotenv import load_dotenv
import pandas as pd

class DepartmentDataManager:

    def __init__(self):
        load_dotenv()
        self.database_url = os.getenv("DATABASE_URL")

        if not self.database_url:
            raise ValueError("DATABASE_URL was not found.")

    def populate_departments(self):

        departments = [
            ("Software Development", "Toronto", 1500000),
            ("Data & Analytics", "Waterloo", 1200000),
            ("Cloud & DevOps", "Toronto", 1400000),
            ("Cybersecurity", "Ottawa", 1100000),
            ("IT Support", "Waterloo", 800000)
        ]

        conn = psycopg2.connect(self.database_url)
        cursor = conn.cursor()

        for department in departments:
            cursor.execute(
                """
                INSERT INTO departments
                (department_name, location, budget)
                VALUES (%s, %s, %s)
                """,
                department
            )

        conn.commit()
        cursor.close()
        conn.close()

        print("Departments inserted successfully.")

    def assign_departments_to_employees(self):

        position_department_map = {
            "Software Developer": 1,
            "Backend Developer": 1,
            "Software Engineer": 1,
            "QA Engineer": 1,
            "Solutions Architect": 1,

            "Data Analyst": 2,
            "Data Engineer": 2,
            "Machine Learning Engineer": 2,

            "DevOps Engineer": 3,
            "Cloud Engineer": 3,

            "Cybersecurity Analyst": 4,
            "Network Engineer": 4,

            "IT Support Specialist": 5,
            "Systems Analyst": 5,
            "Database Administrator": 5
        }

        conn = psycopg2.connect(self.database_url)
        cursor = conn.cursor()

        for position, department_id in position_department_map.items():
            cursor.execute(
                """
                UPDATE employees
                SET department_id = %s
                WHERE position = %s
                """,
                (department_id, position)
            )

        conn.commit()
        cursor.close()
        conn.close()

        print("Departments assigned to employees successfully.")
        
    def load_employee_department_data(self):

        conn = psycopg2.connect(self.database_url)

        query = """
            SELECT
                e.employee_id,
                e.name,
                e.position,
                e.start_date,
                e.salary,
                d.department_name,
                d.location,
                d.budget
            FROM employees e
            JOIN departments d
                ON e.department_id = d.department_id;
        """

        df = pd.read_sql_query(query, conn)

        conn.close()

        return df
from faker import Faker
from datetime import date
import random
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv


# Generate synthetic employee data for IT-related job positions

fake = Faker()

it_positions = [
    "Software Developer",
    "Backend Developer",
    "Data Analyst",
    "Data Engineer",
    "Database Administrator",
    "DevOps Engineer",
    "Cloud Engineer",
    "Network Engineer",
    "Systems Analyst",
    "Cybersecurity Analyst",
    "Machine Learning Engineer",
    "QA Engineer",
    "IT Support Specialist",
    "Solutions Architect",
    "Software Engineer"
]

employees = []

# Generate 50 employees
for i in range(50):
    employees.append({
        "name": fake.name(),
        "position": random.choice(it_positions),
        "start_date": fake.date_between(
            start_date=date(2015, 1, 1),
            end_date=date(2024, 12, 31)
        ),
        "salary": random.randint(60000, 200000)
    })

# Convert generated records to a DataFrame
df = pd.DataFrame(employees)

print(df)
print("\nTotal records generated:", len(df))


# Insert employee data into Neon PostgreSQL

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL was not found in the .env file")

conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

for employee in employees:
    cursor.execute(
        """
        INSERT INTO employees (name, position, start_date, salary)
        VALUES (%s, %s, %s, %s)
        """,
        (
            employee["name"],
            employee["position"],
            employee["start_date"],
            employee["salary"]
        )
    )

conn.commit()

print("50 employees inserted successfully!")

cursor.close()
conn.close()
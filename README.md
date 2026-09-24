# Data Engineering & Exploratory Data Analysis Workshop

## Project Overview

This project demonstrates a data engineering and exploratory data analysis workflow using Python, Pandas, and a PostgreSQL cloud database hosted on Neon.

A synthetic employee dataset was generated using Python and the Faker library and stored in the PostgreSQL database. The data was then loaded into a Pandas DataFrame for cleaning, transformation, feature engineering, scaling, exploratory data analysis, and visualization.

For the advanced analysis, a second table containing department information was added and joined with the employee data.

---

## Dataset

The employee dataset contains 50 synthetic employee records with the following information:

- Employee ID
- Name
- IT-related job position
- Start date between 2015 and 2024
- Salary between $60,000 and $200,000

The data was generated using Python and the Faker library and inserted into a Neon PostgreSQL database.

---

## Database

The project uses a PostgreSQL cloud database hosted on Neon.

Employee records are retrieved from the database using SQL and `psycopg2`.

Example SQL query:

```sql
SELECT * FROM employees;
```

For the advanced analysis, a second table called `departments` is used. The `employees` and `departments` tables are joined using the `department_id` column.

The department data contains:

- Department name
- Location
- Budget

---

## Data Cleaning

The employee dataset was checked for:

- Missing values
- Duplicate records
- Data types
- Salary range
- Start date range

These checks help make sure the data is ready for analysis.

---

## Descriptive Statistics

Descriptive statistics were used to understand the employee dataset.

The following Pandas methods were used:

```python
df.info()
df.describe()
df.isnull().sum()
```

These methods provide information about data types, missing values, averages, minimum values, maximum values, and other numerical statistics.

---

## Data Transformation and Feature Engineering

The `start_date` column was converted to a Pandas datetime format.

Two additional features were created:

- `start_year` – represents the year the employee started.
- `years_of_service` – represents the approximate number of years the employee worked by the end of 2024.

These features were created to make the employee data easier to analyze.

---

## Scaling

Min-Max scaling was applied to the employee salary.

The scaled values are stored in a new column called `salary_scaled`.

The values are transformed to a range between 0 and 1 while the original salary column is kept in the dataset.

---

## Visualizations

### Visualization 1: Average Salary by Position and Start Year

A grouped bar chart is used to compare the average salary of different job positions based on the year employees started.

This visualization helps show salary differences across job positions and start years.

### Visualization 2: Average Salary by Department and Position

For the advanced analysis, employee data is combined with department information using an SQL JOIN.

A heatmap is used to compare the average salaries of different job positions across departments.

This provides a more detailed comparison using information from multiple database tables.

---

## Project Structure

```text
Machine_Learning_Programing/
│
├── src/
│   ├── departments.py
│   ├── generate_employees.py
│   ├── load_employees.py
│   └── visualization.py
│
├── exploratory_data_analysis.ipynb
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

### File Description

- `generate_employees.py` – generates 50 synthetic employee records and inserts them into PostgreSQL.
- `load_employees.py` – retrieves employee data from PostgreSQL and loads it into a Pandas DataFrame.
- `departments.py` – manages department data, assigns departments to employees, and joins employee and department data.
- `visualization.py` – contains the grouped bar chart and heatmap visualization methods.
- `exploratory_data_analysis.ipynb` – main notebook containing data cleaning, descriptive statistics, transformation, feature engineering, scaling, visualizations, and conclusions.
- `requirements.txt` – contains the Python packages required to run the project.
- `.env.example` – shows the required environment variable without including private database credentials.
- `.gitignore` – prevents private and unnecessary files from being uploaded to GitHub.

---

## Required Python Packages

All required Python packages are listed in `requirements.txt`.

Install them using:

```bash
pip install -r requirements.txt
```

---

## Environment Setup

The PostgreSQL database connection string is stored in a `.env` file.

For security reasons, the actual `.env` file is not included in the GitHub repository.

An `.env.example` file is provided as a template.

Create a `.env` file in the project root and add your PostgreSQL connection string:

```text
DATABASE_URL=your_neon_database_connection_string
```

Do not upload the `.env` file to GitHub because it contains private database credentials.

---

## Running the Project

1. Clone the GitHub repository.

2. Create and activate a Python virtual environment.

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Create a PostgreSQL database in Neon.

5. Create a `.env` file and add your database connection string:

```text
DATABASE_URL=your_neon_database_connection_string
```

6. Make sure the required `employees` and `departments` tables are available in the PostgreSQL database.

7. Run `generate_employees.py` to generate and insert the synthetic employee records.

8. Open `exploratory_data_analysis.ipynb`.

9. Run all notebook cells from the beginning to perform the analysis and display the visualizations.

---

## Insights and Conclusion

The employee data was checked for missing values, duplicate records, data types, salary ranges, and start dates.

The grouped bar chart was used to compare average salaries across different job positions and employee start years.

For the advanced analysis, employee data was joined with department data. A heatmap was used to compare average salaries across departments and job positions.

New features such as `start_year` and `years_of_service` were created, and Min-Max scaling was applied to salary values.

Overall, this project demonstrates how data can be generated, stored in a PostgreSQL cloud database, loaded into Python, cleaned, transformed, analyzed, and visualized.
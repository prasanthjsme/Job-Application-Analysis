# Job Application Analysis — SQL + Interactive Dashboard

A portfolio project that analyzes **120 fictional job application records** using MySQL SQL queries and an interactive Streamlit dashboard. The project helps explore application activity, outcomes, portals, roles, locations, and expected salary.

> **Data note:** The included dataset is synthetic and for learning/portfolio purposes only. Do not upload personal job-tracker data to a public repository.

## Dashboard Overview

The interactive dashboard is built with **Streamlit, Pandas, and Plotly**. It lets users filter the sample dataset and explore the metrics and charts below.

### KPI Cards
- **Total Applications** — count of applications after filters
- **Positive Responses** — applications marked Shortlisted or Interview Scheduled
- **Positive Response Rate** — positive responses divided by filtered applications
- **Average Expected Salary** — average expected salary in LPA for filtered records

### Interactive Filters
- Applied date range
- Job portal
- Job role
- Location
- Application status

### Charts & Analysis
1. **Applications by Status** — compare statuses such as Applied, Rejected, Shortlisted, and Interview Scheduled.
2. **Applications by Portal** — compare application counts across job portals.
3. **Monthly Application Trend** — view application volume over time.
4. **Applications by Role** — compare application counts for different job roles.

### Application Records & Export
- View the filtered application records in a data table.
- Download the currently filtered records as a CSV file.

## Dashboard Preview (what you will see when running it)

- Dashboard title and a sidebar containing date, portal, role, location, and status filters.
- Four KPI metric cards across the top.
- Four interactive charts arranged in two columns.
- Application records table with a **Download filtered CSV** button.

## Technologies Used
- **SQL / MySQL:** data analysis queries and database practice
- **Python:** dashboard logic
- **Pandas:** data loading, filtering, and calculations
- **Streamlit:** interactive dashboard interface
- **Plotly:** charts

## Dataset

`data/job_applications_sample.csv` contains 120 synthetic records with fields such as company, job role, location, applied date, portal, status, experience level, and expected salary. The data is fictional and should not be interpreted as real job-market results.

## SQL Concepts Practiced
- SELECT, WHERE, ORDER BY
- GROUP BY and aggregate functions
- CASE statements
- HAVING
- Date-based analysis
- Conditional aggregation
- Common Table Expressions (CTEs)
- Window functions (including `RANK()`)
- Application-status and positive-response analysis

## Project Structure

```text
Job_Application_Analysis_SQL_Dashboard/
├── app.py                              # Streamlit interactive dashboard
├── requirements.txt                     # Python dependencies
├── README.md                            # Project documentation
├── data/
│   └── job_applications_sample.csv      # Synthetic dataset (120 rows)
└── sql/
    ├── 01_create_database_table.sql     # Database and table setup
    └── 02_analysis_queries.sql          # SQL analysis queries
```

## Run the Dashboard Locally

1. Install Python 3.10+.
2. Open a terminal in the project folder.
3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```
4. Start the dashboard:

   ```bash
   python -m streamlit run app.py
   ```
5. Streamlit will open the dashboard in your browser. If it does not, use the local URL printed in the terminal (usually `http://localhost:8501`).

## Run the SQL Analysis

1. Open MySQL Workbench.
2. Run `sql/01_create_database_table.sql` to create the database and table.
3. Import `data/job_applications_sample.csv` into the created table.
4. Run `sql/02_analysis_queries.sql` to explore the analysis queries.

## Business Questions
- How many applications were submitted?
- What is the distribution of application statuses?
- Which job portals have the most applications?
- How does application volume change month by month?
- Which job roles receive the most applications?
- What is the positive-response rate?
- How do expected salary values vary across applications?

## Resume Description
**Job Application Analysis | SQL, MySQL, Python, Pandas, Streamlit, Plotly**

- Analyzed 120 synthetic job application records using MySQL to track application status, portal, role, location, expected salary, and monthly trends.
- Practiced SQL aggregations, CASE statements, date functions, HAVING, CTEs, and window functions to derive application metrics and response rates.
- Built an interactive Streamlit dashboard with KPI cards, filters, charts, a records table, and CSV export to explore application patterns.

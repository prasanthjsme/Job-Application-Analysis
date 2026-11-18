# Job Application Analysis — SQL + Dashboard
Portfolio project analyzing 120 synthetic job applications.
## Features
- MySQL analysis: status, portal, role, location, monthly trend, response rate, salary, CTE and RANK.
- Streamlit dashboard: KPIs, filters, charts, records table and CSV export.
## Dataset
`data/job_applications_sample.csv` contains fictional data only.
## Run Dashboard
`python -m pip install -r requirements.txt` then `python -m streamlit run app.py`
## SQL Setup
Run `sql/01_create_database_table.sql` in MySQL Workbench, import the sample CSV into the table, then run `sql/02_analysis_queries.sql`.
## Resume description
**Job Application Analysis | SQL, MySQL, Python, Pandas, Streamlit**
- Analyzed 120 synthetic job application records using MySQL to track status, role, company, location, portal and monthly trends.
- Used aggregations, CASE, date functions, HAVING, CTEs and window functions to calculate application metrics and response rates.
- Built an interactive dashboard with KPI cards, filters, charts and CSV export to explore application patterns.
Use synthetic/anonymized data in public repositories; do not upload personal job tracker records.

CREATE DATABASE job_application_analysis;
USE job_application_analysis;
CREATE TABLE job_applications (application_id INT PRIMARY KEY, company_name VARCHAR(100), job_role VARCHAR(100), location VARCHAR(50), applied_date DATE, job_portal VARCHAR(50), status VARCHAR(50), experience_level VARCHAR(30), expected_salary_lpa DECIMAL(5,2));
-- Import the sample CSV into this table using MySQL Workbench.

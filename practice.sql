CREATE TABLE employee_performance (
    email_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary DECIMAL (10,2) CHECK (salary >0),
    joining_date DATE NOT NULL,
    experience_years INT CHECK (experience_years >= 0),
    performance_score DECIMAL(4,2) CHECK (performance_score >= 0 AND performance_score <= 5),
    project_completed INT DEFAULT 0,
    last_promotion_date DATE NULL,
    employee_status VARCHAR(20) CHECK (employee_status IN ('Active', 'On Leave','Resigned')) 
); 
/* Task 2 DDL*/
ALTER TABLE employee_performance 
ADD email VARCHAR(150) UNIQUE ; 

ALTER TABLE employee_performance
ADD bonus DECIMAL(10,2) DEFAULT 0;

ALTER TABLE employee_performance
RENAME COLUMN project_completed TO total_projects;

ALTER TABLE employee_performance
DROP COLUMN bonus; 

/* Task 3 DML */

INSERT INTO employee_performance 
(email_id, employee_name, department, salary, joining_date, experience_years, performance_score, total_projects, last_promotion_date, employee_status, email)
VALUES
(1,'Mubarak','IT',60000,'2020-05-10',5,4.5,12,'2023-06-15','Active','mubarak@gmail.com'),
(2,'Sadiq','HR',45000,'2019-03-12',6,4.2,8,NULL,'Active','sadiq@gmail.com'),
(3,'Arjun','Finance',70000,'2018-07-19',8,4.8,15,'2022-09-10','Active','arjun@gmail.com'),
(4,'Priya','Marketing',50000,'2021-01-25',4,3.9,7,NULL,'On Leave','priya@gmail.com'),
(5,'Vikram','Operations',55000,'2017-11-30',9,4.1,10,'2021-12-01','Active','vikram@gmail.com'),

(6,'Nisar','IT',62000,'2022-02-14',3,4.3,6,NULL,'Active','nisar@gmail.com'),
(7,'Raju','HR',40000,'2020-08-18',5,3.5,5,'2022-04-10','Resigned','raju@gmail.com'),
(8,'Meena','Finance',72000,'2016-09-23',10,4.9,18,'2023-03-12','Active','meena@gmail.com'),
(9,'Rohit','Marketing',48000,'2021-06-17',3,3.8,4,NULL,'Active','rohit@gmail.com'),
(10,'Suresh','Operations',53000,'2019-12-05',6,4.0,9,'2022-08-22','Active','suresh@gmail.com'),

(11,'Divya','IT',65000,'2018-04-21',7,4.6,14,'2023-01-10','Active','divya@gmail.com'),
(12,'Sindhu','HR',42000,'2021-09-11',2,3.7,3,NULL,'On Leave','sindhu@gmail.com'),
(13,'Lakshmi','Finance',75000,'2015-10-14',11,4.9,20,'2022-05-18','Active','lakshmi@gmail.com'),
(14,'Kavya','Marketing',51000,'2020-02-20',5,4.1,8,'2023-02-01','Active','kavya@gmail.com'),
(15,'Rajesh','Operations',56000,'2017-03-08',8,3.6,11,NULL,'Resigned','rajesh@gmail.com'),

(16,'Pooja','IT',63000,'2022-07-19',2,4.4,5,NULL,'Active','pooja@gmail.com'),
(17,'Ajay','HR',41000,'2019-05-30',6,3.9,6,'2022-11-11','Active','ajay@gmail.com'),
(18,'Neha','Finance',73000,'2016-01-16',10,4.7,17,'2023-04-04','Active','neha@gmail.com'),
(19,'Tarun','Marketing',49000,'2021-03-09',4,3.4,4,NULL,'Active','tarun@gmail.com'),
(20,'Harish','Operations',54000,'2018-12-27',7,4.2,12,'2022-07-15','Active','harish@gmail.com'); 

/* Task 4 DQL */

UPDATE employee_performance
SET salary = salary*1.10
WHERE department = 'IT' 
AND performance_score > 4.0 ; 

UPDATE employee_performance 
SET employee_status = 'On Leave'
WHERE performance_score < 2 ; 

UPDATE employee_performance 
SET Last_promotion_date ='CRUDATE' /* CRUDATE set current date automatically */
WHERE experince_years >5
AND oerformance_score > 4.5 ; 

UPDATE employee_performance 
SET salary = salary*0.95
WHERE total_projects < 2 ;  

/*task 5*/

DELETE FROM employee_performance
WHERE employee_status = 'Resigned'
AND last_promotion_date < DATE_SUB(CURDATE(), INTERVAL 2 YEAR);  

DELETE FROM employee_performance 
WHERE performance_score = 0
AND experience_years =0 ;
 

/*DQL :- */

SELECT *
FROM (
    SELECT employee_name, department, salary,
           ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rank_no
    FROM employee_performance
) AS ranked
WHERE rank_no <= 3; 

SELECT employee_name, department, salary
FROM employee_performance e
WHERE salary > (
    SELECT AVG(salary)
    FROM employee_performance
    WHERE department = e.department
); 

SELECT employee_name, joining_date
FROM employee_performance
WHERE joining_date >= DATE_SUB(CURDATE(), INTERVAL 3 YEAR); 

SELECT department,
       AVG(performance_score) AS avg_performance
FROM employee_performance
GROUP BY department; 

SELECT employee_status,
       COUNT(*) AS total_employees
FROM employee_performance
GROUP BY employee_status; 

/*Advanced Queries*/
SELECT department, employee_name, salary
FROM (
    SELECT department, employee_name, salary,
           DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rnk
    FROM employee_performance
) AS ranked
WHERE rnk = 2; 

SELECT e.employee_name, e.department, e.salary
FROM employee_performance e
WHERE e.salary > (
    SELECT MAX(salary)
    FROM employee_performance
    WHERE department = e.department
    AND experience_years < 3
); 

SELECT employee_name, last_promotion_date, performance_score
FROM employee_performance
WHERE performance_score > 4
AND (
      last_promotion_date IS NULL
      OR last_promotion_date < DATE_SUB(CURDATE(), INTERVAL 3 YEAR)
); 

SELECT employee_name, performance_score
FROM employee_performance
WHERE performance_score > (
    SELECT AVG(performance_score)
    FROM employee_performance
); 

SELECT department, employee_name, performance_score,
       RANK() OVER (PARTITION BY department ORDER BY performance_score DESC) AS dept_rank
FROM employee_performance; 

/* Window Function Challenges*/

SELECT department,
       employee_name,
       salary,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank_salary,
       DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dense_rank_salary
FROM employee_performance; 

SELECT employee_name,
       joining_date,
       salary,
       SUM(salary) OVER (ORDER BY joining_date) AS running_total
FROM employee_performance; 

SELECT employee_name,
       department,
       salary,
       ROUND(
           (salary / SUM(salary) OVER (PARTITION BY department)) * 100, 2
       ) AS salary_percentage
FROM employee_performance; 

SELECT employee_name, salary
FROM employee_performance
WHERE salary > (
    SELECT MAX(salary) * 0.80
    FROM employee_performance
); 

SELECT employee_name,
       performance_score,
       PERCENT_RANK() OVER (ORDER BY performance_score DESC) AS percent_rank
FROM employee_performance; 

SELECT *
FROM (
    SELECT employee_name,
           performance_score,
           PERCENT_RANK() OVER (ORDER BY performance_score DESC) AS percent_rank
    FROM employee_performance
) AS ranked
WHERE percent_rank <= 0.20; 

/*Subquery Challenges*/

SELECT employee_name, department, salary
FROM employee_performance
WHERE salary > (
    SELECT MAX(salary)
    FROM employee_performance
    WHERE department = 'HR'
);

SELECT department, AVG(salary) AS avg_salary
FROM employee_performance
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 1; 

SELECT employee_name, salary
FROM employee_performance
WHERE salary < (
    SELECT AVG(salary)
    FROM (
        SELECT salary
        FROM employee_performance
        ORDER BY salary
        LIMIT 2 - (SELECT COUNT(*) FROM employee_performance) % 2
        OFFSET (SELECT (COUNT(*) - 1) / 2 FROM employee_performance)
    ) AS median_table
); 

SELECT e.employee_name,
       e.department,
       e.performance_score
FROM employee_performance e
WHERE performance_score = (
    SELECT MAX(performance_score)
    FROM employee_performance
    WHERE department = e.department
);
 
SELECT DISTINCT e1.employee_name,
       e1.department,
       e1.salary
FROM employee_performance e1
JOIN employee_performance e2
ON e1.salary = e2.salary
AND e1.department <> e2.department;

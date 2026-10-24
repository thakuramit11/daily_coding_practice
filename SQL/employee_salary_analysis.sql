
-- 1. Employees earning more than 40000
SELECT *
FROM Employees
WHERE salary > 40000;

-- 2. Average salary in each department
SELECT department, AVG(salary) AS avg_salary
FROM Employees
GROUP BY department;

-- 3. Employee with the highest salary
SELECT *
FROM Employees
WHERE salary = (SELECT MAX(salary) FROM Employees);


-- Write a query to display employees whose salary is 
-- greater than the average salary of all employees.

SELECT *
FROM Employees
WHERE salary > (
    SELECT AVG(salary)
    FROM Employees
);
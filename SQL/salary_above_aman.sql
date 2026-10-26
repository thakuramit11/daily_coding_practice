-- Find employees earning more than Aman

SELECT *
FROM Employees
WHERE salary > (
    SELECT salary
    FROM Employees
    WHERE emp_name = 'Aman'
);
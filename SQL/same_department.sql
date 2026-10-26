-- Find employees working in the same department as Aman

SELECT *
FROM Employees
WHERE department = (
    SELECT department
    FROM Employees
    WHERE emp_name = 'Aman'
);
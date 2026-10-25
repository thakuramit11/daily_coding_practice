-- Display the employee or employees who receive the highest salary.

SELECT *
FROM Employees
WHERE salary = (
    SELECT MAX(salary)
    FROM Employees
);

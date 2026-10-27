-- Find employees earning above their department's average salary,
-- but only in departments whose average salary is above the company's overall average.

SELECT emp_id, emp_name, department, salary
FROM Employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM Employees
    WHERE department = e.department
)
AND department IN (
    SELECT department
    FROM Employees
    GROUP BY department
    HAVING AVG(salary) > (
        SELECT AVG(salary)
        FROM Employees
    )
);

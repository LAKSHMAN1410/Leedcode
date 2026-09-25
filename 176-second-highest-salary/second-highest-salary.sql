-- Write your PostgreSQL query statement below
SELECT 
(SELECT DISTINCT salary FROM
(SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rmd FROM Employee
)AS denserank
WHERE rmd=2
)AS SecondHighestSalary;
-- 각 부서의 최고 연령 직원과 해당 부서의 평균 연령을 함께 조회
SELECT d.name AS department,
       e.name AS oldest_employee,
       MAX(e.age) AS max_age,
       AVG(e.age) AS avg_age
FROM employees e
JOIN departments d ON d.id = e.departmentId
GROUP BY d.name;

-- 부서별로 가장 많은 급여를 받는 직원의 정보와 그 급여를 함께 조회
SELECT d.name AS department,
       e.name AS highest_paid_employee,
       MAX(salary) AS max_salary
FROM employees e
JOIN departments d ON d.id = e.departmentId
GROUP BY d.name;

-- 부서별로 연령대 별 직원 수를 조회
SELECT d.name AS department,
       CASE
           WHEN e.age < 30 THEN 'Under 30'
           WHEN e.age BETWEEN 30 AND 40 THEN 'BETWEEN 30-40'
           ELSE 'Over 40'
       END AS age_group,
       COUNT(*) AS num_employees
FROM employees e
JOIN departments d ON d.id = e.departmentId
GROUP BY department, age_group
ORDER BY department, age_group;

-- 부서별로 최고 급여를 받는 직원을 제외한 평균 급여 조회
SELECT d.name AS department,
       AVG(e.salary) AS avg_salary_excluding_hightest
FROM employees e
JOIN departments d ON d.id = e.departmentId
WHERE (e.salary, e.departmentId) NOT IN (
    SELECT MAX(salary), departmentId
    FROM employees e
    GROUP BY departmentId
)
GROUP BY department;
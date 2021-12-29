# Write your MySQL query statement below

with high_salary as
(
    select name,dense_rank() over(partition by departmentid order by salary desc) as rn, departmentid,salary
    from employee
    
)
select d.name as Department, e.name as Employee, Salary
from department d, high_salary e
where d.id = e.departmentid
and e.rn <=3

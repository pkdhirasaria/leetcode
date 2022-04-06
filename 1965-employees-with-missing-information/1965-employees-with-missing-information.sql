# Write your MySQL query statement below
select COALESCE(Emp_id,S_id) as employee_id
from 
((select e.employee_id as Emp_id, e.name, s.employee_id as S_id,s.salary from Employees e left join Salaries s on e.employee_id =s.employee_id )
union 
(select e.employee_id as Emp_id, e.name, s.employee_id as S_id,s.salary from Employees e right join Salaries s on e.employee_id =s.employee_id )) a
where a.name is null or a.salary is null
order by 1
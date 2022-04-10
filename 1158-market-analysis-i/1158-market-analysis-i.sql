# Write your MySQL query statement below
select buyer_id,join_date,
    sum(case when extract(year from o.order_date) = '2019' then 1 else 0 end) as 'orders_in_2019'
from Users u join orders o on o.buyer_id = u.user_id
# where extract(year from o.order_date) = '2019'
group by 1
union all
select user_id,join_date,0 as 'orders_in_2019'
from users u 
where u.user_id not in (select distinct buyer_id from orders)
# where extract(year from o.order_date) = '2019'
# group by 1

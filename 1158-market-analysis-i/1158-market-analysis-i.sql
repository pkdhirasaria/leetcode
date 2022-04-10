# Write your MySQL query statement below
select coalesce(buyer_id,user_id) as buyer_id,join_date,
    sum(case when extract(year from o.order_date) = '2019' then 1 else 0 end) as 'orders_in_2019'
from Users u left join orders o on o.buyer_id = u.user_id
# where extract(year from o.order_date) = '2019'
group by 1

# Write your MySQL query statement below
with prev_end_date as (
    select *,
     max(end_day) over(partition by hall_id order by start_day) as max_end
    from HallEvents
),p as (select *,lag(max_end) over(partition by hall_id order by start_day) as prev_max_end
from prev_end_date),q as (select *, sum(case when prev_max_end < start_day then 1 else 0 end) over(partition by hall_id order by start_day,end_day) as cnt
from p
order by hall_id,start_day)




select hall_id,min(start_day) as start_day, max(end_day) as end_day
from q
group by 1,cnt

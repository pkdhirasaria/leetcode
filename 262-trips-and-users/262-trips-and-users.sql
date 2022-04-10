select 
    request_at as Day, 
    # sum(case when status like 'can%' then 1 else 0 end),
    # count(*),
    round(sum(case when status like 'can%' then 1 else 0 end)
        /count(*),2) as 'Cancellation Rate'
from trips t
where client_id not in (select users_id from Users where banned = "Yes") and driver_id not in (select users_id from Users where banned = "Yes")
and request_at between '2013-10-01' and '2013-10-03'
group by 1

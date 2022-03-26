# Write your MySQL query statement below
with leaf as (
    select id, 'Leaf' as type from tree a
    where id not in (select p_id from tree where a.id = p_id) and p_id is not null
), inner_l as (
    select id, 'Inner' as type from tree a
    where id in (select p_id from tree where a.id = p_id) and p_id is not null
), root as (
    select id, 'Root' as type from tree
    where p_id is null
)
select * from leaf
union 
select * from inner_l
union 
select * from root
order by id
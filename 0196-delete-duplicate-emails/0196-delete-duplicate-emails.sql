# Write your MySQL query statement below
delete e from Person e
join Person e1
on e.email=e1.email
where e.id>e1.id
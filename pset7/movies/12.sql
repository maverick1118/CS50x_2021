select title from stars
join movies on stars.movie_id = movies.id
join people on stars.person_id = people.id
where name = 'Johnny Depp'
intersect
select title from stars
join movies on stars.movie_id = movies.id
join people on stars.person_id = people.id
where name = 'Helena Bonham Carter'
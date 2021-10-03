select distinct(name) from stars
join movies on stars.movie_id = movies.id
join people on stars.person_id = people.id
where movies.id in
    (select movies.id from stars
    join movies on stars.movie_id = movies.id
    join people on stars.person_id = people.id
    where name = 'Kevin Bacon' and birth = 1958)
and name != 'Kevin Bacon'
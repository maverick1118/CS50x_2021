select name from stars
join people on stars.person_id = people.id
join movies on stars.movie_id = movies.id
where title = 'Toy Story' 
select title from stars
join movies on stars.movie_id = movies.id
join people on stars.person_id = people.id
join ratings on stars.movie_id = ratings.movie_id
where people.name = 'Chadwick Boseman'
order by ratings.rating  desc
limit 5;
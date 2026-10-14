-- queries with aggregations
-- retrieve the number of movies by year
-- expected output
year | number_of_movies
1963		4
1964		5
...
2020    11

-- solution sorting result by number of movies in descending mode
select year, count(*) as number_of_movies 
from imdb.movie 
group by year
order by number_of_movies  desc


-- retrieve the years after 2010 in which more than 10 movies have been produced
select year, count(*) as number_of_movies 
from imdb.movie
where year > '2010'
group by "year"
having count(*)> 10
order by number_of_movies  desc


-- for each movie, retrieve the number of persons involved for each role 
-- expected output
001  actor	3
001	director 1
002	 producer 2
002 actor	23

select movie, p_role, count(*)
from imdb.crew 
group by p_role, movie
order by movie, p_role 

-- return the movie title and the number of persons per role 
-- is it possible that two movies in a group have different titles? no
-- expected output
0013444 actor  2
0013444 director 1
0013444 producer 3 

select movie, official_title, p_role, count(*)
from imdb.crew inner join imdb.movie on movie.id = crew.movie 
group by p_role, movie, official_title
order by movie, p_role 


-- retrieve the average movie length for each year (sorted) 


-- retrieve the number of persons by role


-- retrieve the movies with more than 10 actors in the crew 


-- retrieve the persons that played more than one role 
select person, count(*), count(p_role), count(distinct p_role)
from imdb.crew
group by person  
having count(distinct p_role) > 1


-- for each movie, return the number of genres
-- in this solution we are not considering movies without genre
select movie, count(*), count(genre) 
from imdb.genre 
group by movie 




-- to include movies without genre, use left join
-- example of records
movie.id | ... | movie  | genre 
001				 001			thriller
001				 001 		drama
002				 002			Comics 
003				 [null]     [null]

select movie.id, count(*), count(genre) 
from imdb.movie left join imdb.genre on movie.id = genre.movie 
group by movie.id


 
-- return the number of movies produced in each country 
iso3 | name 			| movie | country
USA		united...		001		USA
USA		united...		002		USA
USA		united...		003		USA
ITA		Italy			001		ITA
ALB		Albania			[null]  [null]
NIG						[null]  [null]


select iso3, count(movie)
from imdb.country left join imdb.produced on country.iso3 = produced.country 
group by iso3 


-- for each person, count the number of movies (all roles - including persons with zero movies)
-- consider that a person can participate in a movie twice - use the proper version of count if you wnat to count all the participations in a movie or just once


-- for each person, count the number of movies (only as actor - including persons with zero movies)


-- for each country, count the number of persons born there (including countries without persons born)
-- hint: use the table location with d_role = 'B'


-- retrieve the best rating score for each movie 
select movie, max(score/scale) as top_rating
from imdb.rating 
group by movie 


-- retrieve the title of movies whose length is greater than Marnie (movie title)
-- what happens when you have more than one movie with title Marnie
-- sql operator for comparison on sets of values: ANY, ALL 
-- 001 Marnie 	112
-- 002 Marnie   150
select id, official_title
from imdb.movie 
where length > any (
select length
from imdb.movie 
where official_title = 'Marnie');

-- alternative
select id, official_title
from imdb.movie 
where length > (
select min(length)
from imdb.movie 
where official_title = 'Marnie');

003 M1 90 -> not in the result
004 M4 130 -> this is in the result 
005 M5 160 -> this is in the result 

-- solution with ALL 
select id, official_title
from imdb.movie 
where length > ALL (
select length 
from imdb.movie 
where official_title = 'Marnie');

-- alternative
select id, official_title
from imdb.movie 
where length > (
select max(length)
from imdb.movie 
where official_title = 'Marnie');

003 M1 90 -> not in the result
004 M4 130 -> not in the result
005 M5 160 -> this is in the result 


-- try to solve the query with self-join 


-- return the title of movies whose length is greater that the average of movies from the same year 
-- this is a correlated query
select id, official_title
from imdb.movie m1
where length > (
select avg(length)
from imdb.movie m2
where m1.year = m2.year)

-- alternative solution (but less smart than the previous one)
create view imdb.m_length_by_year as (
select year, avg(length) as avg_length
from imdb.movie 
group by year);

select id, official_title
from imdb.movie m1
where length > (
select avg_length 
from imdb.m_length_by_year m2
where m1.year = m2.year);


-- think about a solution with self-join 




-- retrieve the actor that played the highest number of movies as actor
-- this solution is wrong: you cannot apply an aggregate function to another aggregate funciton
select person, max(count(movie))
from imdb.crew 
where p_role = 'actor'
group by person;


-- this is not a correct solution as well
select person, count(movie) as p_count
from imdb.crew 
where p_role = 'actor'
group by person
order by p_count desc;


-- solution with view 
create view imdb.person_movie_counts as (
select person, count(movie) as p_count
from imdb.crew 
where p_role = 'actor'
group by person)

select *
from imdb.person_movie_counts
where p_count = (
select max(p_count)
from imdb.person_movie_counts);

-- smarter solution 
select person, count(movie) as p_count
from imdb.crew 
where p_role = 'actor'
group by person
having count(movie) >= all (
select count(movie)
from imdb.crew 
where p_role = 'actor'
group by person);


person | count(movie)
p1		   5
p2 		   3
p3         6 *** 

the subquery returns the set: 5, 3, 6 
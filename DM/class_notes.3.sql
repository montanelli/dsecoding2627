-- retrieve the directors of thriller movies (consider table genre)
select distinct person 
from imdb.crew, imdb.genre 
where crew.movie = genre.movie and p_role = 'director' and lower(genre) = 'thriller'

-- syntax with join operation fully specified in the from clause
-- inner means that we insert in the result only records that satisfy the join condition 
select distinct person 
from imdb.crew inner join imdb.genre on crew.movie = genre.movie 
where p_role = 'director' and lower(genre) = 'thriller'

-- retrieve the countries without produced movies
-- we start by finding countries and corresponding produced movies
select iso3  
from imdb.country inner join imdb.produced on country.iso3 = produced.country 

country
iso3 | name
POL		Poland
USA		United States
GBR		Great Britain


produced 
movie | country
001		USA
002		GBR


country inner join produced on country.iso3 = produced.country 
iso3 | name 				| movie | country 
USA 		United States 		001		USA
GBR		Great Britain	    002		GBR


-- external joins: LEFT, RIGHT, FULL JOIN
-- left join: the result is the result of inner join + spurious record in the table on the left
select iso3  
from imdb.country left join imdb.produced on country.iso3 = produced.country 

country left join produced on country.iso3 = produced.country 
iso3 | name 				| movie | country 
USA 		United States 		001		USA
GBR		Great Britain	    002		GBR
POL	    Poland			   [null]	[NULL]

-- now, we take countries that are not involved in produced by filtering the result of the left join
select iso3, name 
from imdb.country left join imdb.produced on country.iso3 = produced.country 
where produced.country is null;

-- right join: the result is the result of inner join + spurious records in the table on the right
select iso3, name 
from imdb.produced right join imdb.country on country.iso3 = produced.country 
where produced.country is null;

produced right join country on country.iso3 = produced.country 
	movie | country 		| iso3 | name 				
	001		USA			| USA 		United States 	
    002		GBR			| GBR		Great Britain	  
   [NULL]   [NULL]		| POL		Poland
   
-- FULL JOIN: result of inner join + spurious records of the left table + spurious records of the right table 
   

-- retrieve the movies that are never rated 
-- movie (id, official_title, ...)
-- rating (check_date, source, movie, ..., score)
select 
from imdb.movie left join imdb.rating on movie.id = rating.movie 
where rating.movie is null; 


-- retrieve the country in which movies are not produced



-- retrieve the movies in which both Leonardo DiCaprio and Thomas Hardy are involved as actors
create view imdb.actor_movies
as (
select person.id, given_name, movie
from imdb.person inner join imdb.crew on person.id = crew.person
where p_role = 'actor');

-- this solution is not correct 
select *
from imdb.actor_movies 
where given_name = 'Tom Hardy' and given_name = 'Leonardo DiCaprio';

-- use subquery
select movie
from imdb.actor_movies 
where given_name = 'Tom Hardy' and movie in (
select movie
from imdb.actor_movies 
where given_name = 'Leonardo DiCaprio');

-- use self-join
select *
from imdb.actor_movies m1, imdb.actor_movies m2
where m1.given_name = 'Tom Hardy' and m2.given_name = 'Leonardo DiCaprio' and m1.movie = m2.movie

select *
from imdb.actor_movies m1 inner join imdb.actor_movies m2 on m1.movie = m2.movie
where m1.given_name = 'Tom Hardy' and m2.given_name = 'Leonardo DiCaprio' 


-- retrieve the movies with italian or france directors


-- retrieve the movies produced in both Italy and USA


-- solution based on self-join


-- solution based on subquery


-- retrieve the movies produced only in Italy
-- the movie is produced in ITA and the movie is not produced in another country
-- produced(movie, country)
-- using subquery:
select movie
from imdb.produced 
where country = 'ITA' and movie not in (
select movie
from imdb.produced 
where country <> 'ITA')

-- using self-join: not working (the movie 002 is returned but it is not produced only in ITA)
select p1.movie
from imdb.produced p1, imdb.produced p2 
where p1.country = 'ITA' and p2.country <> 'ITA' and p1.movie = p2.movie 

-- running over the istances
produced
movie  | country
001			ITA
002			USA
002			ITA

p1.movie  | p1 country  | p2.movie  |  p2.country
001				ITA			001				ITA    X
001				ITA			002				USA    X
001				ITA			002				ITA    X
002				USA			001				ITA    X
002				USA			002				USA    X
002				USA			002				ITA    X
002				ITA			001				ITA    X
002				ITA			002				USA    ok: returned, but wrong
002				ITA			002				ITA    X


-- correct version:
-- the conditions in the join clause are evaluated before those in where clause
-- spurious tuples are calculated according to the two conditions in the join clause
-- the last row of the example below is the spurious record added with left join
-- the last row is the only one returned and it is correct
select p1.movie
from imdb.produced p1 left join imdb.produced p2 on p2.country <> 'ITA' and p1.movie = p2.movie 
where p1.country = 'ITA' AND p2.movie is null

p1.movie  | p1 country  | p2.movie  |  p2.country      
001				ITA			001			ITA   X (not satisfying the join condition) 
001				ITA			002			USA   X (not satisfying the join condition)  
001				ITA			002			ITA   X (not satisfying the join condition)  
002				USA			001			ITA   X (not satisfying the join condition)  
002				USA			002			USA   X (not satisfying the where condition)
002				USA			002			ITA   X (not satisfying the join condition)  
002				ITA			001			ITA   X (not satisfying the join condition)  
002				ITA			002			USA   X (not satisfying the where condition) 
002				ITA			002			ITA   X (not satisfying the join condition)   
001			    ITA         [NULL]      [NULL] ok

-- retrieve the movies without italian actors
-- crew(movie, person, p_role, ...)
-- location(person, country, d_role) 
select movie 
from imdb.crew inner join imdb.location on crew.person = location.person 
where p_role = 'actor' and d_role = 'B' and country <> 'ITA';


crew
person | movie | p_role
001		 ABC		  actor
002		 DEF		  actor
001		 DEF		  actor
003		 EFG		  actor

location
person | country | d_role
001		  ITA		B
002		  USA		B 
003		  GBR		B

imdb.crew inner join imdb.location on crew.person = location.person
person | movie | p_role | person | country | d_role
001		 ABC		  actor		001		  ITA		B
002		 DEF		  actor		002		  USA		B 
001		 DEF		  actor		001		  ITA		B
003		 EFG		  actor		003		  GBR		B

-- the solution below is wrong: DEF and EFG are returned but DEF involves an italian actor. This happens because the movies are evaluated record by record but the decision to include/exclude a movie from the result must be taken considering all the actors involved 
select movie 
from imdb.crew inner join imdb.location on crew.person = location.person 
where p_role = 'actor' and d_role = 'B' and country <> 'ITA';

-- correct solutiony, only the movie DEF is returned:
select movie
from crew
where p_role = 'actor' and movie not in 
(select movie  
from imdb.location inner join imdb.crew on crew.person = location.person 
where d_role = 'B' and country = 'ITA')


crew
person | movie | p_role
001		 ABC		  actor 
002		 DEF		  actor
001		 DEF		  actor 
003		 EFG		  actor ** finally returned

imdb.crew inner join imdb.location on crew.person = location.person
person | movie | p_role | person | country | d_role
001		 ABC		  actor		001		  ITA		B ** excluded
002		 DEF		  actor		002		  USA		B 
001		 DEF		  actor		001		  ITA		B ** excluded
003		 EFG		  actor		003		  GBR		B


-- retrieve the movies in which a person is both actor and director
-- hint: solve with self-join



-- retrieve the movie with highest/lowest/avg length
-- aggregate functions: 
-- argument is atomic values (single attributes)
--- max, min 
--- sum 
--- avg 
--- count 

select max(length) 
from imdb.movie 

select min(length) 
from imdb.movie 

select avg(length) 
from imdb.movie 

-- retrieve the average duration of movies produced in 2010
select avg(length) 
from imdb.movie
where year = '2010';

-- return also code and title of the movie in the previous query
select official_title, max(length) 
from imdb.movie 

select id, official_title, length
from imdb.movie 
where length = (
select max(length) 
from imdb.movie)

-- return the title of movies with minimum length
select id, official_title, length
from imdb.movie 
where length = (
select min(length) 
from imdb.movie)

-- retrieve the overall length of 2010 movies
select sum(length) 
from imdb.movie
where year = '2010';

-- retrieve the number of stored movies
select count(*)
from imdb.movie

-- retrieve the number of stored movies for which the title is defined
-- use(count <attribute>)
select count(*), count(official_title)
from imdb.movie

-- retrieve the number of movies with year of production 
-- use(count <attribute>)
select count(year), count(*)
from imdb.movie 

-- alternative solution
select count(*)
from imdb.movie m 
where year is not null;


-- retrieve the number of movies with different title
-- use count(distinct <attribute>)
select count(official_title), count(distinct official_title), count(*)
from imdb.movie 
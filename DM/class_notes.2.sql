CREATE TABLE imdb.country (
    iso3 char(3) PRIMARY KEY,
    name varchar(20) UNIQUE NOT NULL
);

CREATE TABLE imdb.movie (
	id varchar(10) NOT NULL PRIMARY KEY,
	official_title varchar(200) NOT NULL,
	budget numeric(12, 2),
	"year" char(4),
	length integer,
	plot text NULL UNIQUE,
	CONSTRAINT length_check CHECK ((length > 0)),
	UNIQUE(official_title, year),
	UNIQUE(official_title, length)
);

CREATE TABLE imdb.produced (
    movie varchar(10) NOT NULL REFERENCES movie(id) ON UPDATE NO ACTION ON DELETE NO ACTION,
    country char(3) NOT NULL REFERENCES country(iso3) ON DELETE NO ACTION,
    PRIMARY KEY(movie, country)
)

-- DML commands (insert, delete, update)

-- Examples on referential integrity
-- consider the following commands and discuss the possible errors that can raise
-- consider to have a policy ON UPDATE CASCADE on produced.movie and a policy ON DELETE CASCADE on produced.country. What can happen when you execute the following commands?
INSERT INTO imdb.produced VALUES ('0338751', 'USA');
UPDATE imdb.produced SET movie = '0097576' WHERE movie = '0338751';

UPDATE imdb.movie SET id = 'AVAVA' WHERE id = '0338751';
DELETE FROM imdb.country WHERE name = 'Germany';
DELETE FROM imdb.movie WHERE year = '2010';

-- example on strict concurrency
-- in this example, the final balance is wrong
-- the notion of transaction of relational database allows to prevent that such situations occur (isolation property)
user B: read the balance (Euros 100)
user A: read the balance (Euros 100)

user B: write the deposit (Euros 100 + 50)
user A: write the deposit (Euros 100 + 75)


-- DQL - data query language

-- extract/retrieve the records of the table movie 
select *
from imdb.movie 

-- extract/retrieve the records of the table movie but show only id, title, year 
select id, official_title, year 
from imdb.movie

-- extract/retrieve the records of the table movie but show only id, title, year and show only movies from 2010 
select id, official_title, year 
from imdb.movie
where year = '2010'

-- =, <>, >=, <= 
-- between, in, like, is null
-- lower, upper, trim
-- attribute aliases 
-- distinct


-- retrieve all the attributes of movies of 2010 with length greater than one hour
select *
from imdb.movie
where year = '2010' and length > 60


-- retrieve all the attributes of movies of 2010 with length betweem 1 and 2 hours (excluding extremes)


-- retrieve all the attributes of movies not realized in 2010 with length betweem 1 and 2 hours (including extremes) 
-- precedence of operators are from left to right
select *
from imdb.movie
where year <> '2010' and (length >= 60 and length <= 120)

-- alternative syntax
select *
from imdb.movie
where year <> '2010' and (length between 60 and 120)

-- sort the result of the previous query according to year
select *
from imdb.movie
where year <> '2010' and (length between 60 and 120)
order  by year desc, official_title asc 

-- are movies with null on year included in the result of the previous query?
-- null values are not comparable so not considered in normal comparisons

-- retrieve the persons whose death date is known
select *
from imdb.person 
where death_date is not null;

-- retrieve the persons that are not dead
select *
from imdb.person 
where death_date is null;

-- create a view with name, birth date and death date of persons whose death date is known
create view imdb.dead_people as (
select id, given_name, birth_date, death_date 
from imdb.person
where death_date is not null);

-- return the person with death_date in 1982
-- we use the view as a source (as it is a table)
select *
from imdb.dead_people
where death_date between '1982-01-01' and '1982-12-31'


-- retrieve the title of movies of 2010 or 2011 or 2012
select id, official_title 
from imdb.movie 
where year = '2010' or year = '2011' or year = '2012'

-- alternative solution with in operator
-- rename the attributes in the select clause
select id as movie_id, official_title as "movie title"
from imdb.movie 
where year IN ('2010','2011','2012');


-- retrieve the persons that have "Mark" in the given name
-- we need an operator to perform approximate match: like
-- postgres supports also the ilike operator that is the insensitive like 
-- like uses a placeholder to denote where to be flexible.
-- the % placeholder is used to denote any string
-- the _ placeholder is used to denote a string of exactly one char
select id, given_name
from imdb.person 
where given_name like '%Mark%';

-- retrieve the movie with title inception
select id, official_title
from imdb.movie 
where official_title = 'Inception';

-- possible way to workaround capital letters
select id, official_title
from imdb.movie 
where official_title like '_nception';

select id, official_title
from imdb.movie 
where lower(official_title) = 'inception';

select id, official_title
from imdb.movie 
where upper(official_title) = 'INCEPTION';

-- check for ucwords
select id, official_title
from imdb.movie 
where ucwords(official_title) = 'Inception';

-- retrieve the persons that have "Mark" as first name
select id, given_name
from imdb.person 
where given_name like 'Mark %';


-- retrieve the persons that have "Mark" as last name
select id, given_name
from imdb.person 
where given_name like '% Mark';


-- retrieve the title of movies of 2010 or length between one and two hours;


-- retrieve the title of movies produced in USA
select movie
from imdb.produced 
where country = 'USA'

select id, official_title
from imdb.movie 
where id in (< the result of the previous query>)

-- solution with subquery/nested query
select id, official_title
from imdb.movie 
where id in (
select movie
from imdb.produced 
where country = 'USA');

-- solution with join operation

-- step1: build the cartesiano product of the involved tables 
select *
from imdb.movie, imdb.produced 

movie 
id | title ...
====
001		movie1
002		movie2

produced
movie | country
================
001		USA
001		GBR
002		ITA

movie x produced
id  | title | ...| movie | country 
==================================
001	 movie1			001		USA *
001	 movie1			001		GBR
001	 movie1			002		ITA
002	 movie2			001		USA *
002	 movie2			001		GBR
002	 movie2			002		ITA

-- step2: filter the cartesian product to get the records where production is from USA and where produced.movie = movie.id 
-- this is a join operation 
select *
from imdb.movie, imdb.produced 
where country = 'USA' and produced.movie = movie.id

-- retrieve the title of movies with rating > 8/10
select id, official_title, scale, score, score/scale as "ratio score on scale"
from imdb.movie, imdb.rating 
where movie.id = rating.movie and score/scale > 0.8

-- retrieve the name of persons that are actors
select id, given_name 
from imdb.person, imdb.crew
where p_role = 'actor' and person.id = crew.person;

-- alternative syntax
-- sort the result by given_name
-- show the actor only once even if they appear in many movies
select distinct id, given_name 
from imdb.person inner join imdb.crew on id = person
where p_role = 'actor'
order by given_name;

-- retrieve the name of actors and corresponding movie titles
select distinct person.id as person_id, given_name, movie.id as movie_id, official_title 
from imdb.person inner join imdb.crew on person.id = person inner join imdb.movie on movie.id = movie 
where p_role = 'actor'
order by given_name; 


-- retrieve the countries in which movies of 2010 have been released (consider the table released and return the movie title, both the official and the released one (where available))


-- retrieve the movies for which the title released in Italy is not defined

-- retrieve the name of actors in the movie Inception


-- retrieve the actors that joined movies of 2010


-- retrieve the directors of thriller movies (consider table genre)




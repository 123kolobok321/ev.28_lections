# Task1
# SELECT plaintext FROM wordform LIMIT 10;

# Task2
# SELECT plaintext FROM wordform WHERE plaintext ILIKE 'a%';

# Task 3
# SELECT title, genretype FROM work WHERE genretype = 'p';

# Task 4
# SELECT avg(totalparagraphs) FROM work WHERE genretype = 't';
# SELECT AVG(totalparagraphs) FROM work WHERE genretype = 't';

# Task 5
# SELECT title FROM work WHERE totalwords > (SELECT AVG(totalwords) FROM work);


# CREATE TABLE films (
# code char(5),
# title varchar(100),
# date date,
# ganre varchar(50),
# budget integer,
# country varchar(50),
# id serial
# );



























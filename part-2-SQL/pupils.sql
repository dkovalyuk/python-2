pragma foreign_keys = on

----------------------------------
-- 1. Написати запит, який вставляє запис (INSERT INTO) в таблицю pupils 

INSERT INTO pupils(name, birthday, gender)
VALUES('Oleg', '2000-01-01', 1);


-- 2. Написати запит, який вставляє запис (INSERT INTO) в таблицю courses 
INSERT INTO courses
VALUES(5, 'AI', 0, 'python');


-- 3. Написти запит, який оновлює (UPDATE) дані в таблиці courses
UPDATE courses
SET title='Artificial Intelligence'
WHERE id=5;

UPDATE courses
SET lang='Java Script', is_children = 0
WHERE id IN (13,14);


-- 4. Написати запит, який вибирає найбільший бал з курсу Python
SELECT MAX(rating) FROM school s 
WHERE course_id in (SELECT id FROM courses c WHERE lang = 'python')


-- 5. Написати запит, який виводить курси, які пройшли студенти зі Львова
SELECT c.title as course_title
  FROM courses c, school s, pupils_address pa
 WHERE pa.id = s.pupil_id
   AND s.course_id = c.id
   AND address = 'Львів'
   ORDER BY course_title


-- 6. Написати запит, який виводить інформацію про курси дівчат, відсортовані по спаданню
SELECT c.title as course_title
  FROM courses c, school s, pupils p
 WHERE p.id = s.pupil_id
   AND s.course_id = c.id
   AND gender = 2
   ORDER BY course_title
   
   
   
-- 7. Написти запит, який видаляє запис про навчання студента (таблиця school) за його іменем 
  
DELETE FROM school
WHERE pupil_id IN (SELECT id FROM pupils p WHERE name LIKE 'Сідоров%');



----------------------------------------------------------------------------------------------

SELECT DISTINCT pupil_id FROM school s  ORDER BY pupil_id 


SELECT DISTINCT course_id  FROM school s 


select s.pupil_id, c.title as course_title,  p.name, p.birthday  
from school AS s 
INNER JOIN pupils AS p ON p.id = s.pupil_id 
INNER JOIN courses c ON c.id = s.course_id 
WHERE c.is_children = 1
order by title 


select s.pupil_id, c.title, p.name, p.birthday  
from school s, pupils p, courses c 
WHERE p.id = s.pupil_id 
  AND c.id = s.course_id 
  AND c.is_children = 1
order by title 
	

SELECT p.*, pa.address from pupils p   
INNER JOIN pupils_address AS pa ON p.id = pa.id 


SELECT p.*, pa.address from pupils p   
LEFT JOIN pupils_address AS pa ON p.id = pa.id 
ORDER BY  gender  


SELECT COUNT(pupil_id) from school s 
WHERE course_id = 1


SELECT 
	MIN(birthday) as min_bith, 
	MAX(birthday) as max_bith 
from pupils p 


SELECT MIN(rating), MAX(rating), AVG(rating), SUM(rating), COUNT(rating)  
FROM school s 
WHERE course_id in (1, 2)


select course_id, title, count(pupil_id), avg(rating) 
from school s, courses c 
WHERE s.course_id = c.id 
GROUP BY course_id
HAVING avg(rating) > 80
order by avg(rating)


select pupil_id, p.name, count(course_id) as course_count
from school s, pupils p  
WHERE s.pupil_id = p.id 
GROUP BY pupil_id
ORDER BY course_count DESC 


SELECT DISTINCT pupil_id, name 
FROM school s
INNER JOIN pupils p on s.pupil_id = p.id  
WHERE course_id in (1, 2)


SELECT course_id, COUNT(course_id) as course_times, AVG(rating) as avg_rating  
FROM school s
GROUP BY course_id
HAVING course_times > 2

UPDATE pupils
SET name='Dmytro', birthday = '2000-11-22'
WHERE id = 25;

UPDATE courses
SET is_children = 10
WHERE lang = 'python';


DELETE FROM pupils WHERE id = 25;


SELECT * FROM pupils p order by id 
 LIMIT 2 
OFFSET 3















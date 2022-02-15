pragma foreign_keys = on


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




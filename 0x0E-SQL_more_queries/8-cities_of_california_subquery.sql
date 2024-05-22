-- lists all the cities of California in database
SELECT id, name FROM cities
WHERE state_id = (
	SELECT id FROM states
	WHERE NAME = "California")
ORDER BY id;

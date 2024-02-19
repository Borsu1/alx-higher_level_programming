# Script that displays the top 3 of cities temperature during July and August ordered by temperature

USE hbtn_0c_0;

SELECT city, AVG(temperature) AS average_temperature
FROM weather_data
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY average_temperature DESC
LIMIT 3;

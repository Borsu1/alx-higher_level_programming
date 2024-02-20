-- Script that displays the top 3 of cities temperature during July and August ordered by temperature

USE hbtn_0c_0;

SELECT `city`, AVG(`value`) AS `average_temperature`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `average_temperature` DESC
LIMIT 3;

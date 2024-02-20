-- Script that displays the max temperature of each state (ordered by State name)

USE hbtn_0c_0;

SELECT `state`, MAX(`value`) AS `max_temperature`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;

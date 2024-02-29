-- This script lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0

USE HBTN_0C_0;

SELECT SCORE, NAME
FROM SECOND_TABLE
WHERE SCORE >= 10
ORDER BY SCORE DESC;

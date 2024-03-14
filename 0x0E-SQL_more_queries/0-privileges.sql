-- Script that lists all privileges of the MySQL users user_0d_1 and user_0d_2

-- For user_0d_1
SELECT * FROM mysql.user WHERE User='user_0d_1' AND Host='localhost';

-- For user_0d_2
SELECT * FROM mysql.user WHERE User='user_0d_2' AND Host='localhost';

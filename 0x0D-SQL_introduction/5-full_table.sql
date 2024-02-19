-- Script that prints the full description of the first_table from the hbtn_0c_0 
-- database
SELECT 
    COLUMN_NAME, 
    DATA_TYPE, 
    IS_NULLABLE, 
    COLUMN_KEY, 
    COLUMN_DEFAULT, 
    EXTRA 
FROM 
    INFORMATION_SCHEMA.COLUMNS 
WHERE 
    TABLE_SCHEMA = 'hbtn_0c_0' AND 
    TABLE_NAME = 'first_table';

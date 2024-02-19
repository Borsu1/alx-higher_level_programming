#!/bin/bash
# Script to insert a new row in the table first_table from the database hbtn_0c_0

# Database name
DB_NAME="hbtn_0c_0"

# Table name
TABLE_NAME="first_table"

# New row details
ID=89
NAME="Best School"

# MySQL command to insert a new row
mysql -u root -p -e "USE $DB_NAME; INSERT INTO $TABLE_NAME (id, name) VALUES ($ID, '$NAME');"

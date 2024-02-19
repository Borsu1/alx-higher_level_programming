#!/bin/bash
# Script to list all rows of the table first_table from the database hbtn_0c_0

# Database name
DB_NAME="hbtn_0c_0"

# Table name
TABLE_NAME="first_table"

# MySQL command to list all rows
mysql -u root -p -e "USE $DB_NAME; SELECT * FROM $TABLE_NAME;"

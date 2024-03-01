-- Script that list all the tables of a database

CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
USE hbtn_0c_0;

CREATE TABLE IF NOT EXISTS holbteron_0 (
    id INT AUTO_INCREMENT,
    data VARCHAR(255),
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS holbteron_1 (
    id INT AUTO_INCREMENT,
    data VARCHAR(255),
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS holbteron_2 (
    id INT AUTO_INCREMENT,
    data VARCHAR(255),
    PRIMARY KEY(id)
);

SHOW TABLES;

-- Create the database hbtn_0d_usa if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created database
USE hbtn_0d_usa;

-- Ensure the states table exists first (from previous script)
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Create the cities table if it doesn't already exist
-- id is an auto-incrementing unique primary key that can't be null
-- state_id is a foreign key referencing the id in the states table
-- name is a non-nullable VARCHAR column
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

-- Create the table force_name if it doesn't already exist
-- Ensure the table has an id column and a non-null name column
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

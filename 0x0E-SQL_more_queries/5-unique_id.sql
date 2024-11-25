-- Create the table unique_id if it doesn't already exist
-- Ensure the table has an id column with a default value of 1 and is unique
-- and a name column with no constraints
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);

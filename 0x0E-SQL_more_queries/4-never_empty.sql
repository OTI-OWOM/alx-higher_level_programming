-- Create the table id_not_null if it doesn't already exist
-- Ensure the table has an id column with a default value of 1
-- and a name column with no constraints
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
);

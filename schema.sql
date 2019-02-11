-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS corpora;

CREATE TABLE corpora (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  description TEXT ,
  corpora_path TEXT NOT NULL,
  is_valid BIT NOT NULL
);


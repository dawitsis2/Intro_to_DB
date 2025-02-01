-- Use the provided database
USE alx_book_store;

-- Get the full description of the "books" table
SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT, CHARACTER_MAXIMUM_LENGTH
FROM information_schema.columns
WHERE table_name = 'Books' AND table_schema = 'alx_book_store';

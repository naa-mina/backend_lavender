/*
1️⃣ Create a books table with columns (id, title, author, year_published).
 2️⃣ Insert at least 5 books into the table.
 3️⃣ Write queries to:
Select all books
Get books by a specific author
Update the year of a book
Delete a book
 4️⃣ Challenge: Create a borrowers table and connect it to books using a foreign key.

*/
--query to create table
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year_published INT NOT NULL
);


--query to add books to table
INSERT INTO books (title, author, year_published) VALUES
('Lemon Suitcase', 'Peggy Oppong', 2010),
('Chronicles of Nania', 'CS Lewis', 1956),
('Pride and Prejudice', 'Jane Austen', 1813),
('The Lion and the King', 'Ama Asare', 2007),
('Still Walking', 'Bill Moss', 2011);

--query to view info
SELECT * FROM books;

-- query to get books by a specific author
SELECT * FROM books WHERE author = 'Peggy Oppong';

--querry to update the year of a book 
UPDATE books SET year_published = 2011 WHERE author = 'Peggy Oppong';


--query to delete a book
Delete from books where title = 'The Lion and the King'


--challenge
CREATE TABLE borrowers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    book_id INT,
    borrow_date DATE DEFAULT CURRENT_DATE,
    return_date DATE,
    CONSTRAINT fk_book FOREIGN KEY (book_id) REFERENCES books(id)
);

--add borrowers
INSERT INTO borrowers (name, book_id, return_date) VALUES
('Ama Frimpong', 3, '2024-03-20'),
('Kofi Asare', 2, '2024-03-22'),
('Daniel Adjei', 1, '2024-04-01');

select * from borrowers;

--query to view borrowed books
SELECT books.title, books.author, borrowers.name, borrowers.borrow_date, borrowers.return_date
FROM books
LEFT JOIN borrowers ON books.id = borrowers.book_id;

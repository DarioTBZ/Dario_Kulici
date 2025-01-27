CREATE TABLE employees (
id INTEGER AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50),
email VARCHAR(100),
hire_date DATE,
salary DECIMAL(10,2)
);

ALTER TABLE employees ADD department VARCHAR(50);

ALTER TABLE employees MODIFY salary Float(10.2);

ALTER TABLE employees RENAME COLUMN department TO department_id;

ALTER TABLE employees MODIFY department INT;

ALTER TABLE employees DROP COLUMN email;
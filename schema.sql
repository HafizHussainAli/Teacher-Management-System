CREATE TABLE teachers (
    teacher_id INTEGER PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    Email VARCHAR(50) NOT NULL,
    phone VARCHAR (50) NOT NULL,
    subject VARCHAR(100),
    salary NUMERIC(10, 2),
    is_active BOOLEAN DEFAULT TRUE
);

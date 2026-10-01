-- ==========================================================
-- Teacher Management System - Extracted PostgreSQL Queries
-- ==========================================================

-- 1. Add Teacher
INSERT INTO teachers (
    first_name, 
    last_name, 
    email, 
    phone, 
    subject, 
    hire_date, 
    salary, 
    is_active
) VALUES (
    :first_name, 
    :last_name, 
    :email, 
    :phone, 
    :subject, 
    :hire_date, 
    :salary, 
    TRUE
);

-- 2. View All Teachers
SELECT *
FROM teachers
ORDER BY teacher_id;

-- 3. Search Teacher by ID
SELECT *
FROM teachers
WHERE teacher_id = :teacher_id;

-- 4. Search Teacher by Name (Case-Insensitive Substring Match)
SELECT *
FROM teachers
WHERE LOWER(first_name) LIKE LOWER(:pattern)
   OR LOWER(last_name) LIKE LOWER(:pattern);

-- 5. Search Teacher by Subject (Case-Insensitive Exact Match)
SELECT *
FROM teachers
WHERE LOWER(subject) = LOWER(:subject);

-- 6. Update Teacher
-- 6a. Check if teacher exists before update
SELECT *
FROM teachers
WHERE teacher_id = :teacher_id;

-- 6b. Perform update
UPDATE teachers
SET first_name = :first_name,
    last_name  = :last_name,
    email      = :email,
    phone      = :phone,
    subject    = :subject,
    salary     = :salary
WHERE teacher_id = :teacher_id;

-- 7. Delete Teacher
-- 7a. Check if teacher exists before delete
SELECT *
FROM teachers
WHERE teacher_id = :teacher_id;

-- 7b. Perform deletion
DELETE FROM teachers
WHERE teacher_id = :teacher_id;

-- 8. Activate / Deactivate Teacher
-- 8a. Check current active status
SELECT is_active
FROM teachers
WHERE teacher_id = :teacher_id;

-- 8b. Deactivate
UPDATE teachers
SET is_active = FALSE
WHERE teacher_id = :teacher_id;

-- 8c. Activate
UPDATE teachers
SET is_active = TRUE
WHERE teacher_id = :teacher_id;

-- 8d. Alternative: Toggle active status directly in one query
-- UPDATE teachers
-- SET is_active = NOT is_active
-- WHERE teacher_id = :teacher_id;

-- 9. View Active Teachers
SELECT *
FROM teachers
WHERE is_active = TRUE
ORDER BY teacher_id;

-- 10. View Inactive Teachers
SELECT *
FROM teachers
WHERE is_active = FALSE
ORDER BY teacher_id;

-- 11. Show Highest-Paid Teacher
SELECT *
FROM teachers
ORDER BY salary DESC
LIMIT 1;

-- 12. Show Average Salary
SELECT AVG(salary)
FROM teachers;
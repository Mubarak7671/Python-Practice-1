CREATE TABLE Employess( 
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50)
) 
CREATE TABLE EmployeeProfile(
    profile_id INT PRIMARY KEY,
    emp_id INT UNIQUE,
    address VARCHER(100),
    FOREIGN KEY (emp_id) REFERENCES Employess(emp_id)
) ---This one is One to One realtionshiop and unique word must be used in the emp_id column of EmployeeProfile table to ensure that each employee can have only one profile. 

---2.ONE to Many Realationship:-
 CREATE TABLE Customers(
    cust_id INT PRIMARY KEY,
    cust_name VARCHAR(50)
 )

 CREATE TABLE Orders(
    order_id INT PRIMARY KEY,
    cust_id INT,
    order_date DATE,
    FOREIGN KEY (cust_id) REFERENCES Customers(cust_id)
 ) ---This one is One to Many relationship because one customer can have multiple orders but each order is associated with only one customer. Here Unique constraint is not used 

---3.Many to Many Realationship:-
CREATE TABLE Students(
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50)
);

CREATE TABLE Courses(
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50)
); 
---This is Many to Many relationship because one student can enroll in multiple courses and one course can have multiple students. To implement this relationship, we need a junction table that connects the two tables.

CREATE TABLE Studentcourses(
    student_id INT ,
    course_id INT, 
    PRIMARY KEY (student_id,course_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY(course_id) REFERENCES Courses(course_id)
) 

----SET OPERATIONS:- 

--UNION:- 
SELECT city FROM Customers
UNION 
SELECT city FROM Suppliers; 

--UNION ALL:- 
SELECT city FROM Customers 
UNION ALL 
SELECT city FROM Suppliers; 

--INTERSECT:- 
SELECT city FROM Suppliers 
WHERE city IN (SELECT city FROM Customers); 
 
 ---DEFFERENCE:- 
SELECT city FROM Suppliers
WHERE city NOT IN (SELECT city FROM Customers);
---EXAMPLE FOR SET OPERATIONS:- 

CREATE TABLE Customers (
    cust_id INT PRIMARY KEY,
    cust_name VARCHAR(50) NOT NULL,
    city VARCHAR(50)
);

CREATE TABLE Suppliers (
    supplier_id INT PRIMARY KEY,
    supplier_name VARCHAR(50) NOT NULL,
    city VARCHAR(50)
);

INSERT INTO Customers Values 
    (1,'Mubarak' ,'Chennai'),
    (2,'SAjid' ,'Bangalore'),
    (3,'Balaji' ,'Mumbai'),
    (4,'Adharsh' ,'Chennai');  

INSERT INTO Suppliers Values 
    (1,'Nanda' ,'Chennai'),
    (2,'Raja' ,'Kolkata'),
    (3,'Arjun' ,'Mumbai'),
    (4,'Reddy' ,'Chennai'); 

--- Table Relationships:- 
--- One to One Relationship:- 
CREATE TABLE Students(
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50)
);
---Profile table for one person 
CREATE TABLE StudentProfile (
    profile_id INT PRIMARY KEY,
    student_id INT UNIQUE, 
    address VARCHAR(100),
    phone_number VARCHAR(15),
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
)  ;

---One to Many Relationship:-
CREATE TABLE Courses(
    course_id INT PRIMARY KEY,
    course_name VARCHAR(30)
) ;
---Many courses of one student 
CREATE TABLE Enrollments(
    enrollment_id INT PRIMARY KEY, 
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
) ;

---Many to Many Relationship:-
--Junction table for many to many relationship 
CREATE TABLE student_courses(
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
 
-- ============================================
-- ONLINE LEARNING PLATFORM DATABASE PROJECT
-- ============================================

DROP DATABASE IF EXISTS learning_platform;
CREATE DATABASE learning_platform;
USE learning_platform;

-- ============================================
-- PART 1: TABLE CREATION (DDL)
-- ============================================

-- Students Table
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    city VARCHAR(50),
    join_date DATE DEFAULT (CURRENT_DATE)
);

-- Instructors Table
CREATE TABLE instructors (
    instructor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    expertise VARCHAR(100)
);

-- Courses Table
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    price DECIMAL(8,2),
    instructor_id INT,
    FOREIGN KEY (instructor_id)
    REFERENCES instructors(instructor_id)
    ON DELETE SET NULL
);

-- Enrollments Table
CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enroll_date DATE,
    FOREIGN KEY (student_id)
    REFERENCES students(student_id)
    ON DELETE CASCADE,
    FOREIGN KEY (course_id)
    REFERENCES courses(course_id)
    ON DELETE CASCADE
);

-- Lessons Table
CREATE TABLE lessons (
    lesson_id INT AUTO_INCREMENT PRIMARY KEY,
    lesson_name VARCHAR(100),
    course_id INT,
    duration INT,
    FOREIGN KEY (course_id)
    REFERENCES courses(course_id)
    ON DELETE CASCADE
);

-- Lesson Completion Table
CREATE TABLE lesson_completion (
    completion_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    lesson_id INT,
    completion_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id)
);

-- ============================================
-- PART 2: INSERT DATA (DML)
-- ============================================

-- Students (5)
INSERT INTO students (name, email, city, join_date) VALUES
('Mubarak', 'mubarak@gmail.com', 'Bangalore', '2024-01-01'),
('Sajid', 'sajid@gmail.com', 'Chennai', '2024-01-02'),
('Balaji', 'balaji@gmail.com', 'Mumbai', '2024-01-03'),
('Adharsh', 'adharsh@gmail.com', 'Hyderabad', '2024-01-04'),
('Naveen', 'naveen@gmail.com', 'Delhi', '2024-01-05');

-- Instructors (3)
INSERT INTO instructors (name, expertise) VALUES
('Ravi Kumar', 'Python'),
('Anita Sharma', 'Data Science'),
('Karthik Reddy', 'Frontend Development');

-- Courses (4)
INSERT INTO courses (title, price, instructor_id) VALUES
('Python Full Stack', 25000, 1),
('Data Science Mastery', 30000, 2),
('Frontend Development', 20000, 3),
('SQL for Beginners', 15000, 1);

-- Lessons (10)
INSERT INTO lessons (lesson_name, course_id, duration) VALUES
('Python Basics', 1, 2),
('Django Framework', 1, 3),
('REST API', 1, 2),
('ML Introduction', 2, 4),
('Deep Learning', 2, 5),
('HTML Basics', 3, 2),
('CSS Styling', 3, 2),
('JavaScript Basics', 3, 3),
('SQL Introduction', 4, 2),
('Joins and Subqueries', 4, 3);

-- Enrollments (8)
INSERT INTO enrollments (student_id, course_id, enroll_date) VALUES
(1,1,'2024-02-01'),
(1,2,'2024-02-02'),
(2,1,'2024-02-03'),
(3,3,'2024-02-04'),
(4,4,'2024-02-05'),
(5,2,'2024-02-06'),
(2,3,'2024-02-07'),
(3,4,'2024-02-08');

-- Lesson Completion
INSERT INTO lesson_completion (student_id, lesson_id, completion_date) VALUES
(1,1,'2024-02-10'),
(1,2,'2024-02-12'),
(2,1,'2024-02-15'),
(3,6,'2024-02-18'),
(3,7,'2024-02-20'),
(4,9,'2024-02-21');

-- ============================================
-- PART 3: QUERY TASKS (DQL)
-- ============================================

-- 1. Show all students
SELECT * FROM students;

-- 2. List all courses with instructor names
SELECT c.title, i.name AS instructor
FROM courses c
JOIN instructors i ON c.instructor_id = i.instructor_id;

-- 3. Show lessons of Course ID 1 
SELECT lesson_name FROM lessons WHERE course_id = 1;

-- 4. Students from Bangalore
SELECT * FROM students WHERE city = 'Bangalore';

-- 5. Student names with enrolled course titles
SELECT s.name, c.title
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id;

-- 6. Count students per course
SELECT c.title, COUNT(e.student_id) AS total_students
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.title;

-- 7. Courses taught by each instructor
SELECT i.name, c.title
FROM instructors i
LEFT JOIN courses c ON i.instructor_id = c.instructor_id;

-- 8. Lessons completed by each student
SELECT s.name, l.lesson_name
FROM lesson_completion lc
JOIN students s ON lc.student_id = s.student_id
JOIN lessons l ON lc.lesson_id = l.lesson_id;

-- 9. Students enrolled in more than one course
SELECT s.name, COUNT(e.course_id) AS total_courses
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id
HAVING COUNT(e.course_id) > 1;

-- 10. Course with highest enrollments
SELECT c.title, COUNT(e.student_id) AS total
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id
ORDER BY total DESC
LIMIT 1;

-- 11. Instructors whose courses have no enrollments
SELECT i.name
FROM instructors i
LEFT JOIN courses c ON i.instructor_id = c.instructor_id
LEFT JOIN enrollments e ON c.course_id = e.course_id
WHERE e.enrollment_id IS NULL;

-- 12. Rank courses by popularity
SELECT c.title,
COUNT(e.student_id) AS total_enrollments,
RANK() OVER (ORDER BY COUNT(e.student_id) DESC) AS ranking
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id;

-- ============================================
-- END OF PROJECT
-- ============================================
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Create Student Table
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Student (
        Sid INTEGER PRIMARY KEY,
        Name TEXT,
        Age INTEGER,
        Major TEXT
    )''')

# Create Enroll Table
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Enroll (
        Sid INTEGER,
        CourseId TEXT,
        FOREIGN KEY (Sid) REFERENCES Student(Sid)
    )''')

# Create Course Table
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Course (
        CourseId TEXT PRIMARY KEY,
        CourseName TEXT
    )''')

# Insert data into Student Table
students_data = [
    (10111, 'Lin', 21, 'CS'),
    (10122, 'Guldu', 23, 'IT'),
    (10133, 'Lin', 18, 'CS')
]
cursor.executemany('''INSERT INTO Student (Sid, Name, Age, Major) VALUES (?, ?, ?, ?)''', students_data)

# Insert data into Enroll Table
enroll_data = [
    (10111, 'CSCI4333'),
    (10122, 'CSCI1320'),
    (10111, 'CSCI1320')
]
cursor.executemany('''INSERT INTO Enroll (Sid, CourseId) VALUES (?, ?)''', enroll_data)

# Insert data into Course Table
courses_data = [
    ('CSCI4333', 'Database Design'),
    ('CSCI1320', 'C++ Programming'),
    ('ITEC3335', 'Web Design'),
    ('CSCI3323', 'HCI Interface')
]
cursor.executemany('''INSERT INTO Course (CourseId, CourseName) VALUES (?, ?)''', courses_data)

print("Tables created successfully and data inserted!")

# Execute the SQL query
cursor.execute('''
    SELECT Student.Sid, Student.Name
    FROM Student
    JOIN Enroll ON Student.Sid = Enroll.Sid
    JOIN Course ON Enroll.CourseId = Course.CourseId
    WHERE Student.Major = 'CS' AND Course.CourseName = 'Database Design'
''')

# Fetch all the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Execute the SQL query
cursor.execute('''
    SELECT DISTINCT e1.Sid, e2.Sid AS Sid2
    FROM Enroll e1
    JOIN Enroll e2 ON e1.CourseId = e2.CourseId AND e1.Sid < e2.Sid
''')

# Fetch all the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Commit changes and close connection
conn.commit()
conn.close()

# Diagram Review

### 1. Basic Units
Entity Set: <div style="margin-left: auto; margin-right: auto; width: 30%"> ![Entity Graph](Images\DR1_1.png) </div>

Relationship Set:<div style="margin-left: auto; margin-right: auto; width: 30%"> ![Relationship Graph](Images\RP_2.png) </div>

### 2. Constraints (Key) -> at most one -> <= 1
one-to-one<div style="margin-left: auto; margin-right: auto; width: 30%"> ![one-to-one graph](Images\DR1_3.png) </div>
one-to-many<div style="margin-left: auto; margin-right: auto; width: 30%"> ![one-to-many graph](Images\DR1_4.png) </div>
many-to-one<div style="margin-left: auto; margin-right: auto; width: 30%"> ![many-to-one graph](Images\DR1_5.png) </div>
many-to-many<div style="margin-left: auto; margin-right: auto; width: 30%"> ![many-to-many graph](Images\DR1_6.png) </div>

### 3. Constraint (Participation)
-> at least one -> >= 1<div style="margin-left: auto; margin-right: auto; width: 30%"> ![constraint participation graphs](Images\DR1_7.png) </div>

### 4. Advanced E-R Diagram
Weak Entity<div style="margin-left: auto; margin-right: auto; width: 50%"> ![Weak Entity graph](Images\DR1_8.png) </div>
 Recursive Relationship<div style="margin-left: auto; margin-right: auto; width: 30%"> ![Recursive Relationship graph ](Images\DR1_9.png) </div>
Ternary Relationship (not going to be in exam)<div style="margin-left: auto; margin-right: auto; width: 30%"> ![Ternary Relationship graph](Images\DR1_10.png) </div>
Is A Relationship<div style="margin-left: auto; margin-right: auto; width: 30%"> ![Is A Relationship](Images\DR1_11.png) </div>

---
##Q1:
Please complete the E-R Diagram for this University Database. Your E-R Diagram should describe all conditions below. **If you find some conditinons cannot be enforced in E-R Diagram, clearly state them and explain the reason.**
1. For each professor, the database stores Name, employee ID, salery, and Date of Birth.
2. Each student record contains a student ID, a name, and the average GPA.
3. Each Course record contains a course ID, course name.
4. An empplayee ID can be uniquely identify a professor.
5. A Student ID can be uniquely identify a student.
6. A student can become a GTA for a course
7. A GTA record additional stores the salery information for the student.
8. Each course can have any number of prerequisite courses.
9. A GTA needs to teach at least one course, and a course can have any number of GTAs.
10. Professor can teach any number of courses, but a course should be taught by at least one
11. Students should enroll in at least one course and each course should be enrolled by at least one student.

<div style="margin-left: auto; margin-right: auto; width: 85%"> 

![E-R Diagram for University Database](Images\DR1_12.png) </div><br>

---
<br>
<div style="display:relative; text-align: center;">end of document</div>
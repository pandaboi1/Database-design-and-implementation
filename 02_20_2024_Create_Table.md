# Create table
..how do we create an actual database on our computers?
We use SQL, a language that allows us to build, modify and query databases.

##### professor(<u>PID</u>:string, name:string)<div style="margin-left: auto; margin-right: auto; width: 60%"> ![SQL Table 1](Images\CT\CT_1.png) </div>

---
### SQL (Stuctured Query Language)
- SQL is a language that allows us to build, modify and query databases.
- SQL is an ANSI standard language.(American National Standards Institute)
- SQL is the "engine" behind Oracle, Microsoft SQL Server, etc..
- Most of these systems have built GUIs on top of the command line interface, so you don't normally write statments dirctly in SQL (although you can).
---
### Create Table Statment
Create Table Statment consists:
- Table Name
- Attributes
- Primary Key
- Foreign Key
---
#### Constraints
**Primary Key**: The (combination of) attributes that can uniquely define each record in a table.
**Foreign Key**: 
- The (combination of) attributes that are "borrow" form another table.All the values in these attribute(s) should be existed in another table.
- Set of feilds in one relation that is used to 'refer' to a tuple in another relation. (Most correspond to <span style="color:red">primary key</span> of the second relation.) Like a `logical pointer’.

- Only students listed in the Students relation should be allowed to enroll for courses.

<div style="margin-left: auto; margin-right: auto; width: 260px">
<span style="color:red">Enrolled</span>

|sid|cid|grade|
|:---:|:---|:---:|
|53666|Carnatic101|C|
|53666|Reggae|B|
|53650|Topology112|A|
|53666|History|B|
</div>
<div style="margin-left: auto; margin-right: auto; width: 370px">
<p style="text-align:center">|<br>v</p>
<span style="color:red">Students</span>

|sid|name|login|age|gpa|
|:--:|:---|:---:|:--:|:--:|
|53666|Jones|jones@cs|18|3.4|
|53666|Smith|smith@eecs|18|3.2|
|53650|Smith|smith@math|19|3.8|
</div>


---
### To SQL Statment
***Strategy***:
- Translate everything into relational schema
- Then translate it into SQL Statment by:
    - Work on [Table Name], [Attributes], [Type of Attributes], [Primary Key].
    - For some tables (relationship), we need to enforce foreign key constraint.
----
### Create Table
<div style="margin-left: auto; margin-right: auto; width: 70%"> 

![SQL Table 1](Images\CT\CT_2.png) </div>
##### Professor(name : string, <u>SSN</u> : string, DoB : date)
***SQL***
```SQL
CREATE TABLE Table_Name
    (attr1 type1, 
    attr2 type2,
    ...
    attr_n type_n,

    PRIMARY KEY (Key)
);
```
---
### Relationship: Translate to
<div style="margin-left: auto; margin-right: auto; width: 70%"> 

![Entity Set 1](Images\CT\CT_3.png) </div>
#### Work(<u>SSN</u> : string, <u>did</u> : string)
```SQL
CREATE TABLE Work(
    ssn CHAR(11),
    did INTEGER,
    PRIMARY KEY (ssn, did),
    FOREIGN KEY (ssn) REFERENCES Professor,
    FOREIGN KEY (did) REFERENCES Department
)
```
- In translating a relationship set to a relation, attributes of the relation must include:
    - Keys for the participating entity set(s) as foreign keys
        - This set of attributes forms a <b>superkey</b> for the relation.
    - All descriptive attributes.
---
### Key Constraints
Each dept has at most one manager, according to the <u style="color:blue"><i>key constraint</i></u> on Manages.
<div style="margin-left: auto; margin-right: auto; width: 70%"> 

![Entity Set 2](Images\CT\CT_4.png) </div>
#### Manages(ssn: string, <u>did</u>: string, since: date)
Map relationship to a table:
- Note that did is the key now!
```SQL
    CREATE TABLE Manages(
    ssn CHAR(11),
    did INTEGER,
    since DATE,
    PRIMARY KEY (did),
    FOREIGN KEY (ssn) REFERENCES Manager,
    FOREIGN KEY (did) REFERENCES Departments);
```
---
### Primary Constraint
Does every department have a manager?
- If so, this is a <u style="color:blue"><i>participation constaint:</i></u> the participation of Depatments in Manages is said to be <span style="color:blue">total (vs. partial)</span>.
    - Every <i>did</i> value in Departments table must appear in a row of the Manages table (with a non-null ssn value!).
<div style="margin-left: auto; margin-right: auto; width: 70%"> 

![Entity Set 3](Images\CT\CT_4.png) </div>
##### Relational Schema:
##### Manager(<u>ssn</u>: string, name: string, lot:number)
##### <span style="color:red">Dept_Mgr(<u>did</u> : string, dname : string, budget : number, since: date, ssn : string)</span>

- We can capture participation constraints involving one entity set in binary relationship.
<span style="color:red">Dept_Mgr(<u>did</u> : string, dname : string, budget : number, since: date, ssn : string)</span>

```SQL
    CREATE TABLE Dept_Mgr(
    did INTEGER,
    dname CHAR(20),
    budget REAL,
    ssn CHAR(11) NOT NULL,
    since DATE,
    PRIMARY KEY (did),
    FOREIGN KEY (ssn) REFERENCES Manager);
```
<span style="color:red;">ssn should come from Manager table!</span>

---
### Recursive Relationship with Roles
<div style="margin-left: auto; margin-right: auto; width: 30%"> 

![Entity Set 4](Images\CT\CT_5.png) </div>

<span style="color:red">Rename attribute by adding role</span>
```SQL
    CREATE TABLE Reports_To(
    supervisor_ssn CHAR(11),
    subordinate_ssn CHAR(11),
    PRIMARY KEY (supervisor_ssn, subordinate_ssn),
    FOREIGN KEY (supervisor_ssn) REFERENCES Employees(ssn),
    FOREIGN KEY (subordinate_ssn) REFERENCES Employees(ssn));
```
---
### Weak Entities
- A <span style="color:blue">weak entity</span> can be identified uniquely only by considering the primary key of another (owner) entity.
    - Owner entity set and weak entity set must participate in a one-to-many relationship set (1 owner, many weak entities).
    -  Weak entity set must have total participation in this <span style="color:blue">identifying</span> relationship set.
    <div style="margin-left: auto; margin-right: auto; width: 60%"> 
    
    ![SQL Table 2](Images\CT\CT_6.png) </div>
---
### Translating Weak Entity Sets
- Weeak entity set and identifying relationship set are translated into a single table.
    - <span style="color:blue">When the owner entity is deleted, all owned weak entities must also be deleted.</span>
```SQL
CREATE TABLE Dep_Policy (
    pname CHAR(20),
    age INTEGER,
    cost REAL,
    ssn CHAR(11),
    PRIMARY KEY (pname, ssn),
    FOREIGN KEY (ssn) REFERENCES Employees);
```
----
### ISA ('is a') Hierarchies
<div style="margin-left: auto; margin-right: auto; width: 60%"> 

![ISA Entity Set](Images\CT\CT_7.png) </div>
Write down relational schema

##### Employee(<u>ssn</u>:string, name:string, lot:number)
```SQL
CREATE TABLE Employees (
    ssn CHAR(20),
    name CHAR(50),
    lot INTEGER,
    PRIMARY KEY (ssn));
```
##### Hourly_Emps(<u>ssn</u>:string, hourly_wage:number, hourly_worked:number)
```SQL
CREATE TABLE Hourly_Emps (
    ssn CHAR(20),
    hourly_wages REAL,
    hours_worked INTEGER,
    PRIMARY KEY (ssn),
    FOREIGN KEY (ssn) REFERENCES Employees);
```
##### Contract_Emps(<u>ssn</u>:string, contractid:string)
```SQL
CREATE TABLE Contract_Emps (
    ssn CHAR(20),
    contractid INTEGER,
    PRIMARY KEY (ssn),
    FOREIGN KEY (ssn) REFERENCES Employees);
```
---
### Practice
<div style="margin-left: auto; margin-right: auto; width: 80%"> 

![SQL Table 3](Images\CT\CT_8.png) </div>
Trail(<u>sid</u>:string, name:string, distance:number, rating:number)
Tail_Belong(<u>sid</u>:string, <u>pname</u>:string, name:string, distance:number, rating:number)
Park(<u>pname</u>:string)
Locate(<u>Name</u>:string, <u>city_name</u>:string)
City(<u>city_name</u>:string, state:string)

```SQL
CREATE TABLE Park(
    Name CHAR(20),
    PRIMARY KEY(Name));

CREATE TABLE City(
    city_name CHAR(20),
    State CHAR(2),
    PRIMARY KEY(city_name));
CREATE TABLE locate(
    Name CHAR(20),
    city_name CHAR (20),
    PRIMARY KEY(Name),
    FOREIGN KEY Name REFERENCES Park,
    FOREIGN KEY city_name REFERENCES City);
CREATE TABLE Trail_Belong(
    distance REAL,
    rating REAL,
    name CHAR(20),
    sid CHAR(20),
    pname CHAR(20)NOT NULL,
    PRIMARY KEY(sid),
    FOREIGN KEY pname REFERENCES Park);
```
<br>

---
<br>
<div style="display:relative; text-align: center;">end of document</div>
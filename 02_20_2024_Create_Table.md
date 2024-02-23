## Create table
..how do we create an actual database on our computers?
We use SQL, a language that allows us to build, modify and query databases.

*professor(<u>PID</u>:string, name:string)*

---
### SQL (Stuctured Query Language)
- SQL is a language that allows us to build, modify and query databases.
- SQL is an ANSI standard language.
- SQL is the "engine" behind Oracle, Microsoft SQL Server, st.
- Most of these systems have built GUIs on top of the command line interface, so you don't normally write statments dirctly in SQL (although you can)
---
### Create Table Statment
Create Table Statment consists:
- Table Name
- Attributes
- Primary Key
- Foreign Key

#### Constraints
**Primary Key**: The (combination of) attributes that can uniquely define each record in a table.
**Foreign Key**: 
- The (combination of) attributes that are "borrow" form another table.
- Set of feilds in one relation that is used to 'refer' to a tuple in another relation. (Most correspond to .....)

- Only students listed in the Students relation should be allowed to enroll for courses.

<div style="margin-left: auto; margin-right: auto; width: 373px">

|sid|cid|grade|
|:---:|:---|:---:|
| | | |
| | | |
| | | |
| | | |
</div>

---
### To SQL Statment
***Strategy***:
- Translate everything into relational schema
- Then translate it into SQL Statment by:
    - Work on [Table Name], [Attributes], [Type of Attributes], [Primary Key]
    - For some tables (relationship), we need to enforce foreign key constraint
----
#### Create Table
<div style="margin-left: auto; margin-right: auto; width: 60%"> 

![SQL Table 1](Images\CT\CT_1.png) </div>
*Professor(name:string, <u>SSN</u>:string, DoB:date)*

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
<div style="margin-left: auto; margin-right: auto; width:275px">
.....<b>Check Slides for missing data</b>.....
</div>

---
### Primary Constraint
Does every department have a manager?
- If so, this is a <u style="color:blue">participation constaint:</u> the participation of Depatments in Manages is said to be <u style="color:blue"></u>.....

- We can capture participation constraints involving one entity set in binary relationship.
<span style="color:red">More data missing.......</span>

---
### Transplating Weak Entity Sets
- We ......
----
#### ISA ('is a') Hierarchies
<div style="margin-left: auto; margin-right: auto; width: 60%"> 

![SQL Table ](Images\CT\CT_.png) </div>
Write down relational schema

Employee(<u>ssn</u>:string, name:string, lot:number)
Hourly_Emps(<u>ssn</u>:string, hourly_wage:number, hourly_worked:number)
Contract_Emps(<u>ssn</u>:string, contractid:string)
```SQL
CREATE TABLE 
```
---
### Practice
<div style="margin-left: auto; margin-right: auto; width: 80%"> 

![SQL Table 1](Images\CT\CT_3.png) </div>
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

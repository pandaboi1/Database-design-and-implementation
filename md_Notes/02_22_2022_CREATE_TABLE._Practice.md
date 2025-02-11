# CREATE TABLE (SQL)
# Table of Contents
- [Table A](#tableaattr1--str-attr-str)
- [Creating Tables Practice](#creating-tables-practice)
    - [Account](#accountid--str-name-str)
    - [FacultyAcc](#facultyaccsalary--num-id--str)
    - [StudentAcc](#studentaccid)
    - [Manager_Man](#manager_manname--str-mid--str-days--num-id--str)
    - [Belong](#belongid--str-did--str)
    - [Department](#departmentname--str-did--str)
    - [OfficeOwn](#officeownname--str-lot--num-did--str)
---
### TableA(<u>attr1</u> : str, attr :str)
```SQL
CREATE TABLE TableA(
    attr1 CHAR(10),
    attr2 CHAR(10), 
    PRIMARY KEY (attr1)
    [FOREIGN KEYs]
    Relationship -> key constraint / participation..
    Weak Entity

    ISA
    FOREIGN KEY (attr1 REFERENCES TableB)
);
```

---
## Creating Tables Practice
<div style="margin-left: auto; margin-right: auto; width: 90%"> 

![PC1](./Images/CTP1/CT1.png) </div>

#### Account(<u>id</u> : str, name :str)
```SQL
CREATE TABLE Account(
    id CHAR (10),
    name CHAR (10),
    PRIMARY KEY (id)
);
```
#### FacultyAcc(salary : num, <u>id</u> : str)
```SQL
CREATE TABLE FacultyAcc(
    salary CHAR (20),
    id CHAR (10),
    PRIMARY KEY (id)
    FOREIGN KEY (id) REFERENCES Account
);
```
##### StudentAcc(<u>id</u>) [<i>Click Here For Table</i>](#creating-tables-practice)
```SQL
CREATE TABLE StudentAcc(
    id CHAR (10),
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES Account
);
```
##### Manager_Man(Name : str, <u>MID</u> : str, days : num, id : str) [<i>Click Here For Table</i>](#creating-tables-practice)
```SQL
CREATE TABLE (
    Name CHAR (20),
    MID CHAR (20)
    days INT,
    id CHAR (10) NOT NULL
    PRIMARY KEY (MID)
    FOREIGN KEY (id) REFERENCES FacultyAcc
);
```
##### Belong(<u>id</u> : str, DID : str) [<i>Click Here For Table</i>](#creating-tables-practice)
```SQL
CREATE TABLE Belong(
    id CHAR (10),
    DID CHAR (10),
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES Account,
    FOREIGN KEY (DID) REFERENCES Department
);
```
##### Department(Name : str, <u>DID</u> : str) [<i>Click Here For Table</i>](#creating-tables-practice)
```SQL
CREATE TABLE Department(
    Name CHAR (20),
    DID CHAR (20),
    PRIMARY KEY (DID)
);
```
##### OfficeOwn(Name : str, <u>Lot</u> : num, <u>DID</u> : str) [<i>Click Here For Table</i>](#creating-tables-practice)
```SQL
CREATE TABLE OfficeOwn(
    Name CHAR (10),
    Lot INT,
    DID CHAR (10),
    PRIMARY KEY (Lot, DID),
    FOREIGN KEY (DID) REFERENCES Department
);

```
<br>

---
<br>
<div style="display:relative; text-align: center;">end of document</div>
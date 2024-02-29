# Relational Model 1

<div style="margin-left: auto; margin-right: auto; width: 40%"> 

![ERD](Images\RM1_1.png) </div>

---
#### Relations
A **relation** is a more concrete construction, of something we have seen
before, the ER diagram.

A **relation** consists of a ==**relational schema**== and a ==**relational instance**==.

<span style="color:red">A relation is (just!) a table!</span>

A **relation schema** is essentially a list of column names with their
data types. In this case…
students(name : string, S.S.N, Street, city)

A schema also specifies the name of each **field**, and its domain. **Fields** are often refered to as columns, attributes, dimensinos

**Primary key**: just like ER diagram. Remember that the primary key may be combinationof two or more fields

A **relation instance** is made up of zero or more **tuples** (rows, records)

The number of tuples = **cardinality** of the relation
Of course, we don’t count the row of <span style="color:red">the attribute name</span>!

<div style="margin-left: auto; margin-right: auto; width: 324px">

|Name|<u>S.S.N.</u>|Street|City|
|--|:-:|:-|--|
|Lisa|1272|10th|Mcallen|
|Bart|5592|Sugar|Edingburg|
|Lisa|7552|9th|Mission|
|Sue|5555|Coria|Brownsbille|
</div>

- In this table, **cardinality** is 4
- The number of fields is called the **degree** (or **arity**, or dimensionality of the relation).
- Above we have a table of degree 4.
- The size of this table is 16

---
## E-R Diagram Translation 
###TableName(Attrl : domain, Attr2 : domain, ... )
<div style="margin-left: auto; margin-right: auto; width: 70%"> 

![ERD](Images\RM1_2.png) </div>

#### 1. Customer(name : string, <u>SSN</u> : string, DoB : date)
<div style="margin-left: auto; margin-right: auto; width: 265px">

|Name|<u>S.S.N.</u>|DoB|
|--|:-:|:-|
|Jessica|1111|2002/01/01|
|Tom|2222|1990/01/01|
</div>

#### 2. Order(<u>Ord. #</u> : int, Price : number)
<div style="margin-left: auto; margin-right: auto; width: 150px">

|<u>Ord #</u>|Price|
|--|:-:|
|001|$10.99|
|002|$2.99|
|003|$4.99|
</div>

#### 3. Purchase(<u>SSN</u> : string, <u>Ord. #</u> : int)
    Data type needs to match the previous data types of the previous enities. If day was added to the relational attribute, then it will be:
    <br><div style="text-align: center">***Purchase(<u>SSN</u> : string, <u>Ord. #</u> : int, day : date)***</div><br>
    <div style="margin-left: auto; margin-right: auto; width: 160px">
    
    |<u>SSN</u>|<u>Ord. #</u>|
    |:-:|:-:|
    |1111|001|
    |2222|002|
    |1111|003|
    </div> 
    There won't be any redundent name storing if done this way.
--- 

#### <br><span style="Background-color: black;; color: white; padding: 10px; border-radius: 12px; margin: px"> Practice </span>
<div style="margin-left: auto; margin-right: auto; width: 90%"> 

![ERD](Images\RM1_3.png) </div>

1. **NationalPark(<u>Name</u>:string,State:string, est.:date)**
2. **Trail(Name : string, <u>id</u> : number, Length : number)**
3. **Belong(<u>name</u> : string, <u>id</u> : number)**

<br>

---
<br>
<div style="display:relative; text-align: center;">end of document</div>
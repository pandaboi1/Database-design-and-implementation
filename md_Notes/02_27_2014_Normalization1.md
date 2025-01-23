# Normalization 1
# Table of Contents
- [Question](#question)
- [What is Degree, Cardinality, and Size of Table](#what-is-the-degree-cardinality-and-size-of-alltrail-table)
- [Another D/C/S of Table](#what-about-this)
- [Redundancy is the Enemy](#redundancy-is-the-enemy)
- [Normalization](#normaliztion)
- [Decomposition](#what-do-we-do-decomposition)
- [Redundancy](#redundancy)
- [Another issue](#whats-the-problem-again)
- [If Redundancy](#what-to-do-if-you-see-redundancy)
---
### Think about our previous examples
<div style="margin-left: auto; margin-right: auto; width: 380px">

|<u>Name</u>|State|Established|
|:---:|:---|:---|
|Yellow Stone|WY|1872|
|Great Smoky Mountain|TN|1934|
|Acadia|ME|1916|
</div>
<div style="margin-left: auto; margin-right: auto; width: 80%"><br><img alt="Maps" src="./Images/N1\N1_1.png"></img><br></div>

##### Degree: 3, # of columns
##### Cardinality: 3, # of rows (NOT including Title Names)
##### Size: 3 * 3 = 9, (# of cols) * (# of rows)
---
### Question 
- How do you feel about this database design?
<div style="margin-left: auto; margin-right: auto; width: 80%"><br><img alt="Entity Set 1" src="./Images/N1\N1_2.png"></img><br><br></div>

<span style="color:red">AllTrail(<u>Pname</u>:str, State:str, Est:date, <u>tid</u>:str, length:num, rating:num, difficulty:str)</span>

### What is the ***degree***, ***cardinality***, and ***size*** of AllTrail Table?
Degree = 7 <br>Cardinality = 264+373+224 = 861 <br>Size = 6027

---
### What about this?
<div style="margin-left: auto; margin-right: auto; width: 80%"> <img alt="Entity Set 2" src="./Images/N1\N1_3.png"></img></div>
<div style="margin-left: auto; margin-right: auto; width: 80%"><br><img alt="Maps" src="./Images/N1\N1_1.png"></img><br></div>

### What is the ***degree***, ***cardinality***, and ***size***?

#### Trail(Pname:str, <u>tid</u>:str, length:num, rating:num, difficulty:str)
5 (parameters in Trail)  * 681 (number of trails (264 + 373 + 224)) = **3405 Degree**
#### AllTrail(<u>Pname</u>: str, State: str, Est : date)
3 (rows, each storing a park name) * 3 (cols, name/state/Established) = **9 Cardinality**
#### 3405 (Trail) + 9 (AllTrail) = **3405 Total Size**
---
### Redundancy is the Enemy
<div style="margin-left: auto; margin-right: auto; width: 90%"> <img alt="Too long of Entity Set" src="./Images/N1\N1_4.png"></img></div>Normalization
- Consider relation obtained
    - Hourly_Emps(ssn, name, lot, rating, hrly_wage, hrs_worked)
    - Call it **SNLRHW**
- What if we **know** rating (**R**) determines hrly_wage (**W**)?
<div style="margin-left: auto; margin-right: auto; width: 380px">

|S|N|L|R|W|H|
|:--|:--|:--:|:--:|:--:|:--:|
|122-22-3666|Attishoo|48|8|10|40|
|231-31-5368|Smiley|22|8|10|30|
|131-24-3650|Smethrust|35|5|7|30|
|434-26-3751|Guldu|35|5|7|32|
|612-67-4134|Madayan|35|8|10|40|
</div>

- The existence of integrity constraints **(e.g., R → W)**.
<div style="text-align: center;"><span style="color:blue;">functional dependencies</span></div>

---
### What do we do? Decomposition
<div style="display:relative; align:center">
<div style="margin-left: auto; margin-right: auto; width: 320px">

|S|N|L|R|W|H|
|:--|:--|:--:|:--:|:--:|:--:|
|122-22-3666|Attishoo|48|8|10|40|
|231-31-5368|Smiley|22|8|10|30|
|131-24-3650|Smethrust|35|5|7|30|
|434-26-3751|Guldu|35|5|7|32|
|612-67-4134|Madayan|35|8|10|40|
</div>
<div style="text-align: center;">↓</div>
<div style="margin-left: auto; margin-right: auto; width: 285px">

|S|N|L|R|H|
|:--|:--|:--:|:--:|:--:|
|122-22-3666|Attishoo|48|8|40|
|231-31-5368|Smiley|22|8|30|
|131-24-3650|Smethrust|35|5|30|
|434-26-3751|Guldu|35|5|32|
|612-67-4134|Madayan|35|8|40|
</div>
<div style="text-align: center;">▷◁</div>
<div style="margin-left: auto; margin-right: auto; width: 60px">

|R|W|
|:-:|:-:|
|8|10|
|5|7|
</div>
</div>

---
### Redundancy
- When part of data can be **derived** from other parts, we say redundancy exists.
- Can you guess the value "?"
<div style="margin-left: auto; margin-right: auto; width: 380px">

|S|N|L|R|W|H|
|:--|:--|:--:|:--:|:--:|:--:|
|122-22-3666|Attishoo|48|8|10|40|
|231-31-5368|Smiley|22|8|**?**|30|
|131-24-3650|Smethrust|35|5|7|30|
|434-26-3751|Guldu|35|5|7|32|
|612-67-4134|Madayan|35|8|10|40|
</div>

---
### What’s the problem, again
- <span style="color:blue">Update anomaly</span>: Can we change W in just the 1st tuple of SNLRWH?
- <span style="color:blue">Insertion anomaly</span>: What if we want to insert an employee and don’t know the hourly wage for his rating?
- <span style="color:blue">Deletion anomaly</span>: If we delete all employees with rating 5, we lose the information about the wage for rating 5! 
---
### What to do if you see redundancy?
<div style="display:relative; text-align: center;">
<div style="color:#AA0000">AllTrail(<u>Pname</u>:str, State:str, Est:date, <u>tid</u>: str, length:num, rating:num, difficulty:str)</div>
<div style="text-align: center;">↓ Decomposition</div>
<div style="color:red">Trail(Pname:str, <u>tid</u>:str, length:num, rating:num, difficulty:str)<br>
AllTrail(<u>Pname</u>:str, State:str, Est:date)</div>
</div><br>

---
<br>
<div style="display:relative; text-align: center;">end of document</div>
# SQL Theory Assignment
## Understanding Relational Databases in AI Systems

---

## 1. Importance of Databases in Real-World AI Systems

Databases are essential in real-world AI systems because AI models require large amounts of organized data to learn patterns and make predictions.

Databases store and manage this data efficiently so that it can be accessed, updated, and analyzed easily.

### Examples of Data Stored in Databases
- User information (name, email, age)
- Transaction records (purchases, payments)
- Sensor data (IoT devices)
- Images and metadata
- Logs and behavioral data

### Why Structured Storage is Necessary
Structured storage allows data to be organized in a consistent format. This helps in:
- Faster data retrieval
- Accurate data analysis
- Avoiding duplicate or inconsistent data
- Efficient training of AI models

For example, a recommendation system like Netflix or Amazon stores user viewing or purchasing history in structured databases to recommend new content or products.

---

## 2. Relational Database Mental Model

A relational database organizes data in the form of tables.

### Tables
A table represents a collection of related data about a specific entity.

Example: A **Students** table storing student details.

### Rows
Rows represent individual records in the table.

Example:

| StudentID | Name | Age |
|-----------|------|-----|
| 101 | Rahul | 20 |
| 102 | Anjali | 19 |

Each row represents one student.

### Columns
Columns represent attributes or properties of the entity.

Example columns:
- StudentID
- Name
- Age

Each table should represent **only one entity** to keep the database organized and reduce redundancy.

---

## 3. Primary Key

A **Primary Key** is a column (or combination of columns) that uniquely identifies each record in a table.

### Properties of a Primary Key
- Must be **unique**
- Cannot contain **NULL values**
- Each row must have a different primary key value

Example:

| StudentID (Primary Key) | Name | Age |
|-------------------------|------|-----|
| 101 | Rahul | 20 |
| 102 | Anjali | 19 |

Here, **StudentID** uniquely identifies each student.

Primary keys help databases quickly locate and manage records.

---

## 4. Database Schema

A **Database Schema** defines the structure of the database.

It specifies:
- Tables
- Columns
- Data types
- Relationships
- Constraints (Primary Key, Foreign Key)

Example Schema for Students Table:

Students Table
- StudentID (INT, Primary Key)
- Name (VARCHAR)
- Age (INT)

### Importance of Schema
Schemas ensure that data is stored in a consistent and organized format.  
They help maintain data integrity and prevent incorrect or inconsistent data entries.

---

## 5. Relationships Between Tables

In relational databases, tables are connected through relationships.

These relationships allow data to be linked across multiple tables.

### Foreign Key
A **Foreign Key** is a column in one table that refers to the **Primary Key** in another table.

Example:

Students Table

| StudentID | Name |
|----------|------|
| 101 | Rahul |
| 102 | Anjali |

Courses Table

| CourseID | StudentID | CourseName |
|----------|-----------|------------|
| 1 | 101 | Machine Learning |
| 2 | 102 | Data Science |

Here:
- **StudentID in Courses table is a Foreign Key**
- It references **StudentID in Students table**

This creates a relationship between students and their courses.

### Why Relationships Are Important
- Avoid data duplication
- Maintain data consistency
- Allow complex queries across tables
# -*- coding: utf-8 -*-

import sqlite3
from employee import Employee

## Connection Object

conn = sqlite3.connect('employee.db')

## For memory quick test runs
conn = sqlite3.connect(':memory:')

## Create cursor
c = conn.cursor()

######################################## CREATE TABLE ##########################

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")

## Commit current transaction
conn.commit()

conn.close()


##################################### INSERT DATA ##############################

c.execute("INSERT INTO employees VALUES ('John', 'Dudley', 50000)")

conn.commit()

conn.close()


################################### INSERT DATA 2 ##############################

emp_1 = Employee('John', 'Dean', 9000)
emp_2 = Employee('Jane', 'Dean', 12000)

## First way
c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))

## Second way
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay':emp_2.pay})

conn.commit()

conn.close()

################################## SELECT STATEMENT ############################

c.execute("SELECT * FROM employees WHERE last=:last", {'last':'Dean'})

# Deifferent fetches
print(c.fetchone())
c.fetchmany(5)
c.fetchall()










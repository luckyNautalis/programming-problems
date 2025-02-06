"""176. Second Highest Salary
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

The result format is in the following example.
"""

import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries = employee["salary"].drop_duplicates()
    salaries.dropna(inplace=True)
    salaries.sort_values(ascending=False, inplace=True)
    second_highest = None if salaries.size < 2 else salaries.iloc[1]
    return pd.DataFrame({f"SecondHighestSalary": [second_highest]})

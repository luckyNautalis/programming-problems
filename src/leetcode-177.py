"""177. Nth Highest Salary
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

The result format is in the following example.

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
"""

import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N < 1 or employee["salary"].nunique() < N:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
    salaries = employee["salary"].sort_values()
    salaries.drop_duplicates(inplace=True)
    salaries.dropna(inplace=True)
    nth_highest = salaries[salaries.size - (N - 1)]
    return pd.DataFrame({f"getNthHighestSalary({N})": [nth_highest]})

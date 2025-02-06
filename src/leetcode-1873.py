"""1873. Calculate Special Bonus
Table: Employees

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+
employee_id is the primary key (column with unique values) for this table.
Each row of this table indicates the employee ID, employee name, and salary.

Write a solution to calculate the bonus of each employee. The bonus of an
employee is 100% of their salary if the ID of the employee is an odd number and
the employee's name does not start with the character 'M'. The bonus of an
employee is 0 otherwise.

Return the result table ordered by employee_id.

The result format is in the following example.
"""

import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    """
    a. `(employees["employee_id"] % 2 != 0)` creates a boolean Series where
       True means the employee_id is odd.

    b. `~employees["name"].str.startswith("M")` creates a boolean Series where
       True means the name does not start with 'M'.

    c. The & will check that each element (True/False) in the two Series
       have the same true value by taking the intersection of bits.
    """
    employees["bonus"] = (employees["employee_id"] % 2 != 0) & (
        ~employees["name"].str.startswith("M")
    ) * employees["salary"]
    return employees[["employee_id", "bonus"]].sort_values("employee_id")

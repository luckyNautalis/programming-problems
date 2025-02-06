"""
Table: Employee

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.

 

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.

 

Write a solution to find employees who have the highest salary in each of the departments.

Return the result table in any order.

The result format is in the following example.
"""

import pandas as pd


def department_highest_salary(
    employee: pd.DataFrame, department: pd.DataFrame
) -> pd.DataFrame:
    """
    Algorithmic Paradigm: Iterative
    Programming Paradigm: Imperative
    Complexity:
        - Time: O(n^2), where n is the number of rows in the employee DataFrame.
        - Space: O(n), where n is the number of rows in the employee DataFrame.
    """
    if len(employee) == 0:
        return pd.DataFrame(columns=["Department", "Employee", "Salary"])

    # for id in employee table include row if salary == department max salary
    max_rows = []
    for id, row in employee.iterrows():
        dep_id = row["departmentId"]
        dep_max = employee.loc[employee["departmentId"] == dep_id, "salary"].max()
        if row["salary"] == dep_max:
            max_rows.append(row)

    max_dep_salaries = pd.DataFrame(max_rows)
    max_dep_salaries.drop(labels="id", axis=1, inplace=True)
    max_dep_salaries.reindex(columns=["departmentId", "name", "salary"])
    max_dep_salaries.rename(
        columns={"departmentId": "Department", "name": "Employee", "salary": "Salary"},
        inplace=True,
    )
    cols = ["Department"] + [
        col for col in max_dep_salaries.columns if col != "Department"
    ]
    max_dep_salaries = max_dep_salaries[cols]
    max_dep_salaries.Department = max_dep_salaries.Department.map(
        department.set_index("id")["name"]
    )
    return max_dep_salaries

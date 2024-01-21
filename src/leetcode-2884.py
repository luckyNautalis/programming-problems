#!/usr/bin/env python3
# Problem 2884: Modify Columns
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary']*=2
    return employees

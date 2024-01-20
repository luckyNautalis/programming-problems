#!/usr/bin/env python3
# Problem 2881: Create a New Column
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary']*2
    return employees

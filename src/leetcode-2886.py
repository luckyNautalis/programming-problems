#!/usr/bin/env python3
# Problem 2886: Change Data Type
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
   students['grade'] = students['grade'].astype(int)
   return students

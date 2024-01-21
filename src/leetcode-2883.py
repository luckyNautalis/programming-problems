#!/usr/bin/env python3
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students_clean = students.dropna(subset='name')
    return students_clean

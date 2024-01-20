#!/usr/bin/env python3
# Problem 2880: Select Dataimport pandas as pd
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101, ['name', 'age']]

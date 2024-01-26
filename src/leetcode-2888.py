#!/usr/bin/env python3
# Problem 2888: Reshape Data (Concatonate)
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return df1._append(df2)

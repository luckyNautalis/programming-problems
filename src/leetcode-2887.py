#!/usr/bin/env python3
# Problem 2887: Fill Missing Data
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(value=0, inplace=True)
    return products

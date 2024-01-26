#!/usr/bin/env python3
# Problem 2890: Reshape Data: Melt
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    report_quarterly_sales: pd.DataFrame = pd.melt(report, id_vars='product',
                                                   var_name='quarter', value_name='sales')
    return report_quarterly_sales

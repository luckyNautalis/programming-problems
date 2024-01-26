#!/usr/bin/env python3
# Problem 2889: Reshape Data: Pivot
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    monthly_weather = weather.pivot(index='month', columns='city', values='temperature')
    return monthly_weather

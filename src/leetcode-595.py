# Problem 595: Big Countries
"""
A country is big if:

1) It has an area of at least three million (i.e., 3000000 km2).
2) It has a population of at least twenty-five million (i.e., 25000000).

Write a solution to find the name, population, and area of the big countries.
Return the result table in any order.
"""
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[(world.area >= 3_000_000) | (world.population >= 25_000_000)][['name', 'population', 'area']]

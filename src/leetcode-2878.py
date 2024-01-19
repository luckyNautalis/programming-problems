#!/usr/bin/env python3
import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [*(players.shape)] # * unpack shape tuple

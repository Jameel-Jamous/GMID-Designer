import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

# 1. The file could be empty: pandas.errors.EmptyDataError
# 2. The file does not exist: FileNotFoundError
df = pd.read_csv("../sample_data/correct.csv")
print(df.head())
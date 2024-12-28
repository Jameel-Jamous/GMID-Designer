import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

# 1. The file could be empty: pandas.errors.EmptyDataError
# 2. The file does not exist: FileNotFoundError
df = pd.read_csv("../sample_data/nmos.csv")

# example interpolate Y from X
x_data = df["vov"].to_numpy()
y_data = df["gmid"].to_numpy()

print(df.head())
# NOTE: Probably want to call this using its index name
X_poi = 0.655
#interpXY = interp1d(x_data, y_data, kind='linear')
#Yest = interpXY(X_poi)
#print(f"SCIPY: X: {X_poi} Y: {Yest}")

# interpolation Y from X using numpy
# NOTE: Interpolator returns the last value when interpolating near edges
Yest_1 = np.interp(X_poi,x_data,y_data)
print(f"NUMPY: X: {X_poi} Y: {Yest_1}")

Y_poi = 9.0
# example interpolate X from Y
#interpYX = interp1d(y_data, x_data, kind='linear')
#Xest = interpYX(Y_poi)
#print(f"SCIPY: X: {Xest} Y: {Y_poi}")

# interpolation X from Y using numpy
Xest_1 = np.interp(8.85,y_data,x_data)
print(f"NUMPY: X: {Xest_1} Y: {Y_poi}")

# example of plotting
plt.plot(x_data,y_data)
plt.title("Basic Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


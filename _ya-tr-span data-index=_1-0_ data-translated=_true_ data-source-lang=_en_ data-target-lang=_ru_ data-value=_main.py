import pandas as pd
import numpy as np
data = pd.read_csv("large_file.csv")
processed_data = []
for row in data:
 if row[0] == "value":
  processed_data.append(np.mean(row[1:]))
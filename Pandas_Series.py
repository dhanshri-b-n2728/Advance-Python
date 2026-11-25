import numpy as np
import pandas as pd

random_numbers = np.random.randint(1, 100, 10)

series = pd.Series(random_numbers)

print("Pands series:")
print(series)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, pearsonr

df = pd.read_csv("/content/raw_data_frailty.csv")
df.shape
df.info()
df.dtypes



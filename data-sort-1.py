# %%

import os
import pandas as pd
import pyarrow as pa
import datetime

today = datetime.datetime.now().strftime("%y-%m-%d")

folder = "/Users/rileybathurst/Developer/sierra-pay"

time_df = pd.read_csv(f"{folder}/Timesheets Report Cleaned.csv")

print(time_df.head())
# %%

# %%
import os
# import pandas as pd
# import pyarrow as pa
# import datetime

today = datetime.datetime.now().strftime("%y-%m-%d")

folder = "/Users/rileybathurst/Developer/sierra-pay"

# time_long = pd.read_csv(f"{folder}/Times_2024-01-18.csv")
time_df = pd.read_csv(f"{folder}/Time.csv")
      
      
# %%


# def function to read .txt with text before the header lines
# need to put in seperate file under /LKH so can call ::
def read_data_with_header(fn_i, header_keyword):

    with open(fn_i, 'r') as f:
        lines = f.readlines()

    # Find the header line
    header_index = None
    for i, line in enumerate(lines):
        if header_keyword in line:
            header_index = i
            break

    if header_index is None:
        raise ValueError(f"Header keyword '{header_keyword}' not found in file.")

    # Read the data into a dataframe
    df = pd.read_csv(fn_i, skiprows=header_index, delimiter='\t')

    return df
  
  
header_keyword = 'datetime_utc	SST	SSS	pCO2_sw	pCO2_air	xCO2_air	pH_sw	DOXY	CHL	NTU'

in_fn = posixpath.join(in_dir, (sn +'.txt'))

df = read_data_with_header(in_fn, header_keyword)

dt = pd.to_datetime(df.datetime_utc)
IT = np.array(df.SST)
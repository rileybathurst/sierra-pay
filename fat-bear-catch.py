# this caluates if someone worked more than 40 hours in a week
import pandas as pd

sierra = pd.read_csv("Timesheets Report 11_27_2023-12_10_2023-2.csv", on_bad_lines='skip', skiprows=1)

try:
  sierra = pd.read_csv("/hello/Timesheets Report 11_27_2023-12_10_2023-2.csv", on_bad_lines='skip', skiprows=1)

  print("hello")

except:
  sierra = pd.read_csv("Timesheets Report 11_27_2023-12_10_2023-2.csv", on_bad_lines='skip', skiprows=1)

  print("hello2")
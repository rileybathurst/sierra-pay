from google.colab import drive
drive.mount('/content/drive')

import datetime

date_created = datetime.datetime.now()  # Get the current date and time
date_str = date_created.strftime("%Y-%m-%d")  # Format the date as a string

try:
  sierra = pd.read_csv(f"/content/drive/MyDrive/Jobber Reports/Times_{date_str}.csv", on_bad_lines='skip', skiprows=1)

except:
  sierra = pd.read_csv(f"/content/drive/MyDrive/pay/Times_{date_str}.csv", on_bad_lines='skip', skiprows=1)
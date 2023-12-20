a = 3

names = [
  'Allen',
  'Steve',
]

for name in names:
  weekly_time = {name + '_weekly': 0 for name in names}

for name in names:
  weekly_time[f'{name}_weekly'] += a

for name, time in weekly_time.items():
  print(f"{name}: {time}")

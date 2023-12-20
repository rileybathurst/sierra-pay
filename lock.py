with open('.env', 'r') as f:
    for line in f:
        if 'exceptions' in line:
            exceptions = line.strip()

print(f"The contents of the .gitignore file are: {exceptions}")
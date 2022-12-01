# temporary file

import os

i = 0
data_path = "test1"
pyfiles = []
dirnames = os.listdir(data_path)
for dir in dirnames:
    #if filename[-3:] == ".py":
    full = os.path.join(data_path, dir)
    dirnames2 = os.listdir(full)
    full = os.path.join(full, min(dirnames2, key=len))
    full = os.path.join(full, "kodu1.py")
    with open(full, 'r') as f:
        contents = f.read()
    with open(str(i)+".py", 'w') as f:
        f.write(contents)
    i += 1

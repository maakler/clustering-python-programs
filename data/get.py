 # temporary file

import os

#i = 0
data_path = "test2"
pyfiles = []
dirnames = os.listdir(data_path) # student codes
for dir in dirnames:
    #if filename[-3:] == ".py":
    full = os.path.join(data_path, dir)
    dirnames2 = sorted(os.listdir(full)) # submissions
    full = os.path.join(full, dirnames2[-2])
    full = os.path.join(full, "kodu2.py")
    try:
        with open(full, 'r') as f:
            contents = f.read()
        with open(dir+".py", 'w') as f:
            f.write(contents)
        #i += 1
    except Exception:
        pass

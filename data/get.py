import os
import shutil


for i in range(1, 16):
    if i == 6 or i == 12:
        continue
    for j in range(1, 5):
        num = "0" * (2 - len(str(i))) + str(i)
        dir_path = "C:/Users/oliver/Documents/Sissejuhatus Andmeteadusesse/clustering-python-programs/data/Masinõpe/K" + num
        filename = "kodu" + str(j)
        dest_dir = "C:/Users/oliver/Documents/Sissejuhatus Andmeteadusesse/clustering-python-programs/data/K" + num + filename

        # Get the current working directory

        # Get the names of each subdirectory
        subdirs = [d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d))]

        # Iterate over the subdirectories
        for subdir in subdirs:
            # Get a list of all the directories in the current directory
            print(subdir)
            directories = [d for d in os.listdir(os.path.join(dir_path, subdir)) if os.path.isdir(os.path.join(dir_path, subdir, d)) and "." not in d]
            if len(directories) > 0:
                latest_directory = directories[-1]

                # Construct the path to the file in the subdirectory
                file_path = os.path.join(dir_path, subdir, latest_directory, filename + ".py")
                if not os.path.isfile(file_path):
                    continue

                # Check if the destination directory exists
                if not os.path.exists(dest_dir):
                    # Create the destination directory if it doesn't exist
                    os.mkdir(dest_dir)

                # Construct the path to the destination file
                dest_file_path = os.path.join(dest_dir, subdir + ".py")

                # Move the file to the destination directory

                shutil.copyfile(file_path, dest_file_path)

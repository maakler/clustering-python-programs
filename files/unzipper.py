import os
import zipfile
import constants as c

os.chdir(c.PARENT_DIR)  # change directory from working dir to dir with files

for item in os.listdir(c.PARENT_DIR):  # loop through items in dir
    if item.endswith(c.EXTENSION):  # check for extension
        file_name = os.path.abspath(item)  # get full path of files
        directory = os.path.basename(item).split('.')[0]
        print(directory)
        zip_ref = zipfile.ZipFile(file_name)  # create zipfile object
        path = os.path.join(c.PARENT_DIR, directory)
        os.mkdir(path)
        zip_ref.extractall(path)  # extract file to dir
        zip_ref.close()  # close file
        os.remove(file_name)  # delete zipped file

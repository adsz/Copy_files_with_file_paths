source_path = "D:\Hitachi Kursy i ebooki_test"
destination_path = "D:\Hitachi Kursy i ebooki - Rafal"
extension = ".txt"

import os
from shutil import copyfile
file_names = []

for root, dirs, files in os.walk(source_path):
    for file in files:
        if file.endswith(extension):
            file_old_path = os.path.join(root, file)
            file_new_path = file_old_path.replace(source_path,destination_path)
            new_folder = os.path.dirname(file_new_path)
            print(new_folder)
    
            try:
                os.stat(new_folder)
            except:
                os.makedirs(new_folder)   
            copyfile(file_old_path,file_new_path)
 #file_names.append(file_new_path)
 

''' #ALTERNATIVE WAY 
for dirname, dirnames, filenames in os.walk(source_path):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        for filename in filenames:
            file_names.append(os.path.join(dirname, filename))

'''

print(file_names)
print (str(len(file_names)))

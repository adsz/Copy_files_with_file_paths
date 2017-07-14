source_path = "D:\Hitachi Kursy i ebooki_test"
destination_path = "D:\Hitachi Kursy i ebooki - Rafal"

import os
file_names = []

for root, dirs, files in os.walk(source_path):
    for file in files:
        if file.endswith(".txt"):
             file_names.append(os.path.join(root, file))

''' #ALTERNATIVE WAY 
for dirname, dirnames, filenames in os.walk(source_path):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        for filename in filenames:
            file_names.append(os.path.join(dirname, filename))

'''

print(file_names)

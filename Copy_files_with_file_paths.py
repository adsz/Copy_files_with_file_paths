'''
Adding os module
'''
import os
from shutil import copyfile

SOURCE_PATH = "D:\\Hitachi Kursy i ebooki"
DESTINATION_PATH = "D:\\Hitachi Kursy i ebooki - Rafal"
EXTENSION = ".pdf"


FILE_NAMES = []

for root, dirs, files in os.walk(SOURCE_PATH):
    for file in files:
        print(file)
        if file.endswith(EXTENSION):
            FILE_OLD_PATH = os.path.join(root, file)
            FILE_NEW_PATH = FILE_OLD_PATH.replace(SOURCE_PATH, DESTINATION_PATH)
            NEW_FOLDER = os.path.dirname(FILE_NEW_PATH)
            print(NEW_FOLDER)

            try:
                os.stat(NEW_FOLDER)
            except ValueError:
                os.makedirs(NEW_FOLDER)
            copyfile(FILE_OLD_PATH, FILE_NEW_PATH)
#FILE_NAMES.append(FILE_NEW_PATH)

'''#ALTERNATIVE WAY
for dirname, dirnames, filenames in os.walk(source_path):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        for filename in filenames:
            FILE_NAMES.append(os.path.join(dirname, filename))

'''

print(FILE_NAMES)
print(str(len(FILE_NAMES)))

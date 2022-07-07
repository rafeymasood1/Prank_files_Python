# warning; this code creates 500 files in your computer if the 14th line is altered

import os

# windows desktop
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


for i in range(500):

    new_folder = 'Virus' + str(i)
    folder_path = os.path.join(desktop, new_folder)

#     os.mkdir(folder_path)        # uncomment this to create 500 files

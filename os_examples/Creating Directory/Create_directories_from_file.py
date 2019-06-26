# -*- coding: utf-8 -*-
 
base_path = './../'
 
import os
file_list = os.listdir(base_path)
 
print(file_list)
 
for filepath in file_list:
    full_path = os.path.join(base_path, filepath)
    with open(full_path) as file_:
        contains = file_.read().split()[1] #~ Read dirs to create from file
        new_folder = os.path.join(base_path, contains)
        try:
            os.mkdir(new_folder)
            print("Folder ", new_folder, " utworzony.")
        except FileExistsError:
           print("Folder ", new_folder, " już istnieje.")

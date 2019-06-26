import os
import shutil
from sys import argv as ar
from time import time as tm
from datetime import *

def main():
    if len(ar)<2:
        a=input("Podaj nazwę katalogu/ścieżkę: ")
        b=input("Podaj nazwę rozszerzenia: ")
    elif len(ar)<3:
        a=ar[1]
        b=input("Podaj nazwę rozszerzenia: ")
    elif len(ar)<4:
        a=ar[1]
        b=ar[2]
    else:
        exit('''Too many arguments for function.
Enter path and extension of files to backup.''')

    #~ #Useless, but said us what files were seen :).
    #~ for file in os.listdir(a):
        #~ if file.endswith(b):
            #~ print(os.path.join(a, file))

    #tm() is time now - time in secounds into past.
    do_backup=tm()-(60*60*24)
    data_backup = datetime.now().strftime("%d.%m.%Y %H:%M")

    #Backup directory and data for copy dir.
    out_dir = str(a)+"Backup/copy-"+str(data_backup)
    os.makedirs(out_dir, exist_ok=True)

    #List of files
    src_files = os.listdir(a)
    for file_name in src_files:
        #Concat file with path
        full_file_name = os.path.join(a, file_name)
        #Check when was changed
        file_date = os.stat(full_file_name).st_mtime
        #If changed during last do_backup time.
        if do_backup < file_date:
            #If extension is valid.
            if full_file_name.endswith(b):
                #Make its copy into.
                shutil.copy(full_file_name, out_dir)

if __name__ == "__main__":
    main()

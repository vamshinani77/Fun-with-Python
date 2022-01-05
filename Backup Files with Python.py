#!/usr/bin/env python3
import subprocess
from multiprocessing import Pool

import os


def backup(src):
        dest=os.getcwd() + "path from the current directory"
        print("backing UP {} into {}".format(src,dest))
        subprocess.call(["rsync","-arq",src,dest])

if __name__ == "__main__":
        src=os.getcwd() + "path to the backup directory"
        list_of_files=os.listdir(src)
        all_files=[]

        for value in list_of_files:
                full_path=os.path.join(src,value)
                all_files.append(full_path)

        with Pool(len(all_files)) as pool:
                pool.map(backup,all_files)


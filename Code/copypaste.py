#!/usr/bin/env python
import time
import shutil
import os.path
from os import path

src = r"C:\Users\Okabe\OneDrive\Documents\GitHub"

dst = r"C:\xampp\htdocs\Github"

if os.path.isdir(dst):
    shutil.rmtree(dst)
    print('Deleted Folder\n')
    time.sleep(1)
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns('.git*'))
    print('Copied')
else:
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns('.git*'))
    print('Copied')
time.sleep(1.5)

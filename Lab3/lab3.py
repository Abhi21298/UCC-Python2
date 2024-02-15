## Labsheet 3
import os
import shutil
import re

## Question 1
def setup(submissions, assignment):
    pattern = str("[a-z]+_"+assignment)
    regexp = re.compile(pattern)
    if os.path.exists(submissions) and os.path.isdir(submissions):
        os.chdir(submissions)
        contents = os.listdir(submissions)
        for item in contents:
            if os.path.isfile(item) and regexp.search(item)!=None:
                fold, file = item.split('_')
                os.mkdir(fold)
                shutil.copy(item, os.path.join(fold, file))
            elif os.path.isfile(item) and ((assignment not in item) or (".py" not in item)):
                print("broken file with file name :", item)

setup("D:\\UCC\\Sem-2\\CS6507 - Python 2\\Labs\\UCC-Python2\\Lab3\\testing", "assignment1.py") 
                
## Question 2
def locate(root, filename):
    if filename == "" or root == "":
        print("enter a valid root directory or file name to search for")
        exit(0)

    print(filename)
    if os.path.exists(root) and os.path.isdir(root):
        os.chdir(root)
        for rt, dirs, files in os.walk(root):
            if filename in files:
                print("File found in :", rt)
                print("Absolute path :", rt+ "\\" + filename)
                print("-----------------------------------------")

                
locate("D:\\UCC\\Sem-2\\CS6507 - Python 2\\Labs\\UCC-Python2\\Lab3\\testing", "locater.txt") 
 
## Question 3
def setup_edited(submissions, assignment):
    pattern = str("[a-z]+_"+assignment)
    regexp = re.compile(pattern)
    if os.path.exists(submissions):
        os.chdir(submissions)
        contents = os.listdir(submissions)
        for item in contents:
            if os.path.isfile(item) and regexp.search(item)!=None:
                fold, file = item.split('_', maxsplit = 1)
                os.mkdir(fold)
                shutil.copy(item, os.path.join(fold, file))
            elif os.path.isfile(item) and ((assignment not in item) or (".py" not in item)):
                print("broken file with file name :", item)

setup_edited("D:\\UCC\\Sem-2\\CS6507 - Python 2\\Labs\\UCC-Python2\\Lab3\\testing", r'[aA]ssignment(_)?1.py') 
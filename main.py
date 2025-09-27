#   a loop runs
#       stores the file name and extention in a list
#       loop in the list
#           detects the extention
#           moves the file to designated directory according to the extention
#       wait for t secounds
import time
import os

def extractExtention(fileName):
    for i in range (len(fileName)-1,-1,-1) : # remember ranges stops at one element before
        if fileName[i] == ".":
            break
        else:
            continue

    ext=fileName[i:]
    return ext

delay=30
path="~/Downloads"
downloadDir=os.path.expanduser(path)    #os.listdit cant recognise ~/   && we will not know or need to know username
while True:
    containts=os.listdir(downloadDir)
    for i in containts:
        print(extractExtention(i))
    time.sleep(delay)

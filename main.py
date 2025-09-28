#   a loop runs
#       stores the file name and extention in a list
#       loop in the list
#           detects the extention
#           moves the file to designated directory according to the extention
#       wait for t secounds
import time
import os
from func_lib import destinationPath, extractExtention

delay=30
path="~/Downloads"
downloadDir=os.path.expanduser(path)    #os.listdit cant recognise ~/   && we will not know or need to know username
while True:
    containts = os.listdir(downloadDir)
    for i in containts:
        print(extractExtention(i), " > ", destinationPath(extractExtention(i)))
    time.sleep(delay)

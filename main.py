#   a loop runs
#       stores the file name and extention in a list
#       loop in the list
#           detects the extention
#           moves the file to designated directory according to the extention
#       wait for t secounds
import time
import os
import shutil
from func_lib import destinationPath, extractExtention, noChange

delay=30
path="~/Downloads/"
downloadDir=os.path.expanduser(path)    #os.listdit cant recognise ~/   && we will not know or need to know username
try:
    while True:
        containts = os.listdir(downloadDir)
        for i in containts:
            expand_i=downloadDir+i
            if (os.path.isdir(expand_i)):
                noChange(i)
                continue
            extention=extractExtention(i)
            if (extention==i):
                noChange(i)
                continue
            # print (extention)
            destinationDir=os.path.expanduser(destinationPath(extention))
            if (destinationDir==downloadDir):
                noChange(i)
                continue
            try:
                des=shutil.move(downloadDir+i,destinationDir)
                print(f"{i} -> {des}")
            except FileNotFoundError as e:
                print (e)
            except FileExistsError as e:
                print (e)
        time.sleep(delay)

except KeyboardInterrupt:
    print(" Program Terminated gracefully")

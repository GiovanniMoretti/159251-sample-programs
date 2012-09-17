
# List all of my files omitting some paths - to help find lost files
# dump the resulting list of files to the outfile.
import os,md5

from os.path import join, getsize

outfile   = open("C:/Giovanni/Filelist.txt","w");

exclusions = [ "_svn", "_vti", ".dcu", "/Apps", "/Teaching", "/Config"]

for root, dirs, files in os.walk('C:/Giovanni'):

    for name in files:
        fullname = root + "\\" + name
        matchCount = 0
        for leaveOut in exclusions:
            matchPos = fullname.find(leaveOut)
            if (matchPos != -1):
              matchCount = matchCount+1    
        if matchCount != 0: continue
        output = fullname + "\n"
        # print output
        outfile.write(output)       
outfile.close()

          
          
         

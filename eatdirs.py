"""A simple program to get rid of a specified directory in a directory hierarchy,
e.g. to remove all _svn directories."""

# Written by Giovanni Moretti, Feb 4, 2011

import os, os.path, sys, shutil, stat

if len(sys.argv) != 2:
    print "Usage: cleanDirs <targetDir> -- where <target> is directory to be removed"
    exit(1)

target = sys.argv[1]

#==============================================================================
# Error Handler for SHUTIL.RMTREE() - Remove READONLY attribute
#==============================================================================
   
def on_rm_error( func, path, excinfo):
    # path contains the path of the file that couldn't be removed
    # let's just assume that it's read-only and unlink it.
    if os.name == "nt":
        os.system('attrib -R "%s"' % path)
    else:
        os.chmod( path, stat.S_IWRITE )
        os.unlink( path )

#==============================================================================    
startDir = os.getcwd()  # Get the current working directory

killList = []
print "StartDir = ", startDir

for root, dirs, files in os.walk(startDir, topdown=False):
    if target in dirs:
        fullpath = os.path.join(root, target)
        killList.append(fullpath)
        print "found: ", fullpath


reply = raw_input("Proceed with Deletion (y/n/q): ")
while reply.upper() not in ["Y", "YES", "N", "NO", "Q", "QUIT"]:
    reply = raw_input("Proceed with Deletion:")

    
delCount  = 0
failList = []
if reply[0].upper() != "Y": exit(0)
else:
    for directory in killList:
       try:
           shutil.rmtree(directory, onerror = on_rm_error)
           delCount += 1
       except:
           print "Failed to Del: ", directory
           failList.append(directory)
           raise

print "%d directories deleted" % delCount
print failList
if len(failList) > 0:
    print "Following NOT deleted:"
    print "FailList: ", failList
    for p in failList:
       print "   ", p

#fileAtt = os.stat(myFile)[0]
#if (not fileAtt & stat.S_IWRITE):
#   # File is read-only, so make it writeable
#   os.chmod(myFile, stat.S_IWRITE)

# Checking for read/write access
#           files = os.listdir(directory)
#           for thisfile in files:
#               filepath = os.path.join(directory, thisfile)
#               mode = os.stat(filepath).st_mode
#               os.chmod(filepath, stat.S_IWRITE)
#               print "Writable #2:", os.access(filepath, os.W_OK)
#           # Now all files read-only, try again
#           try:
#               print "Deletion 2:", directory
#               shutil.rmtree(directory, onerror=on_rm_error)
#           except:               
   

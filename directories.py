""" 
  Display the directories in a directory tree to a specified depth,
  optionally omitting directories named in an exclude list.
  by Giovanni Moretti, July 20, 2011
"""
import os, os.path

def showDirs(startDir, depth, maxDepth, exclude = []):
    if depth == 0: print "\n", startDir.upper()
    depth +=1
    contents = os.listdir(startDir)
    for n in contents:
       if os.path.isdir(os.path.join(startDir, n)):
           if n.upper() in exclude:
                continue

           if depth == 1 and maxDepth !=1:
                 print "\n", "==="*depth, n.upper()
           else: print "---"*depth, n

           # recurse if not yet at maximum desired depth
           if depth < maxDepth:
                showDirs(os.path.join(startDir, n) , depth, maxDepth)
                

showDirs("C:/Users", 0, 1)

print "="*80


# all but the 'Download' and 'My Music' directories
print "="*80
showDirs("C:/Users/Fred", 0,2, [n.upper() for n in ["Download", "My Music"]])

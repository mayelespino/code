#!/usr/bin/python
"""
Write a function that takes the current directory path and a target path and returns an absolute path that is equivalent to the target path.
 E.g. current directory /home/andy, target ./bin/foo, absolute /home/andy/bin/foo

Author: Mayel Espino
"""
import re

def absoluteTargetPath(inSource, inTarget):
    #first find if target Path is already in absolute format.
    matchGroup = re.match('^/.*$', inTarget)
    if matchGroup is not None:
        return inTarget

    # Now determine what kind of relative path it is.
    # Begins with ./ - in this case merge with the current path
    matchGroup = re.match('^\./.*$', inTarget)
    if matchGroup is not None:
        newTarget = inSource+inTarget
        return newTarget.replace('./','/')

    # Begins with  ~/ - in this case return $(HOME)/rest/of/path
    matchGroup = re.match('^\~/.*$', inTarget)
    if matchGroup is not None:
        newTarget = "$(HOME)"+inTarget
        return newTarget.replace('~/','/')

    # Begins with  $(HOME)/ - in this case return $(HOME)/rest/of/path
    # Begins with $VAR/ - in this case return an error.
    matchGroupOne = re.match('^\$.*/.*$', inTarget)
    matchGroupTwo = re.match('^\$\(HOME\)/.*$', inTarget)
    if matchGroupTwo is not None:
        return inTarget
    elif matchGroupOne is not None and matchGroupTwo is None:
        return "ERROR"

    matchGroup = re.match('^\./.*$', inTarget)
    if matchGroup is not None:
        return "./"

    return "Target path is not properly formed."

if __name__ == '__main__':

    print absoluteTargetPath("/x/y/z", "/a/b/c")
    print absoluteTargetPath("/x/y/z", "./a/b/c")
    print absoluteTargetPath("/x/y/z", "~/a/b/c")
    print absoluteTargetPath("/x/y/z", "$(HOME)/a/b/c")
    print absoluteTargetPath("/x/y/z", "$(OTHER)/a/b/c")
    print absoluteTargetPath("bla", "bla")

# NOTE:
# Ofcoure I could have just used :
#   import os
#   os.path.abspath("mydir/myfile.txt")
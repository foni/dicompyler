#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
""" Several utility functions that don't really belong anywhere"""

import imp, os, sys

def GetResourcePath(resource):
    """Return the specified item from the resources folder."""

    if main_is_frozen():
        return os.path.join((os.path.join(get_main_dir(), 'resources')), resource)
    else:
        return os.path.join((os.path.join(os.getcwd(), 'resources')), resource)

# from http://www.py2exe.org/index.cgi/HowToDetermineIfRunningFromExe
def main_is_frozen():
   return (hasattr(sys, "frozen") or # new py2exe
           hasattr(sys, "importers") # old py2exe
           or imp.is_frozen("__main__")) # tools/freeze

def get_main_dir():
   if main_is_frozen():
       return os.path.dirname(sys.executable)
   return os.path.dirname(sys.argv[0])
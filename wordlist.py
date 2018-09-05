#!/usr/bin/python

import sys
import itertools

if __name__ == "__main__":

   argsLen = len(sys.argv)
   args = sys.argv[1:]

   for i in range(1, len(args)+1 ):
      for wd in list( itertools.permutations(args, i) ):
         print "".join( list(wd) )

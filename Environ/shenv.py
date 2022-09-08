# !/usr/bin/env python
# -*- coding: cp1251 -*-
# Author: Anatoly Belyakov  <aabelyakov@mail.ru>
# Created: 18.02.2010
# Purpose: shenv.py - Show environment variables.
# Ned Batchelder, http://www.nedbatchelder.com
#############################################################################
import os, sys
#############################################################################
def showVar(varName, indent=''):
    val = os.environ[varName]
    for p in val.split(';'):
        print indent, p
    #endfor    
#enddef
#============================================================================
def showVars(prefix):
    varNames = os.environ.keys()
    varNames.sort()
    for varName in varNames:
        if varName.lower().startswith(prefix.lower()):
            print varName
            showVar(varName, '   ')
        #endif
    #endfor    
#enddef
#============================================================================
if __name__ == '__main__':
    if len(sys.argv) > 1:
        showVars(sys.argv[1])
    else:
        showVars('')
    #endif
#endif
#############################################################################

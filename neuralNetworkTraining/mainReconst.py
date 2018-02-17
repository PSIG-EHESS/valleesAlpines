# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 13:46:48 2017

@author: Pierre
"""

import glob
import sys
sys.path.insert(0, 'running/main.py')

import main as m

def t():
    filepath = glob.glob('running\Test_bois_hv\*.jpg')
    for i in range(0,len(filepath)):
        m.main(filepath[i],'image{}'.format(i))
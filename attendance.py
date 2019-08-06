#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 12:54:29 2019

@author: suchithrakv
"""

import csv
with open('attendance.csv','w',newline='')as f:
    fieldnames=['column1','column2','column3']
    thewriter=csv.DictWriter(f,fieldnames=fieldnames)
    thewriter.writeheader()
    thewriter.writerow({'column1':'one','column2':'two','column3':'three'})
    
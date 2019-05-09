#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:15:25 2019

@author: leealex
"""

# This is an exploratory analysis script.

import os

pwd = os.getcwd()
data_path = pwd + '/WhiteTextGATEDataStoreV1.3/neuroscience_abstract.txt'

# we are only interested in the body of the abstract
targ_word = "<AbstractText>"

# get the number of lines in the text file.
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def get_abstract(data_path, targ_word, line_length):
    f = open(data_path)
    line = f.readline()
    counter = 0
    list_of_abstracts = []
    
    while counter <= line_length:
        if targ_word in line:
            # the target word exists in this line.
            list_of_abstracts.append(line)
        line = f.readline() # move on to the next line
        counter += 1
    
    f.close()
    
    return list_of_abstracts

def get_brain_region(abstract):
    BR = []
    for this_abstract in abstract:
        for i in range(len(this_abstract)):
            if this_abstract[i:i+2] == "<B":
                # starting of the brain region tag. Find the end of the brain region
                this_end = i
                for ii in range(i+1, len(this_abstract)):
                    if this_abstract[ii:ii+2] == "</":
                        this_end = ii
                        break
                    
                BR.append(this_abstract[i+13:this_end])
                
    return(BR)
    
# get the total length of the text file
line_length = file_len(data_path)

# scrape out only abstract    
# abstracts variable is a 'list'
abstracts = get_abstract(data_path, targ_word, line_length)

# scrape out only brain region
# brain_region is a list of brain regions
brain_region = get_brain_region(abstracts)

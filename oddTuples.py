# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 11:03:44 2019

@author: Wishnuputra
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    newTup = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            tup = (aTup[i],)
            newTup += tup

    return newTup

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))    
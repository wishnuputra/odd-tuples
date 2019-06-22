# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 11:27:54 2019

@author: Wishnuputra
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    return aTup[::2]

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))
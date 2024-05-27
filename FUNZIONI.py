# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:08:41 2024

@author: dalil
"""

import json

def caricafile (file_path):
    with open(file_path,'r') as file:
        data=json.load(file)
    return data 

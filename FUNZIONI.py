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

def trovanomi (data):
    """
    Questa funzone mi aiuta ad associare ad ogni utente un numero 
    """
    user_id = {}

    identific_unico = 1
    for campo in data:       
            nome= campo[1]
            if nome not in user_id:
                user_id[nome]=identific_unico
                identific_unico += 1 
    return user_id, identific_unico

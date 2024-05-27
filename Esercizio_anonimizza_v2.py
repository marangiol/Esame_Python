# -*- coding: utf-8 -*-
"""
24 - 05 - 2024

@author: marianna - federica - dalila
"""
# File di origine Python con sottoprogrammi
import FUNZIONI as SL

file_path = 'anonimizza_test2.json'

data=SL.caricafile(file_path)
user_id, identific_unico=SL.trovanomi(data)

data=SL.sostituisci(data,user_id)
data=SL.elimina(data)   

# -*- coding: utf-8 -*-
"""
24 - 05 - 2024

@author: marianna - federica - dalila
"""
# File di origine Python del codice .txt 'Esercizio_anonimizza_v1'
import json

file_path = 'anonimizza_test2.json'

with open(file_path,'r') as file:
    data=json.load(file)
	
	
# creo un dizionario vuoto 
user_id={}

#inizializzo contatore
identific_unico=1

for campo in data:
	nome=campo[1]  
	#estraggo il nome e lo aggiungo nel dizionario vuoto
	if nome not in user_id: 
		user_id[nome]=identific_unico
		identific_unico += 1

#sostitusco nel log l’identificatore unico al nome dell’utente

for campo in data:       
        nome= campo[1]
        if nome in user_id:
            campo[1]=user_id[nome]

#elimino da tutti i log il campo “Utente coinvolto”
for campo in data:       
       campo.pop(2)

#salvo la lista di log anonimizzata nello stesso formato di partenza (json)

output ='anonimizza_13_output.json'
with open(output,'w') as file:
    json.dump(data,file, indent=4)  
    
 

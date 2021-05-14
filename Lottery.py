#Copyright (c) <2021>, <Filippo Piazza>
#All rights reserved.
#This source code is licensed under the BSD-style license found in the
#LICENSE file in the root directory of this source tree. 

file1 = open('biglietti.txt', 'r')

import secrets
import linecache

nr = 0
n = 0
p = ["Bici", "Tv", "Orologio", "Auricolare"]

#il ciclo conta le righe nel file
while True:

    n += 1
 

    #Legge la riga successiva nel file
    line = file1.readline()
 

    # Se è vuota si chiude il ciclo e smette di contare
    if not line:

        break

n = n-1 #correggo il numero dei biglietti (python conta da 0)

#Stampo informazioni
print("Ci sono ", n, " numeri")
print ()
print ("estraggo", len(p) , "premi") #len(p) scrive quanti elementi ci sono dentro p
print()
print()


#questo ciclo, per ogni premio c nell'insieme dei premi p, trova un biglietto a caso e stampa il risultato
for c in p:
    
    #genero un numero random compreso tra 1 e n (la funzione genera i numeri compresi tra zero e argomento-1)
    nr = secrets.randbelow(n)+1
    nr = int(nr) #trasformo nr in un numero intero
    
    #stampo
    print ("Il premio", c, "va al biglietto", linecache.getline('biglietti.txt', nr), "(il biglietto ", nr, "della lista)" )
    print()

    #linecache.getline('biglietti.txt', nr) legge la riga nr nel file biglietti.txt
 
file1.close()

#Copyright (c) <2021>, <Filippo Piazza>
#All rights reserved.
#This source code is licensed under the BSD-style license found in the
#LICENSE file in the root directory of this source tree. 

file1 = open('biglietti.txt', 'r')
prize = open('premi.txt', 'r')

import secrets
import linecache

nr = 0 #numero del biglietto estratto
n = 0 #numero dei biglietti esistenti
p = [] #insieme dei premi

scar = [] #insieme delle posizioni estratte
scarb = [] #insieme dei biglietti estratti


#Il ciclo importa i premi dal file premi.txt
while True:
    
    #Legge la riga successiva nel file
    line1= prize.readline()

    # Se è vuota si chiude il ciclo e smette di contare
    if not line1:

        break
    
    else:
        p.append(line1)

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
print()
print("estraggo", len(p) , "premi") #len(p) scrive quanti elementi ci sono dentro p
print()
print()


#questo ciclo, per ogni premio c nell'insieme dei premi p, trova un biglietto a caso e stampa il risultato
for c in p:
    
    while True: #questo ciclo serve a non estrarre lo stesso numero due volte
        nr = secrets.randbelow(n)+1 #genero un numero random compreso tra 1 e n (la funzione genera i numeri compresi tra zero e argomento-1)
        nr = int(nr) #trasformo nr in un numero intero

        if nr not in scar: #verifico che il numero non sia già uscito
            scar.append(nr) #se non è uscito, lo aggiungo alla lista dei numeri usciti
            break

    biglietto = linecache.getline('biglietti.txt', nr)#linecache.getline('biglietti.txt', nr) legge la riga nr nel file biglietti.txt
    scarb.append(biglietto.rstrip('\n'))#creo una lista dei biglietti vincenti
    
    #stampo
    print ("Il premio", c.rstrip('\n'), "va al biglietto", biglietto.rstrip('\n'), "(il biglietto ", nr, "della lista)" )
    print()

    



print(*scarb, sep=", ") #ristampo i biglietti vincenti
file1.close()
prize.close()

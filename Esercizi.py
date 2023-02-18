#Scrivi una funzione che prenda in input una lista di numeri e restituisca la somma di tutti i numeri nella lista.
def somma_lista(lista):
    for indice in range(len(lista)):
        somma = lista[indice] + lista[indice]
    return somma 
print(somma_lista([10, 20, 30]))

#Scrivi una funzione che prenda in input una lista di numeri e restituisca il valore massimo.
def massimo_lista(lista):
    max = 0
    for indice in range(len(lista)):
        if lista[indice] > max:
            max = lista[indice]
    return max
print(massimo_lista([1, 30, 0, 65, 6]))

#Scrivi una funzione che prenda in input una lista di stringhe e restituisca una nuova lista contenente solo le stringhe con una lunghezza maggiore di 5 caratteri.
def stringhe5(lista):
    lista_2 = []
    for stringa in lista:
        if len(stringa) > 5:
            lista_2.append(stringa)
    return lista_2
print(stringhe5(["Riccardo", "Lorenzo", "ci", "luca"]))

#Scrivi una funzione che prenda in input una lista di numeri e restituisca una nuova lista contenente solo i numeri pari.
def numeri_pari(lista):
    lista_pari = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            lista_pari.append(lista[i])
    return lista_pari
print(numeri_pari([1, 2, 3, 4, 5, 6, 7, 8]))

#Scrivi una funzione che prenda in input due stringhe e restituisca True se le due stringhe hanno lo stesso contenuto, False altrimenti.
def controllo(stringa1, stringa2):
    if stringa1 == stringa2:
        return True
    else:
        return False
print(controllo("ciao", "ciao"))

#Scrivi una funzione che prenda in input una stringa e restituisca il numero di volte che la lettera "a" appare nella stringa.
def conteggio(stringa):
    conto = 0 
    listaStringa = list(stringa)
    for carattere in listaStringa:
        if carattere == "a" or carattere == "A":
            conto += 1
    return conto
print(conteggio("Armando"))

#Scrivi una funzione che prenda in input una stringa e restituisca la stessa stringa con tutte le vocali rimosse.
def rimuovi_vocali(stringa):
    vocali = "aeiouAEIOU"
    nuova_stringa = ""
    for carattere in stringa:
        if carattere not in vocali:
            nuova_stringa += carattere
    return nuova_stringa
print(rimuovi_vocali("Ciao"))
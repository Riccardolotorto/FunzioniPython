#scrivere una funzione che faccia la somma di tutti i numeri presenti in una lista
def sommatrice(lista):
    somma = 0
    for numero in lista:
        somma += numero
    return somma
print(sommatrice([10, 20, 30, 60]))

#scrivere una funzione che faccia il prodotto di tutti i numeri presenti in una lista
def moltiplicatore(lista):
    prodotto = 1
    for numero in lista:
        prodotto *= numero
    return prodotto
print(moltiplicatore([10, 20, 30, 60]))

#Scrivi una funzione a cui passerai come parametro una stringa, e che manderà in print una versione inversa (al contrario) della stessa stringa (ad esempio "abcd" diventerà "dcba")
def reversed(stringa):
    return stringa[::-1]
print(reversed("ciao"))

#Scrivi una funzione che data in ingresso una lista A contenente n parole, restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.
def lunghezza_stringhe(lista):
    return [len(elemento) for elemento in lista]
print(lunghezza_stringhe(["luca", "riccardo", "marco"]))

#Scrivi una funzione a cui passare una stringa come parametro, e che restituisca un dizionario rappresentante la "frequenza di comparsa" di ciscun carattere componente la stringa.
def dizionario_comparsa(stringa):
    lista_carattere = [carattere for carattere in stringa]
    return {lista_carattere[i]: lista_carattere.count(lista_carattere[i]) for i in range(len(lista_carattere))}
print(dizionario_comparsa("ciao mondo"))

#Scrivi una funzione a cui vengono passati come parametro un elemento e una lista di elementi, e che ti dica in output se l'elemento passato sia presente o meno nella lista.
def dentro(elemento, lista):
    if elemento in lista:
        return True, lista.index(elemento)
    else:
        return False
print(dentro("ciao", ["ciao", "prova", "luca"]))

#Scrivi una funzione che, a scelta dell'utente, calcoli l'area di: un cerchio, un quadrato, un rettangolo, un triangolo
def geometria(figura):
    area = 0
    if figura == "cerchio":
        raggio = float(input("inserisci il valore del raggio: "))
        area = (raggio**2) * 3.14
    elif figura == "quadrato":
        lato = float(input("inserisci il valore del lato: "))
        area = lato**2
    elif figura == "rettangolo":
        base = float(input("inserisci il valore della base: "))
        altezza = float(input("inserisci il valore dell'altezza: "))
        area = base * altezza
    elif figura == "triangolo":
        base = float(input("inserisci il valore della base: "))
        altezza = float(input("inserisci il valore dell'altezza: "))
        area = (base * altezza) / 2
    return area
print(geometria("quadrato"))

#Scrivi una semplice funzione che converta un dato numero di giorni, ore e minuti, passati dall'utente tramite funzione input, in secondi.
def secondi_convertitore(ore, minuti):
    secondi = 0
    secondi = (minuti * 60) + (ore * 3600)
    return secondi
print(secondi_convertitore(4, 42))
#creare una funzione che accetti una lista di stringhe e restituisca una nuova lista con le parole che iniziano con una lettera scelta dall'utente
def iniziale(lista, iniziale):
    lista_iniziale = []
    for i in range(len(lista)):
        if lista[i].startswith(iniziale):
            lista_iniziale.append(lista[i])
    return lista_iniziale
print(iniziale(["ciao", "como", "luca", "armando"], "a"))

#scrivere una funzione che accetti una lista di numeri interi e restituisca una nuova lista che contenga i numeri primi
def trova_primi(lista):
    primi = []
    for numero in lista:
        if numero > 1:
            for i in range(2, numero):   #il ciclo parte da 2 (il primo numero primo) e arriva fino al numero - 1
                if (numero % i) == 0:
                    break
            else:
                primi.append(numero)
    return primi
print(trova_primi([10, 2, 7, 33, 32, 37]))

#scrivere una funzione che accetti una stringa e restituisca una nuova stringa senza le consonanti
def stringa_no_consonanti(stringa):
    consonanti = "bcdfghjklmnpqrstvwxyz"
    nuova_stringa = ""
    for carattere in stringa:
        if carattere not in consonanti:
            nuova_stringa += carattere
    return nuova_stringa
print(stringa_no_consonanti("Armando"))

#scrivere una funzione che converta un numero intero in una stringa
def int_stringa(numero):
    numeroString = str(numero)
    return numeroString, type(numeroString)
print(int_stringa(3))

#scrivere una funzione che accetti una stringa in minuscolo e restituisca la stringa in maiuscolo
def maiuscolo(stringa):
    stringa2 = stringa.upper()
    return stringa2
print(maiuscolo("ciAo"))
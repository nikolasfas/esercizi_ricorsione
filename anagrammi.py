import copy
from functools import lru_cache


def anagrammi (parola):
    soluzioni = []
    ricorsione([], parola, soluzioni)
    return soluzioni


def ricorsione(parziale: list, rimanenti: str, soluzioni: list):
    # Caso Terminale
    if len(rimanenti) == 0:
        soluzioni.append(copy.deepcopy(parziale))
    # Caso Ricorsivo
    else:
        for i in range(len(rimanenti)): # DOG
            parziale.append(rimanenti[i]) # O
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i+1:] # OG
            ricorsione(parziale, nuovi_rimanenti, soluzioni)
            parziale.pop()


if __name__ == '__main__':
    print(anagrammi("casa"))

# =====================================================================================

def anagrammi_str (parola):
    soluzioni = set()
    ricorsione_str("", parola, soluzioni)
    return soluzioni

def ricorsione_str(parziale: str, rimanenti: str, soluzioni: list):
    # Caso Terminale
    if len(rimanenti) == 0:
        soluzioni.add(copy.deepcopy(parziale))
    # Caso Ricorsivo
    else:
        for i in range(len(rimanenti)):
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i+1:]
            ricorsione_str(parziale+rimanenti[i], nuovi_rimanenti, soluzioni)


if __name__ == '__main__':
    print(anagrammi_str("casaaa"))

# =====================================================================================

def anagrammi_str2(parola):
    ricorsione_str2("", parola)


@lru_cache(maxsize=None)
def ricorsione_str2(parziale: str, rimanenti: str):
    # Caso Terminale
    if len(rimanenti) == 0:
        print(parziale)
    # Caso Ricorsivo
    else:
        for i in range(len(rimanenti)):
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i+1:]
            ricorsione_str2(parziale+rimanenti[i], nuovi_rimanenti)


if __name__ == '__main__':
    anagrammi_str2("casaaa")
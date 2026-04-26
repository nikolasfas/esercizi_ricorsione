import copy
from time import time


class MagicSquare():

    def __init__(self, N):
        self.N = N
        self.n_chiamate = 0
        self.n_soluzioni = 0
        self.soluzioni = []

    # SOLUZIONE DEL QUADRATO MAGICO RAPPRESENTA DA UNA VETTORE DI N**2 ELEMENTI,
    # OGNI ELEMENTO RAPPRESENTA UNA CELLA DEL QUADRATO, ED IL SUO VALORE E' IL NUMERO CHE METTIAMO NELLA CELLA
    def resolve_square(self):
        self.n_chiamate = 0
        self.n_soluzioni = 0
        self.soluzioni = []

        rimanenti = set(range(1, self.N*self.N+1))
        self._ricorsione([], rimanenti)


    def _ricorsione(self, parziale, rimanenti):
        self.n_chiamate += 1
        # CASO TERMINALE
        if len(parziale) == self.N*self.N:
            if self._is_valid(parziale):

                self.n_soluzioni += 1
                self.soluzioni.append(copy.deepcopy(parziale))

        # CASO RICORSIVO
        else:
            for numero in rimanenti:
                # 1. AGGIUNGERE NUMERO A PARZIALE
                parziale.append(numero)
                if self._is_parziale_valid(parziale):
                    # 1b. TOLGO IL NUMERO APPENA INSERITO DAI RIMANENTI
                    nuovi_rimanenti = copy.deepcopy(rimanenti)
                    nuovi_rimanenti.remove(numero)
                    # 2. ANDARE AVANTI NELLA RICORSIONE
                    self._ricorsione(parziale, nuovi_rimanenti)
                # 3. BACKTRACKING
                parziale.pop()


    def _is_parziale_valid(self, parziale):
        numero_magico = self.N*(self.N*self.N+1)/2
        # 1. CONTROLLARE LE RIGHE
        n_righe_completate = len(parziale)//self.N
        for id_riga in range(n_righe_completate):
            riga = parziale[id_riga*self.N:(id_riga+1)*self.N]
            if sum(riga) != numero_magico:
                return False
        # 2. CONTROLLAR LE COLONNE
        n_colonne_completate = max(len(parziale) - self.N*(self.N-1), 0)
        for id_colonna in range(n_colonne_completate):
            colonna = parziale[id_colonna: (self.N-1)*self.N + id_colonna+1 : self.N]
            if sum(colonna) != numero_magico:
                return False
        # 3. CONTROLLARE DIAGONALE 1
        # diagonale1 = potenziale_soluzione[0: self.N**2 +1 : self.N+1]
        # if sum(diagonale1) != numero_magico:
        #    return False
        # 4. CONTROLLARE DIAGONALE 2
        # somma = 0
        # for indice in range(self.N):
        #    somma += potenziale_soluzione[indice*self.N + (self.N-1 - indice)]
        # if somma != numero_magico:
        #    return False
        # 5. PASSATO TUTTI I CONTROLLI, POSSIAMO PASSARE True
        return True

    def _is_valid(self, potenziale_soluzione):
        numero_magico = self.N*(self.N*self.N+1)/2
        # 1. CONTROLLARE LE RIGHE
        for id_riga in range(self.N):
            riga = potenziale_soluzione[id_riga*self.N:(id_riga+1)*self.N]
            if sum(riga) != numero_magico:
                return False
        # 2. CONTROLLAR LE COLONNE
        for id_colonna in range(self.N):
            colonna = potenziale_soluzione[id_colonna: (self.N-1)*self.N + id_colonna+1 : self.N]
            if sum(colonna) != numero_magico:
                return False
        # 3. CONTROLLARE DIAGONALE 1
        diagonale1 = potenziale_soluzione[0: self.N**2 +1 : self.N+1]
        if sum(diagonale1) != numero_magico:
            return False
        # 4. CONTROLLARE DIAGONALE 2
        somma = 0
        for indice in range(self.N):
            somma += potenziale_soluzione[indice*self.N + (self.N-1 - indice)]
        if somma != numero_magico:
            return False
        # 5. PASSATO TUTTI I CONTROLLI, POSSIAMO PASSARE True
        return True

    def stampa_quadrato(self, soluzione):
        print("----------------")
        for riga in range(self.N):
            print(soluzione[riga * self.N: (riga+1) *self.N])

        print("----------------")

if __name__ == "__main__":
    ms = MagicSquare(3)
    start_time = time()
    ms.resolve_square()
    end_time = time()

    print(f"Elapsed time: {end_time - start_time}")
    print(f"Chiamate effettuate = {ms.n_chiamate}")
    print(f"Soluzioni trovate = {ms.n_soluzioni}")

    for soluzione in ms.soluzioni:
        ms.stampa_quadrato(soluzione)

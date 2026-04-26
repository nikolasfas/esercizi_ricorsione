import copy
from time import time


class NRegine():

    def __init__(self):
        self.n_soluzioni = None
        self.n_chiamate = None
        self.soluzioni = None

    # ===========================APPROCCIO 2==============================
    # SOLUZIONE COME VETTORE DI COPPIE (RIGA, COLONNA)

    def solve2(self, N):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self.soluzioni = []
        self._ricorsione2([], N)

    # parziale E' UN VETTORE DI N ELEMENTI, OGNUNO RAPPRESENTATE
    # UNA REGINA COME RGA E COLONNA
    def  _ricorsione2(self, parziale, N):
        self.n_chiamate += 1
        # CASO TERMINALE: HO MESSO N REGINE
        if len(parziale) == N:

            if self._is_nuova_soluzione(parziale):

                # if self._is_soluzione(parziale):
                self.n_soluzioni += 1
                self.soluzioni.append(copy.deepcopy(parziale))

        # CASO RICORSIVO: HO MESSO < N REGINE
        else:
            for riga in range(N):
                for col in range(N):
                    # VERIFICO SE LA nuova_regina SIA AMMISSIBILE
                    nuova_regina = [riga, col]

                    if self._step_is_valid(nuova_regina, parziale):
                        # AGGIUNGI PEZZO DI SOLUZIONE IN parziale
                        parziale.append(nuova_regina)
                        self._ricorsione2(parziale, N)
                        # FARE BACKTRACKING
                        parziale.pop()

    # CONFRONTIAMO LA SOLUZIONE POTENZIALE CON TUTTE QUELLE GIA' TROVATE
    # SE E' DIVERSA, return True, ALTRIMENTI return False
    def _is_nuova_soluzione(self, soluzione_potenziale):
        N = len(soluzione_potenziale)
        for soluzione in self.soluzioni:
            counter = 0
            for regina in soluzione_potenziale:
                if regina in soluzione:
                    counter += 1
            if counter == N:
                return False
        return True



    def _step_is_valid(self, nuova_regina, parziale) -> bool:
        for regina in parziale:
            if not self._is_pair_admissible(nuova_regina, regina):
                return False;
        return True;



    def _is_pair_admissible(self, regina1, regina2) -> bool:
        # 1 VERIFICO LA RIGA, SE NON VA BENE, return False
        if regina1[0] == regina2[0]:
            return False;

        # 2 VERIFICO LA COLONNA, SE NON VA BENE, return False
        if regina1[1] == regina2[1]:
            return False;

        # 3 VERIFICO LA DIAGONALE 1, SE NON VA BENE, return False
        # PER FARE LA VERIFICA DEVO CONTROLLARE CHE colonna_regina1 - riga_regina1 == colonna_regiona2 - riga_regina2
        if regina1[0] - regina1[1] == regina2[0] - regina2[1]:
            return False;

        # 4 VERIFICO LA DIAGONALE 2, SE NON VA BENE, return False
        # PER FARE LA VERIFICA DEVO CONTROLLARE CHE colonna_regina1 + riga_regina1 == colonna_regiona2 + riga_regina2
        if regina1[0] + regina1[1] ==  regina2[0] + regina2[1]:
            return False;

        # 5 HO PASSATO TUTTI I CONTROLLI, return True
        return True;


    def _is_soluzione(self, sol_possibile) -> bool:
        for i in range(len(sol_possibile)-1):
            for j in range(i+1, len(sol_possibile)):
                if not self._is_pair_admissible(sol_possibile[i], sol_possibile[j]):
                    return False;
        return True;




if __name__ == '__main__':
    nRegine = NRegine()
    start_time = time()
    nRegine.solve2(4)
    end_time = time()

    print(f"Ho trovato {nRegine.n_soluzioni} soluzioni possibili")
    print(f"Chiamate effettuate {nRegine.n_chiamate} chiamate")
    print(f"Elapsed time = {end_time - start_time}")
    print(nRegine.soluzioni)
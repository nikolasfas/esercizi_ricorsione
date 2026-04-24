from time import time


class NRegine():

    def __init__(self):
        self.n_soluzioni = None
        self.n_chiamate = None

    # ===========================APPROCCIO 2==============================
    # SOLUZIONE COME VETTORE DI COPPIE (RIGA, COLONNA)

    def solve2(self, N):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self._ricorsione2([], N)

    # parziale E' UN VETTORE DI N ELEMENTI, OGNUNO RAPPRESENTATE
    # UNA REGINA COME RGA E COLONNA
    def  _ricorsione2(self, parziale, N):
        self.n_chiamate += 1
        # CASO TERMINALE: HO MESSO N REGINE
        if len(parziale) == N:

            if self._is_soluzione(parziale):

                self.n_soluzioni += 1
                print(parziale)

        # CASO RICORSIVO: HO MESSO < N REGINE
        else:
            for riga in range(N):
                for col in range(N):
                    nuova_regina = [riga, col]
                    # AGGIUNGI PEZZO DI SOLUZIONE IN parziale
                    parziale.append(nuova_regina)
                    self._ricorsione2(parziale, N)
                    # FARE BACKTRACKING
                    parziale.pop()

    def _is_soluzione(self, sol_possibile) -> bool:
        pass




if __name__ == '__main__':
    nRegine = NRegine()
    start_time = time()
    nRegine.solve2(4)
    end_time = time()

    print(f"Ho trovato {nRegine.n_soluzioni} soluzioni possibili")
    print(f"Chiamate effettuate {nRegine.n_chiamate} chiamate")
    print(f"Elapsed time = {end_time - start_time}")
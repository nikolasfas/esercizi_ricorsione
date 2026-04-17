class XExpansion:
    def __init__(self):
        soluzioni = []

    def calcola(self, input):
        self._ricorsione("", input)

    def _ricorsione(self, parziale, rimanenti):
        #caso terminale
        if len(rimanenti) == 0:
            print(parziale)
        #caso ricorsivo
        else:
            if rimanenti[0] == 'X':
                self._ricorsione(parziale + '0', rimanenti[1:])
                self._ricorsione(parziale + '1', rimanenti[1:])
            else:
                self._ricorsione(parziale + rimanenti[0], rimanenti[1:])

if __name__ == '__main__':
    xExpansion = XExpansion()
    sequenza = "01X0X"
    print(xExpansion.calcola(sequenza))
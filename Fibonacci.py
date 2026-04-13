from time import time


class Fibonacci:
    def __init__(self):
        self.cache = {0: 0, 1: 1}


    def calcola_elemento_cache(self, n):
        # se ho già la soluzione per questo n la prendo dalla chache
        if self.cache.get(n) is not None:
            return self.cache[n]
        # altrimenti devo andare avanti con la ricorsione
        else:
            self.cache[n] = (self.calcola_elemento_cache(n-1) + self.calcola_elemento_cache(n-2))
            return self.cache[n]

if __name__ == "__main__":
    N = 40
    start_time = time()
    print(Fibonacci().calcola_elemento_cache(N))
    end_time = time()
    print(f"Elapsed time - recursion: {end_time - start_time}")
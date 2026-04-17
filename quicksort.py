def quicksort(sequenza):
    # caso terminale
    if len(sequenza)<=1:
        return sequenza
    # caso ricorsivo
    else:
        # 1. scelta pivot
        pivot = sequenza[0]
        # 2. dividere sequnza secondo il pivot
        #sequenza_smaller = []
        #sequenza_pivot = []
        #sequenza_larger = []

        #for i in sequenza:
            # il numero è < pivot
        #    if i < pivot:
        #        sequenza_smaller.append(i)
            # il numero è uguale al pivot
        #    elif i == pivot:
        #        sequenza_pivot.append(i)
            # il numero è > pivot
        #    else:
        #        sequenza_larger.append(i)

        sequenza_smaller = [ n for n in sequenza if n > pivot]
        sequenza_pivot = [ n for n in sequenza if n == pivot]
        sequenza_larger = [ n for n in sequenza if n < pivot]

        # 3. la soluzione è data da: ordinare il vettore smaller + vettore = pivot
        # + ordinare il vettore bigger
        return quicksort(sequenza_smaller) + quicksort(sequenza_pivot) + quicksort(sequenza_larger)



if __name__ == "__main__":

    # Definire prima l'input per capire come strutturare fuunzione
    sequenza = [9, 5, 43, 7, 12, 65]
    print(quicksort(sequenza))
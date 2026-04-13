from time import sleep


def countdown(n):
    while n >= 0:
        print(n)
        sleep(2)
        n -= 1

def countdown_recursive(n):
    # Condizione terminale
    if n == 0:
        print("Stop")
    # Condizione iterativa / non terminale
    else:
        print(n)
        sleep(1)
        countdown_recursive(n-1)



if __name__ == '__main__':
    N = 5
    countdown_recursive(N)

def palyndrome(word):
    #terminale
    if len(word) <= 1:
        return True
    else:
        return (word[0] == word[-1] and
                palyndrome(word[1:-1]))

if __name__ == "__main__":
    print(palyndrome("casa"))


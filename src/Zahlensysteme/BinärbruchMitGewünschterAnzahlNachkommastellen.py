
def binarbruch2(dezimalzahl, AnzahlNachkommaStellen):

    ganzzahliger_teil = int(dezimalzahl)
    bruchteil = dezimalzahl - ganzzahliger_teil

    bin_ganzzahliger_teil = bin(ganzzahliger_teil)[2:]

    bin_bruchteil = '.'
    for i in range(AnzahlNachkommaStellen):
        bruchteil *= 2
        if bruchteil >= 1:
            bin_bruchteil += '1'
            bruchteil -= 1
        else:
            bin_bruchteil += '0'

    return bin_ganzzahliger_teil + bin_bruchteil


print(binarbruch2(0.1, 13))
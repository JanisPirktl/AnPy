def binarbruch(dezimalzahl):

    ganzzahliger_teil = int(dezimalzahl)
    bruchteil = dezimalzahl - ganzzahliger_teil

    bin_ganzzahliger_teil = bin(ganzzahliger_teil)[2:]

    bin_bruchteil = '.'
    while bruchteil > 0:
        bruchteil *= 2
        if bruchteil >= 1:
            bin_bruchteil += '1'
            bruchteil -= 1
        else:
            bin_bruchteil += '0'
        if len(bin_bruchteil) > 1000:
            break
    return bin_ganzzahliger_teil + bin_bruchteil


print(binarbruch(0.1))

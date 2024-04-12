def dezimal_zu_zweierkomplement(zahl, bit_stellen):
    mask = 2 ** bit_stellen - 1

    if zahl >= 0:
        return format(zahl, '0{}b'.format(bit_stellen))
    else:
        zweierkomplement = (abs(zahl) ^ mask) + 1
        return format(zweierkomplement, '0{}b'.format(bit_stellen))


print(dezimal_zu_zweierkomplement(-99, 8))

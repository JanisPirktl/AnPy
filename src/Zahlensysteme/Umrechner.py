def umrechnen(zahl, eingabe_basis, ziel_basis):

    dezimalzahl = int(str(zahl), eingabe_basis)

    if ziel_basis == 10:
        print(f"{dezimalzahl} (Basis {ziel_basis})")
    else:
        alphabet = "0123456789ABCDEF"
        umgerechnete_zahl = ""
        while dezimalzahl > 0:
            umgerechnete_zahl = alphabet[dezimalzahl % ziel_basis] + umgerechnete_zahl
            dezimalzahl //= ziel_basis
        print(f"{umgerechnete_zahl} (Basis {ziel_basis})")


umrechnen(99, 10, 2)




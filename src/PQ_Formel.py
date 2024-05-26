import math

def berechne_nullstellen(a, b, c):
    # Stellen Sie sicher, dass a nicht 0 ist, da es keine quadratische Gleichung mehr wäre
    if a == 0:
        raise ValueError("Der Koeffizient 'a' darf nicht 0 sein.")

    # Berechnung der p- und q-Werte
    p = b / a
    q = c / a

    # Berechnung der Diskriminante
    diskriminante = (p / 2) ** 2 - q

    # Überprüfung der Diskriminante
    if diskriminante < 0:
        return "Die Gleichung hat keine reellen Nullstellen."
    elif diskriminante == 0:
        x1 = -p / 2
        return f"Die Gleichung hat eine doppelte Nullstelle: x = {x1}"
    else:
        x1 = -p / 2 + math.sqrt(diskriminante)
        x2 = -p / 2 - math.sqrt(diskriminante)
        return f"Die Nullstellen der Gleichung sind: x1 = {x1}, x2 = {x2}"


# Beispielaufruf
a = 1
b = -12
c = 11
nullstellen = berechne_nullstellen(a, b, c)
print(nullstellen)

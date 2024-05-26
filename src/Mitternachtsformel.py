import math

def berechne_nullstellen(a, b, c):
    # Stellen Sie sicher, dass a nicht 0 ist, da es keine quadratische Gleichung mehr wäre
    if a == 0:
        raise ValueError("Der Koeffizient 'a' darf nicht 0 sein.")

    # Berechnung der Diskriminante
    diskriminante = b ** 2 - 4 * a * c

    # Überprüfung der Diskriminante
    if diskriminante < 0:
        return "Die Gleichung hat keine reellen Nullstellen."
    elif diskriminante == 0:
        x = -b / (2 * a)
        return f"Die Gleichung hat eine doppelte Nullstelle: x = {x}"
    else:
        x1 = (-b + math.sqrt(diskriminante)) / (2 * a)
        x2 = (-b - math.sqrt(diskriminante)) / (2 * a)
        return f"Die Nullstellen der Gleichung sind: x1 = {x1}, x2 = {x2}"

# Beispielaufruf
a = 3
b = 9
c = 6
nullstellen = berechne_nullstellen(a, b, c)
print(nullstellen)

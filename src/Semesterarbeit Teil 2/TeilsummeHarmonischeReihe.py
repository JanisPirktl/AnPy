
def berechne_harmonische_teilsumme(n):
    teilsumme = 0
    for k in range(1, n + 1):
        teilsumme += 1 / k
    return teilsumme

print(berechne_harmonische_teilsumme(5))
print(berechne_harmonische_teilsumme(50))
print(berechne_harmonische_teilsumme(500))
print(berechne_harmonische_teilsumme(5000))
print(berechne_harmonische_teilsumme(50000))

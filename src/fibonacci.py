import time
import math


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fib_calls(n, counter=[0]):
    counter[0] += 1  # Zählt den aktuellen Aufruf
    if n <= 1:
        return n
    else:
        return fib_calls(n - 1, counter) + fib_calls(n - 2, counter)


print("Herkömmliche rekursive Funktion")
for i in range(31):
    counter = [0]  # Initialisiert den Zähler für jeden Funktionsaufruf
    start_time = time.perf_counter_ns()
    fib_calls(i, counter)  # Berechnet die i-te Fibonacci-Zahl und zählt die Aufrufe
    end_time = time.perf_counter_ns()
    duration = end_time - start_time
    print(
        f"Die {i}.te Fibonacci-Zahl ist: {fib(i)}; Anzahl der Aufrufe: {counter[0]}; Dafür wurden {duration} Nanosekunden gebraucht")

print()
print("Mittels dynamischer Programmierung")


def fib_dynamic(n, counter=[0]):
    counter[0] += 1  # Zählt den aktuellen Aufruf
    if n <= 1:
        return n
    fib_numbers = [0, 1] + [0] * (
                n - 1)  # Initialisiert ein Array mit den ersten zwei Fibonacci-Zahlen und setzt den Rest auf 0
    for i in range(2, n + 1):
        fib_numbers[i] = fib_numbers[i - 1] + fib_numbers[i - 2]
    return fib_numbers[n]


for i in range(31):
    counter = [0]  # Initialisiert den Zähler für jeden Funktionsaufruf
    total_time = 0
    start_time = time.perf_counter_ns()
    fib_dynamic(i, counter)  # Berechnet die i-te Fibonacci-Zahl und zählt die Aufrufe
    end_time = time.perf_counter_ns()
    duration = end_time - start_time
    total_time = total_time + duration
    print(
        f"Die {i}.te Fibonacci-Zahl ist: {fib(i)}; Anzahl der Aufrufe: {counter[0]}; Dafür wurden {duration} Nanosekunden gebraucht")
average_time = total_time / 30
print(f"Durchschnittliche Zeit der Berechnung: {average_time} Nanosekunden")
print()
print("Mittels Binets Formel")


def fib_binet(n, counter=[0]):
    counter[0] += 1  # Zählt den aktuellen Aufruf
    golden_ratio = (1 + math.sqrt(5)) / 2
    return round((golden_ratio ** n - (1 - golden_ratio) ** n) / math.sqrt(5))


for i in range(31):
    counter = [0]  # Initialisiert den Zähler für jeden Funktionsaufruf
    total_time = 0
    start_time = time.perf_counter_ns()
    fib_binet(i, counter)  # Berechnet die i-te Fibonacci-Zahl und zählt die Aufrufe
    end_time = time.perf_counter_ns()
    duration = end_time - start_time
    total_time = total_time + duration
    print(
        f"Die {i}.te Fibonacci-Zahl ist: {fib(i)}; Anzahl der Aufrufe: {counter[0]}; Dafür wurden {duration} Nanosekunden gebraucht")
average_time = total_time / 30
print(f"Durchschnittliche Zeit der Berechnung: {average_time} Nanosekunden")

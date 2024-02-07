import time
import math

number_of_calls = 31


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fib_calls(n, counter):
    counter[0] += 1 #zählt den aktuellen Aufruf
    if n <= 1:
        return n, counter
    else:
        return fib_calls(n - 1, counter) + fib_calls(n - 2, counter)


print("Mittels rekursiver Funktion:")
for i in range(number_of_calls):
    counter = fib_calls(i, [0])[1][0]
    start_time = time.perf_counter_ns()
    fib_n = fib(i)
    end_time = time.perf_counter_ns()
    duration = end_time - start_time
    print(
        f"Die {i}.te Fibonacci-Zahl ist: {fib_n}; Anzahl der Aufrufe: {counter}; Dafür wurden {duration} Nanosekunden gebraucht")
print()






def fib_dynamic(n):
    if n <= 1:
        return n
    fib_numbers = [0, 1] + [0] * (
            n - 1)  # Initialisiert ein Array mit den ersten zwei Fibonacci-Zahlen und setzt den Rest auf 0
    for i in range(2, n + 1):
        fib_numbers[i] = fib_numbers[i - 1] + fib_numbers[i - 2]
    return fib_numbers[n]

total_time_dynamic = 0
print("Mittels dynamischer Programmierung")
for i in range(number_of_calls):
    start_time = time.perf_counter_ns()
    fib_dynamic(i)
    end_time = time.perf_counter_ns()
    duration = end_time - start_time
    total_time_dynamic = total_time_dynamic + duration
    print(
        f"Die {i}.te Fibonacci-Zahl ist: {fib(i)}; Dafür wurden {duration} Nanosekunden gebraucht")


average_time_dynamic = total_time_dynamic / number_of_calls
print(f"Durchschnittliche Zeit der Berechnung: {round(average_time_dynamic)} Nanosekunden")
print()




def fib_binet(n):
    golden_ratio = (1 + math.sqrt(5)) / 2
    return round((golden_ratio ** n - (1 - golden_ratio) ** n) / math.sqrt(5))

total_time_binet = 0
print("Mittels Binets Formel")
for i in range(number_of_calls):
    start_time = time.perf_counter_ns()
    fib_binet(i)
    end_time = time.perf_counter_ns()
    duration = end_time - start_time
    total_time_binet = total_time_binet + duration
    print(
        f"Die {i}.te Fibonacci-Zahl ist: {fib(i)}; Dafür wurden {duration} Nanosekunden gebraucht")
average_time_binet = total_time_binet / number_of_calls
print(f"Durchschnittliche Zeit der Berechnung: {round(average_time_binet)} Nanosekunden")


binet_was_faster = 0
dynamic_was_faster = 0
for i in range(200):
    total_time_binet = 0
    for i in range(number_of_calls):
        start_time = time.perf_counter_ns()
        fib_binet(i)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        total_time_binet = total_time_binet + duration
    average_time_binet = total_time_binet / number_of_calls
    print(f"binet {average_time_binet}")

    total_time_dynamic = 0
    for i in range(number_of_calls):
        start_time = time.perf_counter_ns()
        fib_dynamic(i)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        total_time_dynamic = total_time_dynamic + duration
    average_time_dynamic = total_time_dynamic / number_of_calls
    print(f"dynamic {average_time_dynamic}")

    if average_time_dynamic > average_time_binet:
        binet_was_faster += 1
    if average_time_binet > average_time_dynamic:
        dynamic_was_faster += 1
print()
print(f"Binet was faster {binet_was_faster} times")
print(f"Dynamic was faster {dynamic_was_faster} times")
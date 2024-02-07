import time
import math

#wird benutzt, um die 30 ersten Fibonacci-Zahlen zu berechnen
number_of_calls = 31



#rekursive Funktion um die n-te Fibonacci-Zahl zu berechnen
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


#Funktion um die Funktionsaufrufe der rekursiven Funktion zu zählen
def fib_calls(n, counter):
    counter[0] += 1 #zählt den aktuellen Aufruf
    if n <= 1:
        return n, counter
    else:
        return fib_calls(n - 1, counter) + fib_calls(n - 2, counter)


#Funktion um die n-te Fibonacci-Zahl dynamisch zu berechnen
def fib_dynamic(n):
    if n <= 1:
        return n
    fib_numbers = [0, 1] + [0] * (n - 1)  # Initialisiert ein Array mit den ersten zwei Fibonacci-Zahlen und setzt den Rest auf 0
    for i in range(2, n + 1):
        fib_numbers[i] = fib_numbers[i - 1] + fib_numbers[i - 2]
    return fib_numbers[n]


#Funktion um die n-te Fibonacci-Zahl mit Binets Formel zu berechnen
def fib_binet(n):
    golden_ratio = (1 + math.sqrt(5)) / 2
    return round((golden_ratio ** n - (1 - golden_ratio) ** n) / math.sqrt(5))


#Berechnet die ersten 30 Fibonacci-Zahlen mit der rekursiven Funktion
#Gibt zusätzlich die jeweilige Anzahl Aufrufe der rekursiven Funktion und die benötigte Zeit aus
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






#Berechnet die ersten 30 Fibonacci-Zahlen mit der dynamischen Funktion
#Gibt zusätzlich die benötigte Zeit aus
total_time_dynamic = 0
print("Mittels dynamischer Programmierung")
for i in range(number_of_calls):
    start_time = time.perf_counter_ns()
    fib_dynamic(i)
    end_time = time.perf_counter_ns()
    duration = end_time - start_time
    total_time_dynamic += duration
    print(
        f"Die {i}.te Fibonacci-Zahl ist: {fib(i)}; Dafür wurden {duration} Nanosekunden gebraucht")

#Berechnet die durschnittlich benötigte Zeit und gibt sie aus
average_time_dynamic = total_time_dynamic / number_of_calls
print(f"Durchschnittliche Zeit der Berechnung: {round(average_time_dynamic)} Nanosekunden")
print()





#Berechnet die ersten 30 Fibonacci-Zahlen mit der Formel von Binet
#Gibt zusätzlich die benötigte Zeit aus
total_time_binet = 0
print("Mittels Binets Formel")
for i in range(number_of_calls):
    start_time = time.perf_counter_ns()
    fib_binet(i)
    end_time = time.perf_counter_ns()
    duration = end_time - start_time
    total_time_binet += duration
    print(
        f"Die {i}.te Fibonacci-Zahl ist: {fib(i)}; Dafür wurden {duration} Nanosekunden gebraucht")

#Berechnet die durchschnittlich benötigte Zeit und gibt sie aus
average_time_binet = total_time_binet / number_of_calls
print(f"Durchschnittliche Zeit der Berechnung: {round(average_time_binet)} Nanosekunden")
print()







#Berechnet 200 mal die ersten 30 Fibonacci-Zahlen mit der dynamischen Formel und Binets Formel
#Berechnet die durchschnittlich benötigte Zeit

gruendlich_testen = 200

total_time_binet = 0
total_time_dynamic = 0

for i in range(gruendlich_testen):

    for i in range(number_of_calls):
        start_time = time.perf_counter_ns()
        fib_binet(i)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        total_time_binet += duration

    for i in range(number_of_calls):
        start_time = time.perf_counter_ns()
        fib_dynamic(i)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        total_time_dynamic += duration

total_number_of_calls = gruendlich_testen*number_of_calls

average_time_dynamic = total_time_dynamic / (total_number_of_calls)
average_time_binet = total_time_binet / (total_number_of_calls)

print(f"Dynamische Funktion benötigte durschnittlich {round(average_time_dynamic)} Nanosekunden für {total_number_of_calls} Aufrufe")
print(f"Funktion mit Binets Formel benötigte durschnittlich {round(average_time_binet)} Nanosekundenfür für {total_number_of_calls} Aufrufe")

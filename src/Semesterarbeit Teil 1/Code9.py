import decimal
import time
import matplotlib.pyplot as plt

# THIS CLASS TAKES SEVERAL MINUTES TO RUN!!!
number_of_calls = 10001
# YOU CAN DECREASE THE NUMBER OF CALLS HERE IF YOU WANT


def set_precision(precision):
    decimal.getcontext().prec = precision
    five = decimal.Decimal(5)
    return five.sqrt()


def fib_binet_precision(n, sqrt_of_5):
    golden_ratio = (1 + sqrt_of_5) / 2
    return round((golden_ratio ** n - (1 - golden_ratio) ** n) / sqrt_of_5)


def fib_iterative_replace(n):
    if n <= 1:
        return n
    fib_numbers = [0, 1]
    for i in range(1, n):
        current = fib_numbers[0]
        fib_numbers[0] = fib_numbers[1]
        fib_numbers[1] = current + fib_numbers[0]
    return fib_numbers[1]


x_values = []
y_values_optimal_precision = []
y_values_high_precision = []


def code9():
    print(f"Calculate {number_of_calls-1} fibonacci-numbers with binets formula and compare the difference for same"
          f" precision and optimal precision")

    for i in range(4, number_of_calls):
        x_values.append(i)

        sqrt_of_5 = set_precision(round(i/4))
        start_time = time.perf_counter_ns()
        fib_result_binet = fib_binet_precision(i, sqrt_of_5)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        y_values_optimal_precision.append(duration)
        fib_result_replace = fib_iterative_replace(i)
        if fib_result_binet != fib_result_replace:
            print(f"RESULTS DO NOT MATCH AT {i}-th NUMBER!")

        sqrt_of_5 = set_precision(round(number_of_calls/4))
        start_time = time.perf_counter_ns()
        fib_result_binet = fib_binet_precision(i, sqrt_of_5)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        y_values_high_precision.append(duration)
        fib_result_replace = fib_iterative_replace(i)
        if fib_result_binet != fib_result_replace:
            print(f"RESULTS DO NOT MATCH AT {i}-th NUMBER!")

    plt.xlabel("n-th Fibonacci Number")
    plt.ylabel("Time needed in Nanoseconds")

    plt.plot(x_values, y_values_high_precision, label='Same Precision for every number', color='blue')
    plt.plot(x_values, y_values_optimal_precision, label='Optimal Precision for every number', color='red')

    plt.legend()
    plt.show()

code9()

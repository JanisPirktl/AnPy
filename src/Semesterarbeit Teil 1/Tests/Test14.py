import Functions as F
import time
import matplotlib.pyplot as plt

number_of_calls = 1001
x_values = []
y_values_replace = []
y_values_binet = []

def test14():
    print(
        f"Measure and compare the average time needed to calculate the {number_of_calls-1}-th fibonacci-number with iterative function and binet's function")


    total_time_replace = 0
    total_time_binet = 0

    sqrt_of_5 = F.set_precision(212)

    for i in range(100):

        x_values.append(i)

        start_time = time.perf_counter_ns()
        fib_result = F.fib_iterative_replace(number_of_calls)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        print(f"REPLACE - {number_of_calls}.te Fibonacci-Number: {fib_result}; Time needed: {duration}")
        y_values_replace.append(duration)
        total_time_replace += duration

        start_time = time.perf_counter_ns()
        fib_result = F.fib_binet_precision(number_of_calls, sqrt_of_5)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        print(f"BINET - {number_of_calls}.te Fibonacci-Number: {fib_result}; Time needed: {duration}")
        y_values_binet.append(duration)
        total_time_binet += duration

    average_time_buffered = total_time_binet / 100
    print(f"Average time needed BINET: {round(average_time_buffered)} in nanoseconds")
    average_time_replace = total_time_replace / 100
    print(f"Average time needed REPLACE: {round(average_time_replace)} in nanoseconds")

    plt.xlabel("Number of Tries")
    plt.ylabel("Time needed in Nanoseconds")

    plt.plot(x_values, y_values_binet, label='Binet-Function', color='red')
    plt.plot(x_values, y_values_replace, label='Replace-Function', color='green')

    plt.legend()
    plt.show()


test14()

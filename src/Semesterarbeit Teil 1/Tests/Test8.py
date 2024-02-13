import Functions as F
import time
import matplotlib.pyplot as plt

number_of_calls = 20001
x_values = []
y_values_replace = []
y_values_buffered = []

def test8():
    print(
        f"Measure and compare the average time needed to calculate the {number_of_calls-1}-th fibonacci-number with iterative functions")


    total_time_replace = 0
    total_time_buffered = 0

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
        fib_result = F.fib_iterative_buffered_non_global_buffer(number_of_calls)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        print(f"BUFFERED - {number_of_calls}.te Fibonacci-Number: {fib_result}; Time needed: {duration}")
        y_values_buffered.append(duration)
        total_time_buffered += duration

    average_time_buffered = total_time_buffered / 100
    print(f"Average time needed BUFFERED: {round(average_time_buffered)} in nanoseconds")
    average_time_replace = total_time_replace / 100
    print(f"Average time needed REPLACE: {round(average_time_replace)} in nanoseconds")

    plt.xlabel("Number of Tries")
    plt.ylabel("Time needed in Nanoseconds")

    plt.plot(x_values, y_values_buffered, label='Buffered-Function', color='red')
    plt.plot(x_values, y_values_replace, label='Replace-Function', color='green')

    plt.legend()
    plt.show()


test8()

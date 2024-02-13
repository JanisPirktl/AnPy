import Functions as F
import matplotlib.pyplot as plt
import time

number_of_calls = 999
x_values = []
y_values = []
buffer = []



def test5():
    print(
        f"Measure the average time needed to calculate the 999-th fibonacci-number with buffered recursive function")

    F.instantiate_buffer(number_of_calls)
    total_time = 0

    for i in range(100):
        F.instantiate_buffer(number_of_calls)
        start_time = time.perf_counter_ns()
        fib_result = F.buffered_fib(number_of_calls)
        end_time = time.perf_counter_ns()
        duration = end_time - start_time
        print(f"{number_of_calls}.te Fibonacci-Number: {fib_result}; Time needed: {duration}")
        x_values.append(i)
        y_values.append(duration)
        total_time += duration

    average_time = total_time / 100
    print(f"Average time needed: {round(average_time)} in nanoseconds")

    plt.xlabel("Number of tries")
    plt.ylabel("Time needed in Nanoseconds")

    plt.plot(x_values, y_values, color='black')
    plt.show()


test5()

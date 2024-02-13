import Functions as F
import time
import matplotlib.pyplot as plt

number_of_calls = 71
x_values = []
y_values_first = []
y_values_second = []


def test12():
    print(f"Calculate the {number_of_calls - 1} first fibonacci-numbers with binet's formula and then again")


    fib_result = F.fib(30)

    for i in range(number_of_calls):
        x_values.append(i)
        start_time = time.perf_counter_ns()
        fib_result = F.fib_binet(i)
        end_time = time.perf_counter_ns()
        duration_binet = end_time - start_time
        y_values_first.append(duration_binet)
        print(
            f"{i}.te Fibonacci-Number:         {fib_result};        Needed time: {duration_binet} nanoseconds;")

    for i in range(number_of_calls):
        start_time = time.perf_counter_ns()
        fib_result = F.fib_binet(i)
        end_time = time.perf_counter_ns()
        duration_binet = end_time - start_time
        y_values_second.append(duration_binet)
        print(
            f"{i}.te Fibonacci-Number:         {fib_result};        Needed time: {duration_binet} nanoseconds;")

    plt.xlabel("n-th Fibonacci Number")
    plt.ylabel("Time needed in Nanoseconds")

    plt.plot(x_values, y_values_first, color='red', label="First Cycle")
    plt.plot(x_values, y_values_second, color='green', label="Second Cycle")

    plt.legend()
    plt.show()


test12()

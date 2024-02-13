import Functions as F
import time
import matplotlib.pyplot as plt

number_of_calls = 71
x_values = []
y_values = []


def test11():
    print("Calculate average time needed with binet's formula if the function is alone in the loop")
    print(
        "Calculate the 30 first fibonacci-numbers with recursive function in advance to guarantee that the variables needed for binet's formula are not in the data-registers or the caches of the cpu")

    for i in range(30):
        fib_result = F.fib(i)


    for i in range(number_of_calls):
        x_values.append(i)
        start_time = time.perf_counter_ns()
        fib_result = F.fib_binet(i)
        end_time = time.perf_counter_ns()
        duration_binet = end_time - start_time
        y_values.append(duration_binet)
        print(
            f"{i}.te Fibonacci-Number:         {fib_result};        Needed time: {duration_binet} nanoseconds;")

    plt.xlabel("n-th Fibonacci Number")
    plt.ylabel("Time needed in Nanoseconds")

    plt.plot(x_values, y_values, color='black')



    plt.show()


test11()
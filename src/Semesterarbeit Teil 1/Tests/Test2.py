import Functions as F
import matplotlib.pyplot as plt

number_of_calls = 31
x_values = []
y_values = []


def test2():
    print(f"Calculate the number of recursive calls required for the n-th fibonacci-number")

    for i in range(number_of_calls):
        fib_result, counter = F.fib_calls(i, [0])
        print(f"{i}.te Fibonacci-Number: {fib_result}; Number of calls: {counter[0]}")
        x_values.append(i)
        y_values.append(counter[0])

    plt.xlabel("n-th Fibonacci Number")
    plt.ylabel("Number of calls")

    plt.plot(x_values, y_values, color='black')
    plt.show()


test2()

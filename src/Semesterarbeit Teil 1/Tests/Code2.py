import matplotlib.pyplot as plt


def fib_calls(n, counter):
    counter += 1
    if n <= 1:
        return n, counter
    else:
        n_1, counter = fib_calls(n-1, counter)
        n_2, counter = fib_calls(n-2, counter)
        return n_1 + n_2, counter


number_of_calls = 31
x_values = []
y_values = []


def test2():
    print(f"Calculate the number of recursive calls required for the n-th fibonacci-number")

    for i in range(number_of_calls):
        fib_result, counter = fib_calls(i, 0)
        print(f"{i}.te Fibonacci-Number: {fib_result}; Number of calls: {counter}")
        x_values.append(i)
        y_values.append(counter)

    plt.xlabel("n-th Fibonacci Number")
    plt.ylabel("Number of calls")

    plt.plot(x_values, y_values, color='black')
    plt.show()


test2()

number_of_calls = 31


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def test1():
    print(f"Calculate the {number_of_calls - 1} first fibonacci-numbers with recursive function")
    for i in range(number_of_calls):
        fib_result = fib(i)
        print(f"{i}.te Fibonacci-Number: {fib_result}")


test1()

import Functions as F

number_of_calls = 31


def test1():
    print(f"Calculate the {number_of_calls - 1} first fibonacci-numbers with recursive function")
    for i in range(number_of_calls):
        fib_result = F.fib(i)
        print(f"{i}.te Fibonacci-Number:    {fib_result}")


test1()

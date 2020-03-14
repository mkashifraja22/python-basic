def list_sum():
    my_list=[1,24,5,6,7,8,9,10]
    print(sum(my_list))
list_sum()


def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==0:
        return 0
    # Second Fibonacci number is 1
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

n=int(input("enter the fib number"))
print(Fibonacci(n))

# imports as needed

from tkinter import N


def fibo_iter(n:int) -> int:
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    
    return b

def fibo_rec(n : int) -> int:
    if n < 2:
        return n

    return fibo_rec(n - 1) + fibo_rec(n - 2)

def main():
    nth_fibo = fibo_iter(10)
    print(nth_fibo)
    nth_fibo = fibo_rec(10)
    print(nth_fibo)

if __name__ == '__main__':
    main()

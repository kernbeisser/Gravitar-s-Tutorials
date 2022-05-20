# imports as needed
"""
move n-1 disc from a to b using c
move 1 disc from a to c
move n-1 disc from b to c using a
"""

# hanoi.py
#    Recursive solution to Towers of Hanoi problem.


def hanoi(n, source, dest, temp):
    if n > 0:
        hanoi(n - 1, source, temp, dest)
        print(f"Move disk {n} from {source} to {dest}")
        hanoi(n - 1, temp, source, dest)


def main():
    hanoi(4, "A", "B", "C")


if __name__ == "__main__":
    main()

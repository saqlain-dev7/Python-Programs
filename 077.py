# Using one recursive function, print increasing then decreasing
def print_up_down(n, current=1):
    if current > n:
        return
    print(current, end=" ")
    print_up_down(n, current + 1)
    print(current, end=" ")

n = int(input("Enter N: "))
print_up_down(n)
print()

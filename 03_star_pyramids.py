n = int(input("Enter number of rows: "))

print("\nPattern 1 (right triangle):")
for i in range(1, n + 1):
    print("*" * i)

print("\nPattern 2 (pyramid):")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

print("\nPattern 3 (inverted):")
for i in range(n, 0, -1):
    print("*" * i)

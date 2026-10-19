n = int(input("Enter limit: "))

cubes = [i**3 for i in range(1, n + 1) if i % 2 == 0]
print("Cubes of even integers up to", n, ":", cubes)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
n = int(input("Enter prefix length to swap: "))

new1 = s2[:n] + s1[n:]
new2 = s1[:n] + s2[n:]

print("After swapping:", new1, new2)

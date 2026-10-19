s = input("Enter the main string: ")
sub = input("Enter the substring: ")

indices = [i for i in range(len(s) - len(sub) + 1) if s[i:i + len(sub)] == sub]

if indices:
    print("Substring found at indices:", indices)
else:
    print("Substring not found")

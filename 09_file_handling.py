# Write
with open("sample.txt", "w") as f:
    f.write("Hello, this is line 1\n")
    f.write("This is line 2\n")

# Append
with open("sample.txt", "a") as f:
    f.write("This is line 3 (appended)\n")

# Read
with open("sample.txt", "r") as f:
    content = f.read()
print("File content:")
print(content)

# Count lines and words
lines = content.splitlines()
print("Total lines:", len(lines))
print("Total words:", len(content.split()))

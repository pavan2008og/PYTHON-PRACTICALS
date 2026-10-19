ch = input("Enter a character: ")[0]

if ch.isalpha():
    if ch.lower() in "aeiou":
        print(ch, "is a vowel")
    else:
        print(ch, "is a consonant")
    print("Case:", "uppercase" if ch.isupper() else "lowercase")
elif ch.isdigit():
    print(ch, "is a digit")
elif ch.isspace():
    print("It is a whitespace")
else:
    print(ch, "is a special character")

# Python Practicals

A collection of 15 beginner-level Python programs covering conditionals, loops, strings, data structures, file handling, OOP and exception handling.

| Field | Details |
|---|---|
| Name | PAVAN MISHRA |
| Roll No. | 26570044 |
| Course | Bsc. HONS. COMPUTER SCIENCE |
| College | RAMANUJAN COLLEGE, UNIVERSITY OF DELHI |

## How to run

Install Python 3, save a program as a `.py` file.

```
python 01_quadratic.py
```

On some systems you may need to use `python3` instead of `python`.

## Contents

1. Quadratic equation
2. Prime numbers
3. Star pyramids
4. Character classification
5. String operations
6. Swap prefixes of two strings
7. Substring indices
8. Cubes of even integers
9. File handling
10. Dictionary of cubes
11. Tuple operations
12. Employee class and object counting
13. Class Point2D
14. Inheritance: class Point3D
15. Exception handling for a name

---

## Practical 01 - Roots of a Quadratic Equation

**File:** `01_quadratic.py`

**Aim:** Find the roots of a quadratic equation ax² + bx + c = 0.

**Logic:** Calculate the discriminant `d = b² - 4ac`. If `d > 0` the roots are real and distinct, if `d == 0` they are real and equal, and if `d < 0` they are complex. If `a == 0`, the equation is not quadratic.

**Sample output:**
```
Enter a: 1
Enter b: -3
Enter c: 2
Real & distinct roots: 2.0 1.0
```

---

## Practical 02 - Prime Numbers

**File:** `02_prime_numbers.py`

**Aim:** Check whether a number is prime and list all primes up to it.

**Logic:** A number is prime if it has no divisor between 2 and its square root. A function `is_prime()` checks this, and a list comprehension collects all primes up to n.

**Sample output:**
```
Enter a number: 20
20 is not prime
Primes up to 20 : [2, 3, 5, 7, 11, 13, 17, 19]
```

---

## Practical 03 - Star Pyramids

**File:** `03_star_pyramids.py`

**Aim:** Print star patterns using nested loops.

**Logic:** Each row `i` prints stars using string repetition (`"*" * i`). Spaces before the stars (`" " * (n - i)`) centre the pyramid. Counting down in the loop gives the inverted pattern.

**Sample output:**
```
Enter number of rows: 4

Pattern 1 (right triangle):
*
**
***
****

Pattern 2 (pyramid):
   * 
  * * 
 * * * 
* * * * 

Pattern 3 (inverted):
****
***
**
*
```

---

## Practical 04 - Character Classification

**File:** `04_character_classification.py`

**Aim:** Classify a character as vowel, consonant, digit, whitespace or special character.

**Logic:** Uses string methods `isalpha()`, `isdigit()`, `isspace()`, `isupper()` along with an `if-elif-else` chain. For letters, the lowercase form is checked against `"aeiou"`.

**Sample output:**
```
Enter a character: a
a is a vowel
Case: lowercase
```

---

## Practical 05 - String Operations

**File:** `05_string_operations.py`

**Aim:** Perform common operations on a string.

**Logic:** Uses `len()`, `upper()`, `lower()`, `title()`, slicing `[::-1]` for reversing, a generator expression to count vowels, `split()` to count words, and compares the string with its reverse to check for a palindrome.

**Sample output:**
```
Enter a string: madam
Length: 5
Uppercase: MADAM
Lowercase: madam
Title case: Madam
Reversed: madam
Vowel count: 2
Word count: 1
Palindrome: Yes
```

---

## Practical 06 - Swap Prefixes of Two Strings

**File:** `06_swap_prefixes.py`

**Aim:** Swap the first n characters of two strings.

**Logic:** Slicing is used: `s2[:n] + s1[n:]` gives the first string's new value, and `s1[:n] + s2[n:]` gives the second's.

**Sample output:**
```
Enter first string: hello
Enter second string: world
Enter prefix length to swap: 2
After swapping: wollo herld
```

---

## Practical 07 - Substring Indices

**File:** `07_substring_indices.py`

**Aim:** Find all starting positions of a substring in a string.

**Logic:** Slide a window of the substring's length over the main string. Wherever the slice equals the substring, that index is stored in a list.

**Sample output:**
```
Enter the main string: banana
Enter the substring: ana
Substring found at indices: [1, 3]
```

---

## Practical 08 - Cubes of Even Integers

**File:** `08_cubes_of_even.py`

**Aim:** Print the cubes of all even integers up to a given limit.

**Logic:** A list comprehension loops from 1 to n, keeps numbers where `i % 2 == 0`, and stores `i**3`.

**Sample output:**
```
Enter limit: 10
Cubes of even integers up to 10 : [8, 64, 216, 512, 1000]
```

---

## Practical 09 - File Handling

**File:** `09_file_handling.py`

**Aim:** Write, append and read a text file.

**Logic:** `open()` is used with modes `"w"` (write), `"a"` (append) and `"r"` (read) inside `with` blocks, which close the file automatically. Lines and words are then counted.

**Sample output:**
```
File content:
Hello, this is line 1
This is line 2
This is line 3 (appended)

Total lines: 3
Total words: 14
```

---

## Practical 10 - Dictionary of Cubes

**File:** `10_dictionary_of_cubes.py`

**Aim:** Create a dictionary with numbers as keys and their cubes as values.

**Logic:** A dictionary comprehension `{i: i**3 for i in range(1, n + 1)}`.

**Sample output:**
```
Enter n: 5
Dictionary of cubes: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
```

---

## Practical 11 - Tuple Operations

**File:** `11_tuple_operations.py`

**Aim:** Demonstrate common tuple operations.

**Logic:** Tuples are immutable, so operations return new values. Covers `len`, `max`, `min`, `count`, `index`, concatenation (`+`), repetition (`*`), slicing and sorting.

**Sample output:**
```
Tuple 1: (10, 20, 30, 40, 20)
Length: 5
Max: 40 | Min: 10
Count of 20: 2
Index of 30: 2
Concatenation: (10, 20, 30, 40, 20, 50, 60)
Repetition: (50, 60, 50, 60)
Slicing t1[1:4]: (20, 30, 40)
Reversed: (20, 40, 30, 20, 10)
Sorted: (10, 20, 20, 30, 40)
```

---

## Practical 12 - Employee Class and Object Counting

**File:** `12_employee_class.py`

**Aim:** Create an `Employee` class and count the objects created.

**Logic:** `count` is a class variable shared by all objects. The constructor `__init__` increases it every time a new object is made.

**Sample output:**
```
Name: Amit | Salary: 50000
Name: Riya | Salary: 60000
Name: Karan | Salary: 55000
Total employees: 3
```

---

## Practical 13 - Class Point2D

**File:** `13_point2d.py`

**Aim:** Create a class for a point in 2D space.

**Logic:** The class stores `x` and `y`, and has methods to display the point, find the distance to another point, and find the distance from the origin using the formula `sqrt((x1-x2)² + (y1-y2)²)`.

**Sample output:**
```
Point(1, 2)
Point(4, 6)
Distance between points: 5.0
Distance of p2 from origin: 7.211102550927978
```

---

## Practical 14 - Inheritance: Class Point3D

**File:** `14_point3d_inheritance.py`

**Aim:** Extend `Point2D` to create `Point3D` using inheritance.

**Logic:** `Point3D(Point2D)` inherits `x` and `y`, adds `z`, calls the parent constructor with `super().__init__()`, and overrides `display()` and the distance calculation for 3 dimensions.

**Sample output:**
```
Point(1, 2, 3)
Point(4, 6, 8)
3D distance: 7.0710678118654755
```

---

## Practical 15 - Exception Handling for a Name

**File:** `15_exception_name.py`

**Aim:** Validate a name using exception handling.

**Logic:** A custom exception `InvalidNameError` is raised if the name is empty or contains non-alphabet characters. `try-except-finally` handles the error and `finally` always runs.

**Sample output:**
```
Enter your name: Rahul
Valid name: Rahul
Program finished
```

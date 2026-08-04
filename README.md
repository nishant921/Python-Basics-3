# Python-Basics-3

# Session 3: Break, Continue, Pass & Strings in Python

## Overview

This session focuses on controlling loops using `break`, `continue`, and `pass`, along with understanding and working with **Strings in Python**.

## Topics Covered

### 1. Break Statement

The `break` statement is used to **immediately stop a loop**.

### Example

```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)
```

**Output:**

```text
1
2
3
4
```

---

### 2. Continue Statement

The `continue` statement is used to **skip the current iteration** and move to the next iteration of the loop.

### Example

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

**Output:**

```text
1
2
4
5
```

---

### 3. Pass Statement

The `pass` statement is a **placeholder** that does nothing when executed.

It is useful when a statement is required syntactically, but you don't want to write the actual code yet.

### Example

```python
for i in range(5):
    if i == 2:
        pass
    print(i)
```

---

## Break vs Continue vs Pass

| Statement  | Purpose                             |
| ---------- | ----------------------------------- |
| `break`    | Completely stops the loop           |
| `continue` | Skips the current iteration         |
| `pass`     | Does nothing; acts as a placeholder |

---

# 4. Python Strings

A **string** is a sequence of characters enclosed inside single quotes, double quotes, or triple quotes.

### Examples

```python
name = "Nishant"
course = 'Python'
message = """This is a
multi-line string."""
```

---

## String Indexing

Each character in a string has an index.

```python
text = "Python"

print(text[0])
print(text[2])
print(text[-1])
```

**Output:**

```text
P
t
n
```

### Index Positions

```text
 P  y  t  h  o  n
 0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
```

---

## String Slicing

Slicing is used to extract a portion of a string.

### Syntax

```python
string[start:stop:step]
```

### Example

```python
text = "Python Programming"

print(text[0:6])
print(text[:6])
print(text[7:])
print(text[::-1])
```

---

## String Operations

### Concatenation

Joining two or more strings using `+`.

```python
first = "Python"
second = "Programming"

result = first + " " + second
print(result)
```

### Repetition

Using `*` to repeat a string.

```python
print("Python " * 3)
```

---

## Important String Functions & Methods

Some commonly used string methods include:

* `len()`
* `lower()`
* `upper()`
* `title()`
* `capitalize()`
* `strip()`
* `replace()`
* `split()`
* `join()`
* `find()`
* `count()`
* `startswith()`
* `endswith()`

### Example

```python
text = "python programming"

print(text.upper())
print(text.title())
print(text.count("p"))
print(text.replace("python", "Java"))
```

---

# Practice Tasks

1. Print numbers from 1 to 20 but stop when the number reaches 10 using `break`.
2. Print numbers from 1 to 20 while skipping even numbers using `continue`.
3. Use `pass` inside an `if` statement.
4. Reverse a string using slicing.
5. Count the number of vowels in a string.
6. Check whether a string is a palindrome.
7. Count the occurrence of a particular character.
8. Find the length of a string without directly using `len()`.
9. Remove spaces from a string.
10. Check whether a string starts or ends with a particular character or word.

---

# Key Takeaways

* `break` completely terminates a loop.
* `continue` skips the current iteration.
* `pass` is used as a placeholder.
* Strings are sequences of characters.
* Strings support indexing and slicing.
* Python provides many built-in string methods for text manipulation.
* String operations are important for processing and analyzing text.

---

## Session 3 Summary

**Topics:**

* Break Statement
* Continue Statement
* Pass Statement
* String Basics
* String Indexing
* String Slicing
* String Operations
* String Methods
* String Practice Problems

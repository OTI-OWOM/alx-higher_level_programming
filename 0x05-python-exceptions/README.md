# 0x05. Python Error/Exception Handling 

This repository contains several Python functions that demonstrate the usage of error handling using `try` / `except` blocks. Each function is designed to perform specific tasks and handle errors gracefully, ensuring the program continues execution without crashing. Below is a breakdown of each task and its corresponding functionality.

---

## 0. **safe_print_list.py**
**Function:** `def safe_print_list(my_list=[], x=0):`
- **Description:** Prints up to `x` elements from a given list.
- **Key Features:**
  - Uses a `try` block to handle potential errors if `x` exceeds the list length.
  - Returns the actual number of elements printed.

---

## 1. **safe_print_integer.py**
**Function:** `def safe_print_integer(value):`
- **Description:** Safely prints an integer if the provided value is an integer.
- **Key Features:**
  - Uses `"{:d}".format()` to print integers.
  - Returns `True` if the value is an integer, otherwise returns `False`.

---

## 2. **safe_print_list_integers.py**
**Function:** `def safe_print_list_integers(my_list=[], x=0):`
- **Description:** Prints the first `x` elements of a list, but only the integers.
- **Key Features:**
  - Skips non-integer elements silently.
  - Uses `try` / `except` to handle errors when accessing the list.
  - Returns the number of integers printed.

---

## 3. **safe_print_division.py**
**Function:** `def safe_print_division(a, b):`
- **Description:** Divides two integers and prints the result.
- **Key Features:**
  - Handles division errors such as `ZeroDivisionError`.
  - Uses a `finally` block to print the result, preceded by "Inside result:".

---

## 4. **list_division.py**
**Function:** `def list_division(my_list_1, my_list_2, list_length):`
- **Description:** Divides elements from two lists element by element.
- **Key Features:**
  - If division is not possible, handles errors like division by zero, wrong types, or list index out of range.
  - Returns a new list with the division results. If division fails, it appends `0` for that element.

---

## 5. **raise_exception.py**
**Function:** `def raise_exception():`
- **Description:** Raises a `TypeError` exception.
- **Key Features:**
  - Demonstrates how to manually raise a `TypeError`.

---

## 6. **raise_exception_msg.py**
**Function:** `def raise_exception_msg(message=""):`
- **Description:** Raises a `NameError` exception with a custom message.
- **Key Features:**
  - Allows passing a message when raising the `NameError`.

---

## 7. **safe_print_integer_err.py**
**Function:** `def safe_print_integer_err(value):`
- **Description:** Attempts to print an integer and handles errors, printing the error to `stderr`.
- **Key Features:**
  - If the value is not an integer, it prints an error message prefixed by "Exception:".
  - Returns `True` if successful, otherwise `False`.

---

## 8. **safe_function.py**
**Function:** `def safe_function(fct, *args):`
- **Description:** Executes a function and returns the result, handling any exceptions that occur during execution.
- **Key Features:**
  - If an exception is raised, it prints an error message and returns `None`.

---

## 9. **magic_calculation.py**
**Function:** `def magic_calculation(a, b):`
- **Description:** This function is reverse-engineered to match specific Python bytecode.
- **Key Features:**
  - Implements bytecode functionality using Python code.
  - Task requires understanding bytecode to implement the correct behavior.

---

## 10. **python.c**
- **Description:** Modifies the header file to use a generic `Python.h` instead of a specific local header file. This file is a part of the C implementation and unrelated to the Python functions.

---



### Conclusion:
These functions demonstrate different scenarios of error handling in Python using `try`, `except`, and `finally` blocks. They showcase how to handle common errors, including type mismatches, division errors, and list index out-of-range errors, ensuring your program runs smoothly without unexpected crashes.

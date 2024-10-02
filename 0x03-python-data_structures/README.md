# 0x03. Python - Data Structures: Lists, Tuples

This repository contains Python functions for various list operations and a C program to check if a singly linked list is a palindrome. Each task demonstrates key programming concepts and practical use of lists in Python and C.

---

## Tasks Overview

### 0. **print_list_integer.py**
- **Function**: `print_list_integer(my_list=[])`
- **Description**: Prints all integers in a list, each on a new line.

---

### 1. **element_at.py**
- **Function**: `element_at(my_list, idx)`
- **Description**: Retrieves the element at the specified index in a list. Returns `None` if the index is out of range.

---

### 2. **replace_in_list.py**
- **Function**: `replace_in_list(my_list, idx, element)`
- **Description**: Replaces an element in a list at a given index. If the index is invalid, the list remains unchanged.

---

### 3. **print_reversed_list_integer.py**
- **Function**: `print_reversed_list_integer(my_list=[])`
- **Description**: Prints integers in a list in reverse order, each on a new line.

---

### 4. **new_in_list.py**
- **Function**: `new_in_list(my_list, idx, element)`
- **Description**: Returns a new list where the element at the given index is replaced. The original list is not modified.

---

### 5. **no_c.py**
- **Function**: `no_c(my_string)`
- **Description**: Removes all instances of 'c' and 'C' from the input string.

---

### 6. **print_matrix_integer.py**
- **Function**: `print_matrix_integer(matrix=[[]])`
- **Description**: Prints a 2D matrix of integers.

---

### 7. **add_tuple.py**
- **Function**: `add_tuple(tuple_a=(), tuple_b=())`
- **Description**: Adds two tuples element-wise. If a tuple is shorter than 2 elements, it is padded with zeros.

---

### 8. **multiple_returns.py**
- **Function**: `multiple_returns(sentence)`
- **Description**: Returns a tuple containing the length of a string and its first character. Returns `None` for the first character if the string is empty.

---

### 9. **max_integer.py**
- **Function**: `max_integer(my_list=[])`
- **Description**: Finds and returns the largest integer in a list. Returns `None` if the list is empty.

---

### 10. **divisible_by_2.py**
- **Function**: `divisible_by_2(my_list=[])`
- **Description**: Identifies elements divisible by 2 in a list. Returns a list of `True` or `False` values.

---

### 11. **delete_at.py**
- **Function**: `delete_at(my_list=[], idx=0)`
- **Description**: Deletes an element at a specified index in the list. Returns the modified list.

---

### 12. **switch.py**
- **Script**: Simple variable swap operation.
- **Description**: Swaps the values of two variables without using temporary storage.

---

### 13. **is_palindrome.c**
- **Function**: `int is_palindrome(listint_t **head)`
- **Description**: Checks whether a singly linked list is a palindrome. Written in C.

---

### Supporting Files

- **linked_lists.c**: Provides helper functions for managing linked lists in C (e.g., adding, freeing nodes).
- **lists.h**: Header file for function prototypes related to linked list operations.

---

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/repo-name.git
   cd repo-name
   ```

2. **Run Python scripts**:
   ```bash
   python3 0-print_list_integer.py
   ```

3. **Compile and run the C program**:
   ```bash
   gcc -Wall -Werror -Wextra -pedantic -std=gnu89 *.c -o palindrome
   ./palindrome
   ```

---

## Notes

- All Python tasks focus on efficient list handling and edge case management.
- The C tasks demonstrate the use of data structures (linked lists) and algorithm design for checking palindromes.

### Author

Created by Ubani Oti-owom.

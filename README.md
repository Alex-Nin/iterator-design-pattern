# Iterable Array with Custom Iterator

This Python project demonstrates the Iterator design pattern by creating a custom iterator for a sequence-like data structure, `MyArray`. The iterator provides sequential access to the elements in `MyArray` while keeping the underlying implementation details hidden, allowing flexible traversal of the array's elements.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Overview](#project-overview)
4. [Key Features](#key-features)
5. [Purpose and Lessons Learned](#purpose-and-lessons-learned)

## Installation

To set up and run this project locally:

1. **Clone the Repository**  
```bash
git clone https://github.com/alex-nin/iterator-design-pattern.git
cd iterator-design-pattern
```

2. **Install Dependencies:** Ensure you have Python 3.x installed.

## Usage

To run the program, execute the following command in your terminal in the program directory, depending on your Python environment:

```bash
python iterator.py
```
or
```bash
python3 iterator.py
```

## Project Overview

The main components include:
- **Iterator Interface**: Defines methods for navigation (`first`, `next`, `is_done`) and accessing the current element (`current`) in a collection.
- **Iterable Interface**: Provides a method to retrieve an iterator for sequential access.
- **Sequence Interface**: Defines basic operations on a sequence-like collection, including `add`, `size`, and `get`.
- **MyArray**: A concrete implementation of `IterableSequence`, representing a dynamic array with a set capacity. It provides methods to add elements and retrieve them by index.
- **MyIterator**: A custom iterator for `MyArray`, implementing navigation and element access methods for traversing `MyArray` elements without exposing the internal structure.

## Key Features

1. **Encapsulated Iteration Logic**: The `MyIterator` class manages element traversal independently, keeping the internal structure of `MyArray` hidden from users.
2. **Flexible Traversal**: Users can initialize the iterator, retrieve the first element, navigate to the next, check completion, and access the current item.
3. **Type-agnostic Design**: The project uses generics, allowing `MyArray` and `MyIterator` to work with any data type.
4. **Custom Collection and Iterator**: `MyArray` and `MyIterator` showcase the flexibility of custom collections and iterators, emphasizing the Iterator pattern's utility in sequence-based structures.


## Purpose and Lessons Learned

This project helped me understand the Iterator design pattern and how to implement custom iterators for user-defined collections. By separating traversal logic from `MyArray`, I saw firsthand how the Iterator pattern improves code structure, making it more flexible and encapsulated. Working with generics also illustrated how the Iterator pattern enables reusable, type-agnostic traversal mechanisms, showcasing its value for both usability and maintainability.

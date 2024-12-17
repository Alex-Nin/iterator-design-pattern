from typing import Callable, Generic, List, TypeVar

T = TypeVar("T")

class Iterator(Generic[T]):
    def first(self):
        raise NotImplementedError
    def next(self):
        raise NotImplementedError
    def is_done(self) -> bool:
        raise NotImplementedError
    def current(self) -> T:
        raise NotImplementedError

class Iterable(Generic[T]):
    def get_iterator(self) -> Iterator[T]:
        raise NotImplementedError

class Sequence(Generic[T]):
    def add(self, value: T):
        raise NotImplementedError
    def size(self) -> int:
        raise NotImplementedError
    def capacity(self) -> int:
        raise NotImplementedError
    def get(self, index: int) -> T:
        raise NotImplementedError

class IterableSequence(Sequence[T], Iterable[T]):
    pass

class MyArray(IterableSequence[T]):
    def __init__(self, elements: List[T]):
        self._array = elements
        self._size = len(elements)
        self._capacity = len(elements)

    def add(self, value: T):
        if self._size < self._capacity:
            self._array[self._size] = value
            self._size += 1

    def size(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._capacity

    def get(self, index: int) -> T:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        return self._array[index]

    def get_iterator(self) -> Iterator[T]:
        return MyIterator(self)

class MyIterator(Iterator[T]):
    def __init__(self, array: MyArray[T]):
        self._array = array
        self._index = 0

    def first(self):
        self._index = 0

    def next(self):
        self._index += 1

    def is_done(self) -> bool:
        return self._index >= self._array.size()

    def current(self) -> T:
        if self.is_done():
            raise StopIteration("Iterator out of bounds")
        return self._array.get(self._index)

class FilterIterator(Iterator[T]):
    def __init__(self, iterator: Iterator[T], predicate: Callable[[T], bool]):
        self._iterator = iterator
        self._predicate = predicate
        self._advance_to_next_valid()

    def _advance_to_next_valid(self):
        while not self._iterator.is_done() and not self._predicate(self._iterator.current()):
            self._iterator.next()

    def first(self):
        self._iterator.first()
        self._advance_to_next_valid()

    def next(self):
        self._iterator.next()
        self._advance_to_next_valid()

    def is_done(self) -> bool:
        return self._iterator.is_done()

    def current(self) -> T:
        if self.is_done():
            raise StopIteration("Iterator out of bounds")
        return self._iterator.current()

class ReverseIterator(Iterator[T]):
    def __init__(self, iterator: Iterator[T]):
        self._items = []
        iterator.first()
        while not iterator.is_done():
            self._items.append(iterator.current())
            iterator.next()
        self._index = len(self._items) - 1

    def first(self):
        self._index = len(self._items) - 1

    def next(self):
        self._index -= 1

    def is_done(self) -> bool:
        return self._index < 0

    def current(self) -> T:
        if self.is_done():
            raise StopIteration("Iterator out of bounds")
        return self._items[self._index]

if __name__ == "__main__":
    words = [
        "American", " ", "flags", " ", "left", " ", "on", " ", "the", " ", "moon", " ", "will", " ",
        "eventually", " ", "get", " ", "bleached", " ", "white", " ", "by", " ", "the", " ", "sun", ".",
        " ", "While", " ", "they", " ", "are", " ", "hibernating", ",", " ", "bears", " ", "do", " ",
        "not", " ", "urinate", ".", " ", "Their", " ", "bodies", " ", "convert", " ", "waste", " ",
        "into", " ", "protein", ".", " ", "White", "-", "faced", " ", "capuchin", " ", "monkeys", " ", "greet",
        " ", "each", " ", "other", " ", "by", " ", "sticking", " ", "their", " ", "fingers", " ", "up",
        " ", "each", " ", "others", "’", " ", "noses", ".", " ", "Gummy", " ", "bears", " ", "were", " ",
        "originally", " ", "called", " ", "\"", "dancing", " ", "bears", ".", "\"", " ", "New", " ",
        "Zealand", " ", "has", " ", "more", " ", "cats", " ", "per", " ", "person", " ", "than", " ",
        "any", " ", "other", " ", "country", " ", "in", " ", "the", " ", "world", "."
    ]

    array = MyArray(words)

    iterator = array.get_iterator()
    print("Original Paragraph:")
    while not iterator.is_done():
        print(iterator.current(), end="")
        iterator.next()
    print("\n")

    def is_not_punctuation_or_space(word):
        if word == " " or word == "," or word == "." or word == "\"" or word == "’" or word == "-":
            return False
        return True

    filtered_iterator = FilterIterator(array.get_iterator(), is_not_punctuation_or_space)
    print("Filtered (No Punctuation or Whitespaces):")
    while not filtered_iterator.is_done():
        print(filtered_iterator.current(), end="")
        filtered_iterator.next()
    print("\n")

    reverse_iterator = ReverseIterator(array.get_iterator())
    print("Reversed Paragraph:")
    while not reverse_iterator.is_done():
        print(reverse_iterator.current(), end="")
        reverse_iterator.next()
    print("\n")

    reverse_filtered_iterator = ReverseIterator(filtered_iterator)
    print("Reversed Filtered (No Punctuation/Whitespace):")
    while not reverse_filtered_iterator.is_done():
        print(reverse_filtered_iterator.current(), end="")
        reverse_filtered_iterator.next()
    print()

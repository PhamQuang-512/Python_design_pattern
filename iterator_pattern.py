from __future__ import annotations
from collections.abc import Iterator, Iterable
from typing import Any


class AlphabeticalOrderIterator(Iterator):
    def __init__(self, _collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = _collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    def __init__(self, collections=None) -> None:
        if collections is None:
            collections = []
        self.__collection = collections

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self.__collection, False)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self.__collection, True)

    def add_item(self, item: Any):
        self.__collection.append(item)

    def __getitem__(self, item):
        return self.__collection[item]


if __name__ == '__main__':
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    print(" | ".join(collection))
    straight_iter = iter(collection)
    print(next(straight_iter))
    print(next(straight_iter))
    print(next(straight_iter))
    print("")

    print("Reverse traversal:")
    print(" | ".join(collection.get_reverse_iterator()))
    reverse_iter = collection.get_reverse_iterator()
    print(next(reverse_iter))
    print(next(reverse_iter))
    print(next(reverse_iter))

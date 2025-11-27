class FlattenIterator:
    def __init__(self, nested_list):
        self._stack = [iter(nested_list)]

    def __iter__(self):
        return self

    def __next__(self):
        while self._stack:
            try:
                current_item = next(self._stack[-1])
            except StopIteration:
                self._stack.pop()
                continue
            if isinstance(current_item, list):
                self._stack.append(iter(current_item))
                continue
            else:
                return current_item
        raise StopIteration


lst = [[1, 2], [3, [4]], 5, [6]]
for element in FlattenIterator(lst):
    print(element)
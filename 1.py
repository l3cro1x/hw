class ChainIterator:
    def __init__(self, *sequences: tuple[list, ...]):
        self.sequences = sequences
        self.index = 0
        self.sequences_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.sequences_index += 1
            return self.sequences[self.index][self.sequences_index - 1]

        except:
            self.index += 1
            self.sequences_index = 1
            if self.index == len(self.sequences):
                raise StopIteration
            return self.sequences[self.index][self.sequences_index - 1]


seq = ChainIterator([1, 2, 3], [4], [5])
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))

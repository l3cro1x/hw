class ZipIterator:
    def __init__(self, *sequences: list):
        self.sequences = sequences
        self.index = 0
        self.sequences_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.sequences):
            raise StopIteration
        new_sequence = []
        for seq in self.sequences:
            new_sequence.append(seq[self.index])
        self.index += 1
        return new_sequence


seq = ZipIterator([1, 2, 3], [4, 5, 6])
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))

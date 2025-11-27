def func(sequence, k):
    if k == 0:
        yield ()
        return
    if not sequence:
        return
    head = sequence[0]
    tail = sequence[1:]

    for combo_tail in func(tail, k - 1):
        yield (head,) + combo_tail

    yield from func(tail, k)


for i in func([1,2,3],2):
    print(i)

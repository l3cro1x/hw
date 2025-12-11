def is_pal(n):
    if len(n) == 1:
        return True
    if n[0] != n[-1]:
        return False
    return is_pal(n[1:-1])


print(is_pal('racecar'))
print(is_pal('error'))

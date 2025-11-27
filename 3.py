def is_prime(n):
    k = 0
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            k +=1
            return False
    return True

class MyIterator:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start < self.end:
            self.start +=1
            return self.start -1
        raise StopIteration

for i in MyIterator(1,10):
    if is_prime(i):
        print(i)
import time


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        time.sleep(1)
        result = method(*args, **kw)
        te = time.time()
        print(te - ts - 1)
        return result

    return timed


@timeit
def hsg(n):
    while n > 1:
        n = n // 2 if n % 2 == 0 else n * 3 + 1
        yield n
def len_hsg(n):
    return len(list(hsg(n)))


@timeit
class Hailston:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > 1:
            self.n = self.n // 2 if self.n % 2 == 0 else self.n * 3 + 1
            return self.n
        else:
            raise StopIteration


print(list(hsg(1000)))
print(len_hsg(1000))
his = iter(Hailston(1000))
print(list(his))

def squ(n):
    i = 1
    while i <= n:
        yield i**2
        i += 1
    yield "end"


n = int(input())

for x in squ(n):
    print(x)



def even(n):
    i = 1
    while i <= n:
        if (i % 2) == 0:
            yield i
        i += 1
    yield "end"


n = int(input())

for x in even(n):
    print(x)




def div(n):
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 4 == 0:
            yield i
        i += 1
    yield "end"

n = int(input())

for x in div(n):
    print(x)



def squ(a, b):
    for x in range(a, b + 1, 1):
        yield x**2
    yield "end"


a = int(input())
b = int(input())

for x in squ(a, b):
    print(x)


def cou(n):
    while n >= 0:
        yield n
        n -= 1
    yield "end"

n = int(input())

for x in cou(n):
    print(x)

















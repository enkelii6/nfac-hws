import time


def calculate():
    return 100


def generator():
    yield 1
    time.sleep(5)
    print('Second yield')
    yield 2
    yield calculate()


gen = generator()

print(next(gen))
print('1st call ended')
print(next(gen))
print(next(gen))

gen2 = generator()

for i in gen2:
    print(i)

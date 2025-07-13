import random
import string
seq = string.ascii_uppercase + string.ascii_lowercase
print(random.choice(seq))

L1 = [10, 20, 30, 40, 1, 2, 3]

random.shuffle(L1)
print(L1)

print(random.randint(1, 5))

for i in range(5):
    random.seed(1, 100)
    print(random.randint(1, 100))

for i in range(5):
    print(random.random())

print(random.randrange(2, 10))
print(random.randrange(2, 10, 2))

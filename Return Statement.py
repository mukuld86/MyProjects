"""x = 10
y = 20


def add(x, y):
    return x + y
a = add(x, y)
print(a)


def sub(x, y):
    return x - y
b=sub(x, y)
print(b)


def mul(x, y):
    return x * y
c=mul(x,y)
print(c)
"""

a = int(input())
b = int(input())


def f1(x, y):
    sum = x + y
    avg = (x + y) / 2
    return sum, avg


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


s, av = f1(a, b)
v2 = sub(a, b)
v3 = mul(a, b)

print("sum,average={},{}".format(s, av))
print("difference is", v2)
print("product is", v3)

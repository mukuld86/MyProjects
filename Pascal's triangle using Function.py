# Pascal triangle
# Very important for Resume

def pascal(x):
    for line in range(1, x + 1):
        c = 1     # used to represent C(line,i)
        for i in range(1, line + 1):
            print(c, end="")
            c = int(c * (line - i) / i)
        print()
# calling the function
n = int(input("Enter an integer: "))
print(pascal(n))

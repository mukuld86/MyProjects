for i in range(5, 0, -1):
    c = 'a'
    u = ord(c)
    for j in range(1, i + 1):
        C = chr(u)
        print(C,end="")
        u += 1
    print()
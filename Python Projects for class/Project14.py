dic={"Rajdeep":"9xxxxxxxx9","Nipun":"8xxxxx7xxx9",}
while True:
    name=input("Enter name (OR Write quit to exit the application): ")
    if name=="all" or name=="ALL":
        print(dic)
    elif name=="quit":
        exit()
    else:
        print(dic[name])
def sayhello(username):
    greet = "Hello "
    print(greet + username)


users = ["Ram", "Mahesh", "Vasudha", "Uma", "Shekhar", "John"]

for i in users:         # call the function by passing items of the list as arguments
        sayhello(i)

while True:
    email=input("Enter your email address: ")
    a=email.index("@")
    s1=email[:a]
    s2=email[a+1:]
    print("username: {} and domain: {}".format(s1,s2.lower()))
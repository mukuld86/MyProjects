s1 = int(input("Enter Side 1:"))
s2 = int(input("Enter Side 2:"))
s3 = int(input("Enter Side 3:"))

if s1 == s2 and s1 == s3:
    print("Triangle is Equilateral")
elif s1 == s2 and s1 != s3:
    print("Triangle is Isosceles")
else:
    print("Triangle is Scalene")

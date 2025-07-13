import random
a=int(input("range start point"))
b=int(input("range ending point"))
number = random.randrange(a,b)
attempts=3
score=0
while True:
    guess = int(input("Guess a number: "))
    if guess == number:
        score+=1
        print("Congrat's","Your Score is",score)
        break
    elif guess>number:
        attempts-=1
        if attempts==0:
            print("Better Luck Next Time!")
            break
        print("have one more try. Your guess was too high")
    elif guess<number:
        attempts-=1
        if attempts==0:
            print("Better Luck Next Time!")
            break
        print("have one more try. Your guess was too small")
    else:
        pass

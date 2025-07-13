import random
def game(Score):
    number = random.randrange(a,b)
    attempts=3
    while True:
        guess = int(input("Guess a number: "))
        if guess == number:
            Score+=1
            print("Congrat's","Your Score is",Score)
            game(Score)
        elif guess>number:
            attempts-=1
            if attempts==0:
                print("Better Luck Next Time! Your Overall score is",Score)
                exit()
            print("You have",attempts,"tries left. Your guess was too high")
        elif guess<number:
            attempts-=1
            if attempts==0:
                print("Better Luck Next Time!Your Overall score is",Score)
                exit()
            print("You have",attempts,"tries left. Your guess was too low")
    else:
        pass
a=int(input("range start point"))
b=int(input("range ending point"))
score=0
game(score)




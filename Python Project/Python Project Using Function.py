"""
The task is to create a script that generates a random number between a fixed range, and if the
user guesses the number right in three chances, then user wins otherwise user lose.
This game user can play as many numbers of times and whenever user wins a score is to be
given to the user.
At the end the users score must be displayed on the screen.
Hint: Make use of random module to design the game

Abstract steps:
 The user enters the lower and upper bounds of the range.
 As a result, the compiler generates a random integer between the range and stores it in
a variable for future use.
 A while loop will be created for repetitive guessing.
 When a user guesses a number that is greater than a randomly selected number, the
user receives the message “have one more try”. Your guess was too high.
 If the user guesses a number smaller than a randomly selected number, the user gets an
output of “have one more try “. Your guess was too small”
 In addition, if the user guesses within a minimum number of attempts, they get a
“Congrat’s” message and also get the winning scores.
 If the user fails to guess the integer in the minimum number of guesses, he/she will
receive a “Better Luck Next Time!

(Student is free to decide the input and output layout for this mini project)
"""
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
import random
L=['Rock', 'Paper', 'Scissors']
score=0
while True:
    UserChoice = input("Rock/Paper/Scissors OR quit for quitting the game: ")
    if UserChoice.lower()=="quit":
        print("Thank you for playing the game! Your overall score is",score)
        exit()
    else:
        CPU = random.choice(L)
        print("CPU:", CPU)
        if UserChoice.lower()=="rock":
            if CPU=="Rock":
                print("Tie")
            elif CPU=="Paper":
                print("You lose! Paper covers Rock")
            else:
                score += 1
                print("You Win! Rock smashes Scissors. Your score is",score)
        elif UserChoice.lower()=="paper":
            if CPU == "Rock":
                score += 1
                print("You Win! Paper covers Rock. Your score is",score)
            elif CPU == "Paper":
                print("Tie")
            else:
                print("You Lose! Scissors cuts Paper")
        elif UserChoice.lower() == "scissors":
            if CPU == "Rock":
                print("You Lose! Rock smashes Scissors")
            elif CPU == "Paper":
                score += 1
                print("You Win! Scissors cuts Paper. Your score is",score)
            else:
                print("Tie")
        else:
            print("Wrong Input!")
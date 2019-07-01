"""
    This is a guess number game, guess a number between 1 and 10.
    The maximum number of trials is 3, after that is GAME OVER!!!
"""

import random
flag = True

def guess(ans):
    count = 0
    flag = True
    while flag:
        if count < 3:
            #prompt for user guess number
            g = input("Guess a number between 1 and 10 ")
            #convert the user guessed number to integer
            #if user does not enter number prompt them to.
            try:
                guess_num = int(g)
            except:
                print("Please enter a number")
                continue

            if guess_num == ans:
                print(str(guess_num) + " Is the correct answer.")
                again()
                flag = False
            elif guess_num < ans:
                print(str(guess_num) + " Is too low.")
            elif guess_num > ans:
                print(str(guess_num) + " Is too high.")
            count += 1

        elif count >= 3:
            print("You tried {} times!!!".format(str(count)))
            print("GAME OVER!!!")
            again()
            flag = False

#Random numbers between 1 and 20
r = random.randint(1, 10)

#Ask if user want to play again
def again():
    response = input("Do you want to play again? : Yes/No ")
    if response.title() == "No":
        print("Thank You")
        pass
    elif response.title() == "Yes":
        guess(r)

guess(r)
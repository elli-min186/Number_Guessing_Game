# A program where the user has to guess the random number generated by the program.
# There are 3 levels in total: Easy, Medium and Hard.
# There will be 5 attempts available in each level and the game is over if the user cannot guess within 5 attempts.
# After the game is over or the user has guessed the number, the program will ask if the user wants to play again.

from random import randint
# importing the "random" library to get random integers.


def game():  # function game
    def check_greater():  # function check_greater
        return int(guess) > random_num
        # return the guess number if the guess is greater than the number generated.

    def check_less():
        return int(guess) < random_num
        # return the guess number if the guess is less than the number generated.

    def check_equal():
        return int(guess) == random_num
        # return the guess number if the guess is equal to the number generated.

# the comments starting from here applies to all the codes of if condition until the end of the function with
    # different conditions.

    print("Welcome to the game of guessing numbers!")
    # print the statement in the game function.
    level = input("Choose a level: 'Easy', 'Medium', 'Hard': ")
    # assign variable level to the user input of easy, medium or hard.
    if level.lower() == "easy":
        # if the user input is easy regardless of the cases,
        attempt = 5
        # the variable attempt will be assigned as 5.
        random_num = int(randint(1, 10))
        # random number generated will be within 1 and 10 and assign it to random_num variable.
        while attempt > 0:
            # as long as the attempt is greater than 0,
            guess = input("Enter a number from 1 to 10: ")
            # guess variable will store the user input from 1 to 10.
            if check_greater():
                # if the guess number from the user is greater than the random number generated,
                print("The number is lower than that.")
                # print the statement.
                attempt -= 1
                # subtract one from the value of attempt.
                print("You have {} attempts left.".format(attempt))
                # print the statement with the number of attempts left in {} brackets.
                continue
                # continue the game/loop
            elif check_less():
                # if the guess number from the user is less than the random number generated,
                print("The number is higher than that.")
                # print the statement.
                attempt -= 1
                # subtract one from the value of attempt.
                print("You have {} number of attempts left.".format(attempt))
                # print the statement with the number of attempts left in {} brackets.
                continue
                # continue the game/loop
            elif check_equal():
                # if the guess number from the user is equal to the random number generated,
                print("Great guess! You got it!")
                # print the statement.
                print("You won with {} attempts left.".format(attempt))
                # print the statement with the number of attempts left in {} brackets.
                break
                # break the loop as the game is won.
            elif attempt == 0:
                # if the attempt becomes 0,
                print("Game Over!")
                # print the statement.
                break
                # break the loop as the game is over.
    elif level.lower() == "medium":
        # if the user chooses the medium level regardless of the cases,
        attempt = 5
        random_num = int(randint(1, 20))
        while attempt > 0:
            guess = input("Enter a number from 1 to 20: ")
            if check_greater():
                print("The number is lower than that.")
                attempt -= 1
                print("You have {} number of attempts left.".format(attempt))
                continue
            elif check_less():
                print("The number is higher than that.")
                attempt -= 1
                print("You have {} number of attempts left.".format(attempt))
                continue
            elif check_equal():
                print("Great guess! You got it!")
                print("You won with {} attempts left.".format(attempt))
                break
    elif level.lower() == "hard":
        # if the user chooses hard level regardless of the cases,
        attempt = 5
        random_num = int(randint(1, 40))
        while attempt > 0:
            guess = input("Enter a number from 1 to 40: ")
            if check_greater():
                print("The number is lower than that.")
                attempt -= 1
                print("You have {} number of attempts left.".format(attempt))
                continue
            elif check_less():
                print("The number is higher than that.")
                attempt -= 1
                print("You have {} number of attempts left.".format(attempt))
                continue
            elif check_equal():
                print("Great guess! You got it!")
                print("You won with {} attempts left.".format(attempt))
                break
    else:
        # if the above conditions are not met,
        game()
        # go back to the start of the function


def play_again():
    # the function play_again
    play = input("Would you like to play again? (Enter Yes/No): ")
    # store the user input in the play variable.
    if play.lower() == "yes":
        # if the player chooses yes regardless the cases,
        return True
    elif play.lower() == "no":
        # if the player chooses not to play again,
        print("Thanks for playing! Have a good day!")
        # print the statement.
        return False
    else:
        # if the above conditions are not met,
        return play_again()
    # go back to the start of the function again.


if __name__ == '__main__':
    # main function
    run = True
    # assign the run variable to True
    while run == True:
        # as long as the run variable is True,
        game()
        # start the game.
        run = play_again()
        # assign the run variable to play_again function.

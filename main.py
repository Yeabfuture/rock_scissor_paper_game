# importing module
import random

# Defining a variable for the number of total games user wants to play and the number of total games he played.

total = 0
number_of_times_played = int(input("How many times would you like to play? "))

# creating a loop which keeps the game active till the number of games he wants to play reached
while total < number_of_times_played:
    # Declaring a function that asks a user a choice and make the computer chose randomly from the given options
    def get_choices():
        player_choice = input('Enter your choice(paper, rock, scissors: ').lower()
        option = ['paper', 'rock', 'scissors']
        computer_choice = random.choice(option)
        choices = {"Player": player_choice, "Computer": computer_choice}
        return choices

    # Declaring a function that checks both choices, compare them by the rule and give the result and counts.
    def check_win(player, computer):
        print(f'You chose {player} and the computer chose {computer}')

        if player == computer:
            global total
            total += 1
            return "It's a tie"
        elif player == 'rock':
            if computer == 'scissors':
                total += 1
                return 'Rock smashes scissors. You win =:)'
            else:
                total += 1
                return 'Paper covers rock. You lose :('
        elif player == 'scissors':
            if computer == 'rock':
                total += 1
                return 'Rock smashes scissors. You Lose:('
            else:
                total += 1
                return 'Scissors cut paper. You win :)'
        elif player == 'paper':
            if computer == 'rock':
                total += 1
                return 'Paper covers rock. You win :)'
            else:
                total += 1
                return ' Scissor cut paper. You Lose :('


    choices = get_choices()
    result = check_win(choices['Player'], choices['Computer'])
    print(result)
else:
    print('Gave Over. Play Again!')
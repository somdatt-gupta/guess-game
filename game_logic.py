import random as rd
# def play_game():
#     print("Welcome to Number guess game.")
#     ready = input("are you ready to play the game(Yes/No) ?  ")

#     if (ready.strip()).lower() == 'yes':

#         print("Let's play the Game.")
#         players = int(input("Enter the number of players Who are going to play this game: "))

#         player_name_and_score = []

#         for i in range(players):
#             n = rd.randint(1, 100)
#             curr_player = (input("Enter the player name: ")).capitalize()
#             print(f"Okk {curr_player}, let's play the game.")

#             a = 0
#             count = 0
            
#             while (a != n):
                
#                 try:
#                     a = int(input("Guess a Number: "))
#                     count += 1

#                     if (a == n):
#                         print(f'Woo hoo, You have guessed the number.')
#                     elif (a < n):
#                         print("You should try a higher number.")
#                     else:
#                         print("You should try a lower number.")
#                 except Exception:
#                     print("INVALID INPUT. Please put numbers between 1 to 100.")
            
#             print(f"Your number was {n}")
            
#             player_name_and_score.append((curr_player, count))

#         winner = ''
#         min_moves = 10000

#         for player, moves in player_name_and_score:
#             if moves < min_moves:
#                 winner = player
#                 min_moves = moves
        
#         print(f'Congratulation {winner}, You have win the game using {moves} guesses only.')

#         restart = input("Would you like to play the game again ?  ")
#         if (restart.strip()).lower() == "yes":
#             play_game()
#         else:
#             print("Thank you for playing the game.")
#     else:
#         print("Thanks for visiting us.")

# play_game()

def welcome_msg():
    print("Welcome to the number Guessing Game!")
    ready = input("Are you ready to play the game (Yes/No) ? ").strip().lower()

    return ready == 'yes'

# def choose_difficulty():
#     print("Choose the difficulty level: ")
#     print("1. Easy (1 - 100, unlimited attempts)")
#     print("2. Easy (1 - 200, unlimited attempts)")
#     print("3. Easy (1 - 200, 50 attempts)")

#     while True:
#         try:
#             choice = int(input("Enter your choice (1, 2 or 3)"))
#             if choice == 1:
#                 return {'range': (1, 100), 'max_attempts': None}
#             elif choice == 2:
#                 return {'range': (1, 200), 'max_attempts': None}
#             elif choice == 3:
#                 return {'range': (1, 200), 'max_attempts': 50}
#             else:
#                 print("INVALID choice! Please choice 1, 2 or 3.")

#         except ValueError:
#             print("Invalid input! Please enter a number (1, 2 or 3).")

def get_players():
    while True:
        try:
            players = int(input("Enter the number of players: "))
            if players > 0:
                break

            print("The number of player must be at least 1.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    player_names = [input(f'Enter player\'s name : ').capitalize() for i in range(players)]

    return player_names

def get_valid_guess():
    while True:
        try:
            guess = int(input("Guess a number: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please guess a number between 1 to 100.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def play_single_round(player_name, target_number):
    print(f'Okay {player_name}, let\'s start!')
    attempts = 0

    while True:
        guess = get_valid_guess()
        attempts += 1

        if guess == target_number:
            print(f'Congratulations, {player_name}! You guessed the number!')
            return attempts
        elif guess < target_number:
            print("You should try a higher number.")
        else:
            print("You should try a lower number.")

def determine_winner(scores):
    return min(scores, key = lambda x: x[1])

def play_game():
    if not welcome_msg():
        print("Thanks for visiting us.")
        return
    
    player_names = get_players()
    scores = []

    for player_name in player_names:
        target_number = rd.randint(1, 100)
        attempts = play_single_round(player_name, target_number)
        scores.append((player_name, attempts))

    winner, min_attempts = determine_winner(scores)

    print(f'🎉 Congratulations {winner}! You won with just {min_attempts} guesses! 🎉')

    if input("Would you like to play again (Yes/No) ? ").strip().lower() == 'yes':
        play_game()
    else:
        print("Thank you for playing! See you next time.")

play_game()
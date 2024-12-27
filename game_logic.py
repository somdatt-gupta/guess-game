import random as rd
def play_game():
    print("Welcome to Number guess game.")
    ready = input("are you ready to play the game(Yes/No) ? ")

    if (ready.strip()).lower() == 'yes':

        print("Let's play the Game.")
        players = int(input("Enter the number of players Who are going to play this game: "))

        player_name_and_score = []

        for i in range(players):
            n = rd.randint(1, 100)
            curr_player = (input("Enter the player name: ")).capitalize()
            print(f"Okk {curr_player}, let's play the game.")

            a = 0
            count = 0
            
            while (a != n):
                
                try:
                    a = int(input("Guess a Number: "))
                    count += 1

                    if (a == n):
                        print(f'Woo hoo, You have guessed the number.')
                    elif (a < n):
                        print("You should try a higher number.")
                    else:
                        print("You should try a lower number.")
                except Exception:
                    print("INVALID INPUT. Please put numbers between 1 to 100.")
            
            player_name_and_score.append((curr_player, count))

        winner = ''
        min_moves = 10000

        for player, moves in player_name_and_score:
            if moves < min_moves:
                winner = player
                min_moves = moves
        
        print(f'Congratulation {winner}, You have win the game using {moves} guesses only.')

        restart = input("Would you like to play the game again ? ")
        if (restart.strip()).lower == "yes":
            play_game()
        else:
            print("Thank you for playing the game.")
    else:
        print("Thanks for visiting us.")

play_game()
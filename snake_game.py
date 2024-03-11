import random

def game():
    choices = ["snake", "water", "gun"]
    computer_choice = random.choice(choices)
    print("Snake, Water, Gun Game")
    x= int(input("The game should be of how many points? "))
    print("Choose your weapon: ")
    print("1. Snake")
    print("2. Water")
    print("3. Gun")
    
    player_point = 0
    computer_point = 0

    for i in range(x):
        player_choice = input("Enter your choice (1/2/3): ")

        if player_choice == "1":
            player_choice = "snake"
        elif player_choice == "2":
            player_choice = "water"
        elif player_choice == "3":
            player_choice = "gun"
        else:
            print("Invalid choice!")
            return

        print("You chose:", player_choice)
        print("Computer chose:", computer_choice)
        if player_choice == computer_choice:
            print("It's a tie!")

        elif player_choice == "snake":
            if computer_choice == "water":
                print("You win!")
                player_point += 1
            else:
                print("Computer wins!")
                computer_point += 1
        elif player_choice == "water":
            if computer_choice == "gun":
                print("You win!")
                player_point += 1
            else:
                print("Computer wins!")
                computer_point += 1
        elif player_choice == "gun":
            if computer_choice == "snake":
                print("You win!")
                player_point += 1
            else:
                print("Computer wins!")
                computer_point += 1
    
    if player_point <= computer_point:
        print("\n GAME OVER \n Computer Wins the game")
    elif player_point >= computer_point:
        print("\n GAME OVER \n You won the game")
    else:
        print("\n GAME OVER \n It is a TIE")

while True:
    game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break

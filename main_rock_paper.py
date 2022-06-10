import random

while True:

    print("R for Rock")
    print("P for Paper")
    print("S for Scissors")
    user_choice = input("Enter a choice: ")
    possible_choices = ["R", "P", "S"]
    cpu_choice = random.choice(possible_choices)

    if user_choice == cpu_choice:
        print(f"Both players made same move. It's a tie!")
        print("-----------------------------------------")
        print("PLAY AGAIN")
    elif user_choice == "R":
        if cpu_choice == "S":
            print("Player(Rock) : CPU(Scissors). You win!")
            break
        else:
            print("Player(Rock): CPU(Paper). CPU wins")
            break
    elif user_choice == "P":
        if cpu_choice == "R":
            print("Player(Paper) : CPU(Rock). You win!")
            break
        else:
            print("Player(Paper) : CPU(Scissors). CPU wins!")
            break
    elif user_choice == "S":
        if cpu_choice == "P":
            print("Player(Scissors) : CPU(Paper). You win!")
            break
        else:
            print("Player(Scissors) : CPU(Rock). CPU wins!")
            break

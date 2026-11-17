from game import create_player, collect_item, move_player, light_beacon


def show_intro():
    print("\n================================")
    print("   MYSTERY ISLAND")
    print("   THE LOST LIGHTHOUSE")
    print("================================")
    print("Your ship has been destroyed by a storm.\n")
    print("You are stranded on a mysterious island.")
    print("Find a way to restore the lighthouse!")
    print("You have only 5 energy points.\n")


def show_status(player):
    print("\n---------- PLAYER STATUS ----------")
    print("Name:", player["name"])
    print("Location:", player["location"])
    print("Energy:", player["energy"])
    print("Inventory:", player["inventory"])
    print("-----------------------------------")


def play_game():
    show_intro()

    name = input("Enter your name, adventurer: ")
    player = create_player(name)

    while not player["game_over"]:

        show_status(player)

        print("\nWhat would you like to do?")
        print("1. Explore")
        print("2. Collect an item")
        print("3. Rest")
        print("4. Quit")
        print("5. Light the lighthouse beacon")

        choice = input("Choose 1-5 ")

        if choice == "1":
            destination = input(
                "Where do you want to go? "
                "(Beach, Jungle, Cave, Old Bridge, Lighthouse): "
            )

            print(move_player(player, destination.title()))

        elif choice == "2":

            if player["location"] == "Jungle":
                print(collect_item(player, "Rope"))

            elif player["location"] == "Cave":
                print(collect_item(player, "Lantern"))

            else:
                print("There are no useful items here!")

        elif choice == "3":

            if player["rested"]:
                print("You have already rested! You cannot rest again.")

            else:
                player["energy"] = 5
                player["rested"] = True
                print("You rested and restored your energy!")

        elif choice == "4":
            print("You abandoned your adventure!")
            break

        elif choice == "5":
            print(light_beacon(player))

        else:
            print("Invalid choice! Please choose between 1 and 5.")


if __name__ == "__main__":
    play_game()
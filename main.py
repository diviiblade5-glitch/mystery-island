from game import create_player, collect_item, move_player, light_beacon, lose_energy

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
        print("6. Make a decision")



        choice = input("Choose 1-6: ")

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
                print("There are no useful items here!😴")

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


        elif choice == "6":

            if player["location"] == "Jungle":

                if player["jungle_decision_made"]:
                    print("You have already made this decision!")

                else:
                    print("\nYou discover two possible paths.")
                    print("1. Take the dangerous shortcut and lose 1 energy.")
                    print("2. Take the long but safe route and save energy.")

                    decision = input("Choose 1 or 2: ")

                    if decision == "1":
                        player["jungle_decision_made"] = True
                        print("You took the shortcut but lost 1 energy!")
                        print(lose_energy(player))

                    elif decision == "2":
                        print("You took the safe route. No energy lost!")
                        player["jungle_decision_made"] = True

                    else:
                        print("Invalid decision! You can try again.")

            elif player["location"] == "Cave":

                if player["cave_decision_made"]:
                    print("You have already made this decision!")

                else:
                    print("\nYou hear a strange sound deep inside the Cave.")
                    print("1. Investigate the sound and lose 1 energy.")
                    print("2. Ignore the sound and conserve your energy.")

                    decision = input("Choose 1 or 2: ")

                    if decision == "1":
                        player["cave_decision_made"] = True
                        print("You investigated the sound and discovered an ancient symbol!")
                        print(lose_energy(player))

                    elif decision == "2":
                        print("You ignored the sound and continued safely.")
                        player["cave_decision_made"] = True

                    else:
                        print("Invalid decision! You can try again.")

            elif player["location"] == "Old Bridge":

                if player["bridge_decision_made"]:
                    print("You have already made this decision!")

                else:
                    print("\nThe Old Bridge is unstable!")
                    print("1. Cross carefully and lose 1 energy.")
                    print("2. Make a risky jump and risk losing your Rope.")

                    decision = input("Choose 1 or 2: ")

                    if decision == "1":
                        player["bridge_decision_made"] = True
                        print("You crossed carefully but lost 1 energy!")
                        print(lose_energy(player))

                    elif decision == "2":

                        if "Rope" in player["inventory"]:
                            player["inventory"].remove("Rope")
                            print("You made the jump, but your Rope fell into the river!")
                        else:
                            print("You made the jump successfully!")

                        player["bridge_decision_made"] = True

                    else:
                        print("Invalid decision! You can try again.")

            else:
                print("There are no decisions to make here right now.")



    if player["won"]:
        print("\n================================")
        print("       YOU ARE VICTORIOUS!")
        print("================================")
        print("The lighthouse beacon is shining!")
        print("A rescue boat spots your signal.")
        print("You have escaped Mystery Island!")

    elif player["energy"] <= 0:
        print("\n================================")
        print("          GAME OVER")
        print("================================")
        print("You ran out of energy.")
        print("The island remains your prison........forever☠️")



if __name__ == "__main__":
    play_game()             
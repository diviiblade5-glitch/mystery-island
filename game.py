def create_player(name):
    return {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False,
        "rested": False,
        "beacon_lit": False
    }


def collect_item(player, item):
    if item not in player["inventory"]:
        player["inventory"].append(item)
        return f"You collected {item}!"

    return "You already have that item."


def lose_energy(player, amount=1):
    player["energy"] -= amount

    if player["energy"] <= 0:
        player["energy"] = 0
        player["game_over"] = True
        return "You have run out of energy. Game over!"

    return f"You have {player['energy']} energy remaining."


def move_player(player, destination):

    paths = {
        "Beach": ["Jungle"],
        "Jungle": ["Beach", "Cave"],
        "Cave": ["Jungle", "Old Bridge"],
        "Old Bridge": ["Cave", "Lighthouse"],
        "Lighthouse": ["Old Bridge"]
    }

    current = player["location"]

    # Check whether the destination exists
    if destination not in paths[current]:
        return "You cannot travel there from here!"

    # Check for the rope before crossing the bridge
    if destination == "Old Bridge":
        if "Rope" not in player["inventory"]:
            return "You need a Rope to cross the bridge!"

    # Check for the lantern before entering the lighthouse
    if destination == "Lighthouse":
        if "Lantern" not in player["inventory"]:
            return "You need a Lantern to enter the lighthouse!"

    # Move the player
    player["location"] = destination

    # Moving costs one energy
    return lose_energy(player, 1)



def light_beacon(player):
    if player["location"] != "Lighthouse":
        return "You must reach the Lighthouse first!"

    if "Lantern" not in player["inventory"]:
        return "You need a Lantern!"

    player["beacon_lit"] = True
    player["won"] = True
    player["game_over"] = True

    return "THE LIGHTHOUSE IS LIT! A RESCUE SHIP IS COMING! YOU WIN!"
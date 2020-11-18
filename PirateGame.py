import time

import random

import sys


# 1.5 sec pause is made after the text is printed
def print_pause(message):
    print(message)
    time.sleep(1.5)


# Description of the player’s story
def intro():
    print_pause("You find yourself standing on a pirate ship"
                "at sunrise.")
    print_pause("You look around and notice a treasure chest")

    print_pause("Your goal is to pacify the shipmates"
                "to safely steer the ship home.")


# Validation of the player's input
def valid_input(message, options):
    while True:
        response = input(message).lower()
        for option in options:
            if option == response:
                response = option
                return response
        print_pause("Sorry, this isn't an option.")


# Different scenarios based on the previous choice in case
# the player meets a human pirate
def human_pirate(item, play_again_list):
    if item == "gold":
        print_pause("Gold makes the human pirate very happy.")
        print_pause("He decides to help you get home.")
    else:
        if item == "brains":
            print_pause("Your brains scared the human pirate and "
                        "he makes you walk the plank.")
        elif item == "bones":
            print_pause("Bones aren't something human pirates "
                        "expect as a gift! It makes him angry.")
        print_pause("The angry pirate throws you overboard.")
        print_pause("You lost! You didn't manage to sail home.")
        play_again(play_again_list)


# Different scenarios based on the previous choice in case
# the player meets a zombie pirate
def zombie_pirate(item, play_again_list):
    if item == "brains":
        print_pause("After feeding the zombie the jar of brains,")
        print_pause("The zombies leave you alone!")
    elif item == "bones" or item == "gold":
        print_pause("This wasn't effective against zombies!")
        print_pause("You lost! You've also been eaten by"
                    "the zombie!")
        play_again(play_again_list)


# Different scenarios based on the previous choice in case
# the player meets a hungry dog
def hungry_dog(item, play_again_list):
    if item == "bones":
        print_pause("You fed the hungry dog a bone.")
        print_pause("The dog is happy now! You may continue your way.")
    elif item == "gold" or item == "brains":
        print_pause("This did not make the dog happy!")
        print_pause("You lost! The dog is so hungry "
                    "he will now attack you!")
        play_again(play_again_list)


# The player uses the item from the backpack to attack the enemy
def action_1(enemy, item, items_chest, play_again_list, enemies):
    # Enemies do not repeat in one game
    enemies.remove(enemy)
    if enemy == "human_pirate":
        human_pirate(item, play_again_list)
    elif enemy == "zombie_pirate":
        zombie_pirate(item, play_again_list)
    elif enemy == "hungry_dog":
        hungry_dog(item, play_again_list)
    print_pause("Your backpack is empty again.")
    items_chest.append(item)


# The player exchanges the item in the backpack
def action_2(enemy, item, items_chest, play_again_list, enemies):
    print_pause("You have arrived back at the treasure chest.")
    print_pause(f"Which item do you want to exchange {item} for?\n")
    items_chest.append(item)
    print_pause(f" - {items_chest[0].capitalize()}\n"
                f" - {items_chest[1].capitalize()}\n")
    item = valid_input("Please, enter a name of the item.\n", items_chest)
    print_pause(f"You put {item} in your backpack and return to the {enemy}.")
    items_chest.remove(item)
    action_1(enemy, item, items_chest, play_again_list, enemies)


# The players find a treasure chest and must choose an item to pick from
# the ["gold", "jar of brains", "bones"] list
def find_chest(items_chest):
    print_pause("At last, you find a treasure chest filled with"
                " three items.")
    print_pause(f"Which item would you like to take?\n")
    print_pause(f" - {items_chest[0].capitalize()}\n"
                f" - {items_chest[1].capitalize()}\n"
                f" - {items_chest[2].capitalize()}\n")
    item = valid_input("Please, enter the name of an item.\n", items_chest)
    print_pause(f"You put {item} in your backpack and continue.")
    items_chest.remove(item)
    return item


# The player is given a choice of two actions after meeting an enemy:
# to use an item to attack the enemy
# or to return to the treasure chest and pick another item.
def meet_enemy(item, items_chest, actions, play_again_list, enemies):
    # The enemy is chosen at random
    enemy = random.choice(enemies)
    print_pause(f"Yikes! You've been approached by a {enemy}.")
    print_pause("What will you do next?\n")
    print_pause(f" 1. Get your {item} out of the backpack.\n"
                " 2. Run back to the old chest to exchange your item.\n")
    action = valid_input("Please enter a number 1 or 2.\n", actions)
    if action == '1':
        action_1(enemy, item, items_chest, play_again_list, enemies)
    elif action == '2':
        action_2(enemy, item, items_chest, play_again_list, enemies)


# After the game is over, the user has the option to play the game again
def play_again(play_again_list):
    print_pause("Would you like to play again?")
    response = valid_input("Please, enter yes or no.\n", play_again_list)
    if response == "yes":
        print_pause("Ok. Let’s restart.\n")
        play_game()
    elif response == "no":
        sys.exit()


def game_body(items_chest, enemies, actions, play_again_list):
    while len(enemies) != 0:
        item = find_chest(items_chest)
        meet_enemy(item, items_chest, actions, play_again_list, enemies)
    print_pause("Congratulatons!")
    print_pause("You defeated all enemies and can sail to safety!")
    play_again(play_again_list)


def play_game():
    items_chest = ["gold", "brains", "bones"]
    enemies = ["human_pirate", "zombie_pirate", "hungry_dog"]
    actions = ['1', '2']
    play_again_list = ["yes", "no"]
    intro()
    game_body(items_chest, enemies, actions, play_again_list)


play_game()
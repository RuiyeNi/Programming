import time
import random


def print_pause(text):
    # print text with a followed pause
    print(text)
    time.sleep(2)


def left():
    # Things that happen to the player in the house
    global restart_flag
    print_pause("Your walk along the left passageway.")
    print_pause("You are about to approach the dark shadow " +
                "and out steps a " + attacker + ".")
    print_pause("Eep! This is where the treasure chest is!")
    print_pause("The " + attacker + " attacks you!")
    house_choice = []
    while house_choice != "1" and house_choice != "2":
        house_choice = input("Would you like to (1) fight or (2) run away?")
    if house_choice == "1":
        if len(tool) > 0:
            print_pause("As the " + attacker +
                        " moves to attack, " +
                        "you throw the torch torwards it.")
            print_pause("The " + attacker +
                        " catches on fire and burns into ashes immediately")
            print_pause("You use the shovel to dig out " +
                        " the pirate\'s treature chest!")
            print_pause("You are victorious!")
        else:
            print_pause("You feel a bit under-prepared for this.")
            print_pause("You do your best ...")
            print_pause("But you are no match for the " + attacker + ".")
            print_pause("You have been defeated!")

        choice_restart = input("Would you like to play again?[y/n]").lower()
        while choice_restart != 'y' and choice_restart != 'n':
            choice_restart = input("Would you like to play again?[y/n]")
        if choice_restart == 'n':
            restart_flag = False
        else:
            print_pause("Excelent! Restarting the game ...")
    elif house_choice == "2":
        print_pause("You escape back to the entrance.")
        entrance()


def right():
    global tool
    # Things that happen to the player in the cave
    print_pause('You cautiously follow the wall and move forward.')
    if len(tool) > 0:
        print_pause("You have been here before, " +
                    "and gotten all the good stuff.")
    else:
        print_pause('It turns out to be a very deep tunnel.')
        print_pause('You have found a warm fireplace, a shovel and a radio ' +
                    'emitting the hum sound at the end of the tunnel.')
        print_pause('You make a torch from the fireplace.')
        tool = "shovel"
        print_pause("And you take the " + tool + " with you.")
    print_pause("You walk back to the entrance.")
    entrance()


def entrance():
    # Things that happen to the player in the field
    passage_choice = []
    while passage_choice != "1" and passage_choice != "2":
        print_pause('')
        print_pause("Enter 1 to choose the left passageway.\n" +
                    "Enter 2 to choose the right passageway.\n" +
                    "Which one would you like to go?")
        passage_choice = input("(Please enter 1 or 2.)")

    if passage_choice == "1":
        left()
    elif passage_choice == "2":
        right()


def restart_game():
    # A complete Cycles 
    global attacker

    if len(attacker) < 1:
        attackers = ['giant zombine', 'skeleton horse', 'killer bunny']
        attacker = random.choice(attackers)

    print_pause('You find yourself in the entrance ' +
                'of a quiet and cold dungeon.')
    print_pause('Rumor has it that a ' + attacker +
                ' is somewhere around here,' +
                ' and has been protecting a pirate\'s treasure chest')
    print_pause('In front of you are two passageways.')
    print_pause('To your left is a light-illuminated passageway ' +
                'with a shaky black shadow on the ground.')
    print_pause('To your right is a dark and sinister passageway ' +
                'from which comes a mysterious hum.')
    entrance()


restart_flag = True

while restart_flag:
    tool = []
    attacker = []
    restart_game()

print_pause("Thanks for playing! See you next time.")

# info[0]: weather
# info[1]: Pikachu
# info[2]: times of waiting

import time
import random


def print_pause(word):
    print(word)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause(
                "Sorry, that's not a valid input."
                "Please try again.")
    return response


def valid_input2(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 == response:
            break
        elif option2 == response:
            break
        else:
            print_pause(
                "Sorry, that's not a valid input."
                "Please try again.")
    return response


def intro():
    print_pause("Welcome to the Pockemon World!")
    print_pause("Here pokemons are friends "
                "of human beings and we help each other.")
    weather = random.randint(0, 2)
    weatherchoice = ['sunny', 'cloudy', "rainy"]
    realweather = weatherchoice[weather]
    print_pause("You are an elementary school student and"
                " today you will go camping with your friends.")
    print_pause('"It will rain today." Your mother tells you.')
    print_pause('On a ' + realweather + " morning, " + "you set out"
                " with your friends and arrive at the destination.")
    print_pause("Suddenly a tiger comes out and kills your"
                " friends and you hide yourself in a cave.")
    print_pause("After a few minutes, it is silent outside.")
    return weather


def play_game():
    weather = intro()
    info = [weather, 0, 0]
    placego(info)


def placego(info):
    place = valid_input2("You are in the cave now.\n"
                         "Do you want to go outside or"
                         " explore deep in the cave?\n"
                         "A. Go outside \n"
                         "B. Explore the cave\nA or B?\n", "a", "b")
    if 'a' in place:
        go_out(info)
    elif 'b' in place:
        explore(info)


def explore(info):
    if info[1] == 0:
        print_pause("You find a bag at the end of the cave.")
        print_pause("In the bag there is a pokemon called Pikachu.")
        print_pause("You achieve Pikachu!")
        info[1] = 1
    elif info[1] == 1:
        print("You have explored the cave."
              "There is nothing to do here.")
    placego(info)


def again():
    again1 = valid_input2("Do you want to play agin? Y/N\n", "y", "n")
    if again1 == 'y':
        print_pause("Let's start again!\n\n\n")
        play_game()
    elif again1 == 'n':
        print_pause("Thank you for playing the game!")


def go_out(info):
    print_pause("You find the tiger is still there.")
    act = valid_input("Do you want to wait for "
                      "some time or fight it now?\n", "wait", "fight")
    if "fight" in act:
        fight(info)
    elif "wait" in act:
        if info[2] >= 2:
            print_pause("You wait too long. \n")
            print_pause("The tiger runs into the cave and eat your head.")
            print_pause("You are defeated.")
            again()
        else:
            info = wait(info)
            placego(info)


def wait(info):
    weatherchoice = ['sunny', 'cloudy', "rainy"]
    info[0] = (info[0] + 1) % 3
    print_pause("You wait for 30 minutes.\n"
                "The weather becomes " + weatherchoice[info[0]] + ".")
    info[2] = info[2] + 1
    return info


def fight(info):
    if info[1] == 0:
        print_pause("The tiger is so strong that you cannot beat it. \n"
                    "Your head is eaten.")
        again()
    elif info[1] == 1 and info[0] == 2:
        print_pause("Pikachu fights for you.")
        print_pause("Pikachu uses his skill of thunder.")
        print_pause("On the rainy day, the power of "
                    "thunder is doubled and the thunder hits the tiger.")
        print_pause("The tiger is dead and you survive!\n Victory!")
        again()
    elif info[1] == 1 and info[0] != 2:
        print_pause("Pikachu fights for you.")
        print_pause("Pikachu uses his skill of thunder.")
        print_pause("But the tiger is so strong that it can still bite you.")
        print_pause("The tiger eats your head.")
        print_pause("You are defeated.")
        again()
    else:
        print("Error!!!!!")


play_game()

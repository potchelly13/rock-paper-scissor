import random

choices = ['rock', 'paper', 'scissor']
rock = choices[0]
paper = choices[1]
scissor = choices[2]
cpu_choice = random.choice(choices)
if cpu_choice == 'rock':
    cpu_choice = rock

if cpu_choice == 'paper':
    cpu_choice = paper

if cpu_choice == 'scissor':
    cpu_choice = scissor

player_choice = input('choose between rock paper and scissor : ')
if player_choice == 'rock':
    player_choice = rock

if player_choice == 'paper':
    player_choice = paper

if player_choice == 'scissor':
    player_choice = scissor

if player_choice not in choices:
    print("you have to choose between rock paper and scissor ")
else:
    print(f"the cpu chose {cpu_choice}")

# compare the computer choice with my user input

while True:
    if player_choice == rock:
        if cpu_choice == paper:
            print("cpu wins")
        elif cpu_choice == scissor:
            print("player wins")
        elif cpu_choice == rock:
            print("tie")

    if player_choice == paper:
        if cpu_choice == rock:
            print("player wins ")
        elif cpu_choice == paper:
            print("tie")
        elif cpu_choice == scissor:
            print("cpu win ")

    if player_choice == scissor:
        if cpu_choice == rock:
            print("cpu wins ")
        elif cpu_choice == paper:
            print("player win")
        elif cpu_choice == scissor:
            print("tie")
    break

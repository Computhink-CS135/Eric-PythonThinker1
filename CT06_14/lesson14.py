
import math

# recap1
# import random
# total = 0
# rolls = []
# for i in range(0, 5):
#     die = random.randint(1, 6)
#     total += die
#     rolls.append (die)
# print(rolls)
# print(f"the sum of {rolls} is {total}.")

# task1
# fruit = ["apples", "bananas", "grapes"]
# prices = [0.5, 1, 1.5]
# for i in range(len(fruit)):
#     print(f"{fruit[i]} costs ${prices[i]}.")

# task2
# items = ["apple", "milk", "bread", "egg", "chocolate"]
# stock = [15, 0, 8, 25, 3]
# print("---Stock Menu---")
# for i in range(len(items)):
#     if stock[i] == 0:
#         status = "Out Of Stock"
#     elif stock[i] < 10:
#         status = "Low Stock"
#     else:
#         status = "Well Stocked"
#     print(f"Item: {items[i]} | Stock: {stock[i]} | Status: {status}​")

# while True:
#     bought = [1, 1, 1, 1, 1]
#     item_buy = input("what do you want to buy?\n").lower()
#     if item_buy == "end":
#         break
#     if item_buy in items:
#         print("purchase successful!")
#         stock[items.index (item_buy)] - bought[items.index (item_buy)]
#         for i in range(len(items)):
#             if stock[i] == 0:
#                 status = "Out Of Stock"
#             elif stock[i] < 10:
#                 status = "Low Stock"
#             else:
#                 status = "Well Stocked"
#             print(f"Item: {items[i]} | Stock: {stock[i]} | Status: {status}​")
#     else:
#         print("purchase failed...")

# task4
import random
moves = ["rock", "paper", "scissors"]
player_score = 0
cpu_score = 0
while player_score < 3 and cpu_score < 3:
    cpu_choice = random.choice(moves)
    player_choice = input("Choose sissors, paper or rock.\n").lower()
    if player_choice in moves:
        print(f"CPU chose {cpu_choice}.")
        if (player_choice == "scissors" and cpu_choice == "paper") or (player_choice == "paper" and cpu_choice == "rock") or (player_choice == "rock" and cpu_choice == "scissors"):
            player_score += 1
            print("you won this round!")
        elif player_choice == cpu_choice:
            print("it's a draw.")
        else:
            cpu_score += 1
            print("CPU wins this round.")
        print(f"Score - Player: {player_score} | Computer: {cpu_score}")
if player_score == 3:
    print("you have won the CPU !!!")
else:
    print("the CPU has won you...")
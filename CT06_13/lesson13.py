
import math
# recap1
# money = 1000
# while True:
#     print("---ATM MENU---\n")
#     print("1, withdraw")
#     print("2, Deposit")
#     print("3, check balance")
#     print("4, exit\n")
#     choice = int(input("enter your choice.\n"))
#     if choice == 1:
#         taken = int(input("how much money do you want to withdraw?\n"))
#         if taken > money:
#             print("invalid")
#             continue
#         else:
#             money -= taken
#     elif choice == 2:
#         put = int(input("how much money do you want to deposit?\n"))
#         money += put
#     elif choice == 3:
#         print(f"your balance is ${money}")
#     elif choice == 4:
#         break
#     else:
#         print("invalid number")
#         continue

# task1
# groceries = ["apple", "bread", "carrots", "dates", "eggs", "grapes", "honey" ]
# print(groceries)
# groceries[6] = "herbs"
# print(groceries)
# groceries.append("ice")
# print(groceries)
# groceries.insert(1, "bananas")
# print(groceries)
# groceries.pop(2)
# print(groceries)
# remove = groceries.pop(2)
# print(groceries)
# print(f"{remove} was removed.")

# task2
# groceries = ["apple", "bread", "carrots", "dates", "eggs", "grapes", "honey" ]
# for i in range(len(groceries)):
#     if groceries[i] == "apple":
#         print(f"{groceries[i]}: I need 5 of them.")
#     elif groceries[i] == "carrots":
#         print(f"{groceries[i]}: I need 3 of them.")
#     elif groceries[i] == "grapes":
#         print(f"{groceries[i]}: get the FreshFarm brand.")
#     else:
#         print(groceries[i])

# task3
# groceries = []
# while True:
#     food = input("what do you need?\n").lower()
#     if food == "end":
#         for i in range(len(groceries)):
#             print(f"you have bought {groceries[i]}.")
#         break
#     else:
#         groceries.append (food)

# task4
# catalogue = []
# while True:
#     item = input("what are you going to add to your catalogue?\n"). lower()
#     if item == "end":
#         break
#     catalogue.append (item)
# print(catalogue)
# ask = input("what are you looking for?\n").lower
# if ask in catalogue:
#     print(f"yes we have {ask}.")
# else:
#     print(f"we don't have {ask}.")

# task5
# import random
# winnings = 0
# winner = []
# guess = int(input("what is your number from 1 - 9999?\n"))
# if guess < 10000 and guess > 0:
#     for i in range(1, 11):
#         num = random.randint(1, 9999)
#         winner.append (num)
#     print(f"the winning numbers were:")
#     for i in range(len(winner)):
#         print(winner[i])
#         if guess == winner[i]:
#             winnings += 1
#     if winnings > 0:
#         print(f"you got {winnings} correct!!!")
#     else:
#         print("you lost.  >:(")
# else:
#     print("tryna cheat you mother fucking bot!")

# task6
ChoosenToppings = []
toppings = ["extra cheese", "pepperonis", "sausage", "fresh garlic", "bacon", "pineapple", "chicken", 
            "beef", "mushrooms", "shrimp", "end"]
for i in range(len(toppings)):
    print(f"{i + 1}. {toppings[i]}")
while True:
    num = int(input("please choose your pizza toppings by number.\n"))
    if num == 11:
        break
    elif num > 11:
        print("no such topping.")
        continue
    ChoosenToppings.append (toppings[num - 1])
print("so your pizza will have")
print(ChoosenToppings)
print("as your toppings.")
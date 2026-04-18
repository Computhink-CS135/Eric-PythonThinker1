
import math
# recap1
# money = 1000
# while True:
    # print("---ATM MENU---\n")
    # print("1, withdraw")
    # print("2, Deposit")
    # print("3, check balance")
    # print("4, exit\n")
    # choice = int(input("enter your choice.\n"))
    # if choice == 1:
    #     taken = int(input("how much money do you want to withdraw?\n"))
    #     if taken > money:
    #         print("invalid")
    #         continue
    #     else:
    #         money -= taken
    # elif choice == 2:
    #     put = int(input("how much money do you want to deposit?\n"))
    #     money += put
    # elif choice == 3:
    #     print(f"your balance is ${money}")
    # elif choice == 4:
    #     break
    # else:
    #     print("invalid number")
    #     continue

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
groceries = []
while True:
    food = input("what do you need?\n").lower()
    if food == "end":
        for i in range(len(groceries)):
            print(f"you have bought {groceries[i]}.")
        break
    else:
        groceries.append (food)
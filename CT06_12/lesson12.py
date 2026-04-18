
import math
# recap1
# num1 = int(input("input a number\n"))
# if num1 % 3 == 0 and num1 % 5 == 0:
#     print(f"{num1} is divisible by 3 and 5.")
# else:
#     print(f"{num1} is not divisible by 3 and 5.")

# task1
# visitors = 0
# while visitors < 50:
#     visitors += 1
#     print(visitors)

# task2
people = 0
# while True:
#     people += 1
#     print(people)
#     if people >= 50:
#         break

# task3
# order = food = input("what would you like to order?\n")
# while True:
#     food = input("what would you like to order?\n").lower()
#     if food == "end":
#         break
#     order = order + ", " + food
# print(f"so it comes out to {order}")

# task4
# num1 = 10
# while not num1 <= 0:
#     print(num1)
#     num1 -= 1
# else:
#     print("happy new year")

# task5
# import random
# tries = 0
# score = 0
# while True:
#     num1 = random.randint(1, 20)
#     num2 = random.randint(1, 10)
#     tries += 1
#     ans = int(input(f"what is {num1} X {num2}?\n"))
#     if ans == num1 * num2:
#         print("that is correct!")
#         score += random.randint(1, 10)
#         if score >= 10:
#             if tries == 1:
#                 print("1st try!!!!")
#             else:
#                 print(f"you took {tries} attempts.")
#             break
#     score -= 1
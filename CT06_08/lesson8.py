
import math
# recap1
# numbers = int(input("how many numbers do you want to multiply?\n"))
# total = 1
# for i in range(1, numbers + 1):
#     num = int(input(f"what is number {i}?\n"))
#     total = total * num
# print(f"the product is {total}.")

# Task1
# 1a
# import time
# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)

# 1b
# import time
# seconds = int(input("how many seconds?\n"))
# for i in range(seconds, 0, -1):
#     print(i)
#     time.sleep(1)

# task2
# 2a
# import random
# random_num = random.randint(1, 10)
# print(random_num)

# 2b
# import random
# for i in range(1, 21):
#     random_num = random.randint(0, 10001)
#     print(random_num)

# task3
# 3a
# boolean = False
# print(boolean)

# 3b
# boolean1 = True
# boolean2 = True
# print(boolean1 == boolean2)

# 3c
# boolean1 = True
# boolean2 = False
# print(boolean1 == boolean2)

# task4
# import random
# guess = int(input("guess the number\n"))
# random_num = random.randint(1, 11)
# print(guess == random_num)
# print(f"the number is {random_num}.")

# task5
import random
num1 = random.randint(1, 11)
num2 = random.randint(1, 11)
answer = num1 * num2
user_answer = int(input("what is "  + str(num1) +  " X " + str(num2) + "?\n"))
print(user_answer == answer)
print(f"the answer is {answer}.")
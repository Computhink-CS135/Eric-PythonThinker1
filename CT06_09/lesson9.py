

import math
# task1
# import random
# num1 = random.randint(1, 6)
# num2 = random.randint(1, 6)
# num3 = random.randint(1, 6)
# even = False
# odd = False
# print(f"1st die:{num1}")
# print(f"2nd die:{num2}")
# print(f"3rd die:{num3}")
# if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0:
#     even = True
# else:
#     odd = True
# if even == True or odd == True:
#     print("All numbers are even/odd.")
# else:
#     print("All numbers are not even/odd.")

# task2
# days = int(input("input the number of days you have borrowed your book.\n"))
# if days >= 24:
#     print("remember to return your book.")

# task3
apples = int(input("how many apples do you want to buy.\n"))
if apples >= 10:
    print ("you will get a 10% discount.")
    price = apples * 1 * 0.9
else:
    price = apples * 1
print(f"the price is {price}")
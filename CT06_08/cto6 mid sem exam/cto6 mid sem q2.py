
total = 0
money = int(input("how much money did you have at the start?\n"))
days = int(input("how many days?\n"))
for i in range(1, days + 1):
    total = money + (i)
    print(f"you have ${total}.")
print(f"you will have ${total} after {days} day(s)")
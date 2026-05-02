
# task1
for i in range(10, 210, 10):
    print(i)

# task2
pw = "superpass123"
password = input("what is the password?\n").lower()
if password == pw:
    print("access granted")
else:
    print("access denied")
name = input("Enter your name: ")

m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
m3 = int(input("Enter mark 3: "))

total = m1 + m2 + m3
average = total / 3

print("Name:", name)
print("Total:", total)
print("Average:", average)

if average >= 50:
    print("Result: PASS")
else:
    print("Result: FAIL")
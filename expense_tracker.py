
expenses = []

for i in range(3):
    amount = float(input("Enter expense: "))
    expenses.append(amount)

total = sum(expenses)

print("Expenses:", expenses)
print("Total expense:", total)

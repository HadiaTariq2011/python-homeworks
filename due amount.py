def calculate_due(total_bill, amount_paid):
    if amount_paid >= total_bill:
        return 0
    else:
        return total_bill - amount_paid

total = float(input("Enter the total bill amount: "))
paid = float(input("Enter the amount paid by the customer: "))

due = calculate_due(total, paid)

if due == 0:
    print("No amount is due. The bill is fully paid.")
else:
    print(f"The due amount is: {due:.2f}")

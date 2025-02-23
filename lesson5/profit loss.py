actual_cost=float(input("enter the actual cost"))
sale_amount=float(input("enter your sales amount"))
if sale_amount>actual_cost:
    amount=sale_amount-actual_cost
    print("the total profit is", amount)
else:
    print("no profit")
    
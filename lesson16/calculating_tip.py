def total_calc(amount,tip_percent):
    total= amount*(1+0.01*tip_percent)
    total=round(total,2)
    print("total amount is",total)
total_calc(125,10)

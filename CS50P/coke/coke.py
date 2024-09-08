cost = 50
while cost > 0:
    coin = int(input('Insert Coin: '))
    if coin == 25 or coin == 10 or coin == 5:
        cost -= coin
        if cost <= 0:
            print(f"Change Owed: {cost * (-1)}")
        else:
            print(f"Amount Due: {cost}")
    else:
       print(f"Amount Due: {cost}")





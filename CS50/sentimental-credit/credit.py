# TODO
import math
credit = int(input('Credit Card Number: '))

credit_1 = math.floor((credit % 10))
credit_2 = math.floor((credit % 100)/10)
credit_3 = math.floor((credit % 1000)/100)
credit_4 = math.floor((credit % 10000)/1000)
credit_5 = math.floor((credit % 100000)/10000)
credit_6 = math.floor((credit % 1000000)/10000)
credit_7 = math.floor((credit % 10000000)/1000000)
credit_8 = math.floor((credit % 100000000)/10000000)
credit_9 = math.floor((credit % 1000000000)/100000000)
credit_10 = math.floor((credit % 10000000000)/1000000000)
credit_11 = math.floor((credit % 100000000000)/10000000000)
credit_12 = math.floor((credit % 1000000000000)/100000000000)
credit_13 = math.floor((credit % 10000000000000)/1000000000000)
credit_14 = math.floor((credit % 100000000000000)/10000000000000)
credit_15 = math.floor((credit % 1000000000000000)/100000000000000)
credit_16 = math.floor((credit % 10000000000000000)/1000000000000000)


if credit_16 == 5 and credit_15 in [1,2,3,4,5]:
    print('MASTERCARD')

elif credit_15 == 3 and credit_14 in [4,7]:
    print('AMEX')

elif credit_13 == 4 or credit_16 == 4:
    print('VISA')

else:
    print('INVALID')
from cs50 import get_string


sum1 = 0
cardNumber = get_string("Number: ")
if len(cardNumber) == 16:
    for n in range(len(cardNumber)):
        if n % 2 == 0:
            if int(cardNumber[n]) * 2 >= 10:
                sum1 += int((int(cardNumber[n]) * 2) / 10)
                sum1 += int((int(cardNumber[n]) * 2) % 10)
            else:
                sum1 += int(cardNumber[n]) * 2
        else:
            sum1 += int(cardNumber[n])
elif len(cardNumber) in [13, 15]:
    sum1 += int(cardNumber[0])
    for n in range(1, len(cardNumber)):
        if n % 2 == 1:
            if int(cardNumber[n]) * 2 >= 10:
                sum1 += int((int(cardNumber[n]) * 2) / 10)
                sum1 += int((int(cardNumber[n]) * 2) % 10)
            else:
                sum1 += int(cardNumber[n]) * 2
        else:
            sum1 += int(cardNumber[n])

if ((cardNumber[0] + cardNumber[1]) in ["34", "37"]) and (sum1 % 10 == 0):
    print("AMEX")
elif ((cardNumber[0] + cardNumber[1]) in ["51", "52", "53", "54", "55"]) and (
    sum1 % 10 == 0
):
    print("MASTERCARD")
elif (
    ((cardNumber[0]) in ["4"]) and (sum1 % 10 == 0) and len(cardNumber) in [13, 15, 16]
):
    print("VISA")
else:
    print("INVALID")

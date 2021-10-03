from cs50 import get_int


def calc(n):
    sum1 = 0
    sum2 = 0
    num = str(n)
    
    while num != "":
        # Remove last digit and add to sum1
        mod1 = int(num[-1])
        num = num[:-1]
        sum1 = sum1 + mod1
        # Remove second last digit

        if num != "":
            mod2 = int(num[-1])
            num = num[:-1]
            # Double second last digit and add digit to sum2
            mod2 = mod2 * 2
            modtemp = str(mod2)
            d1 = int(modtemp[-1])
            if len(modtemp) > 1:
                d2 = int(modtemp[-2])
            else:
                d2 = 0
            sum2 = sum2 + d1 + d2

    total = sum1 + sum2
    return total
    

def check(num):
    start = str(num)
    
    # Next check starting digits for card type    
    # Mastercard
    if ((int(start[0]) == 5) and (0 < int(start[1]) < 6)):
        return("MASTERCARD")
    elif ((int(start[0]) == 3) and (int(start[1]) == 4 or int(start[1]) == 7)):
        return("AMEX")
    elif (int(start[0]) == 4):
        return ("VISA")
    else:
        return ("INVALID")
        

def main():
    num = get_int("Number: ")
    total = 0
    i = len(str(num))
    # Check if length is valid
    if (i != 13 and i != 15 and i != 16):
        print("INVALID")
        exit()
    
    total = calc(num)
    if (total % 10 != 0):
        print("INVALID")
        exit()

    print(check(num))
    

# Calling main function
if __name__ == "__main__":
    main()

a = int(input("Enter first range: "))
b = int(input("Enter second range: "))

for i in range (a, b +1):
    flag= 0
    for j in range (2, (i//2) + 1 ):
        if i % j == 0:
            flag = 1 
            # used as a bookmark to check whether 
            # the number is completely divisible by the j range
            # hence when the condition true, flag=1, 
            # and we break the loop
    if flag == 0:
        # if the number is not divisible by any number in the range of j,
        # flag = 0 indicates it is of i range and does not satisfy 
        # the condition of being divisible by any number in the range of j
        print(i, "is a prime number")
#write a program to take AN INTEGER input from the userand check whether the number is even or odd.
num = int(input("Enter an integer: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# while loop

a = 0 #assignment of 0 to variable a
while a<10 : # after while loop, enter the condition to check whether a is less than 10 or not
    print(a) # print the value of a
    a = a + 1   # to give increment to variable a, so that the loop will not run infinitely.

# For loop

for i in range(0,10,2): # for loop to iterate from 0 to 10 with a step of 2
    print(i) # print the value of i
    
#no connection b/w container and "for" variable is i, and we can use any variable name instead of i, 
# but it is a convention to use i as a variable name in for loop.


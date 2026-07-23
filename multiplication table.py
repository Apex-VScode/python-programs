# write a program to print a multiplication table of a number entered by the user.
n = int(input("Enter a number to print its multiplication table: "))
for i in range(1,11): # for loop to iterate from 1 to 10
    print(n,'x',i,'=',n*i) # print the value of i
# this for prints multiplication table of n from 1 to 10

# wrtie a program to print first 50 even numbers using 'for' loop.

for i in range (0,100,2):
   print(i) 

# write a program to print first 50 odd numbers using 'for' loop.
for i in range (1,100,2):
    print(i) 

# additional methods to print even and odd numbers using 'while' loop.
for i in range (1,131):
    if i%2 != 0:
        print(i, "is an odd number") # prints odd numbers from 1 to 130
    if i%2 == 0:
        print(i, "is an even number") # prints even numbers from 1 to 130
    else:
       print() 

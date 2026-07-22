year = int(input("Enter the year here :"))
if (year%4 == 0 and year%100 != 0) or ( year%400 == 0):
    print("The year you entered is a Leap year")
else:
    print("The year you entered is a Leap year")

a = int(input("Enter first angle here :"))
b = int(input("Enter second angle here :"))
c = int(input("Enter third angle here :"))
if a + b + c == 180:
    print("The angles form a triangle")
if a == 90 or b == 90 or c == 90:
     print("The angles form a right triangle")
else:
    print("The angles do not form a triangle")

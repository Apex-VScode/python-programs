
principal = int(input("Enter your Principal Amount Here"))
Rate = int(input("Enter your Rate OF Interest Here"))
Time = int(input("Enter your Time Period Here"))
#one mistake done by me,
# i did this,,,,,Time = input(int("Enter your Time Period Here"))
#data type sabse phele likho, logic input ka data type decide karna hai
SI = (principal*Rate*Time)/100
print("calculated Simple Interest :", SI)
Total_amount = int(principal + SI)
print('Total Amount on Maturity:',Total_amount)

L= int(input(' Enter length of rectangle here :'))
B = int(input(' Enter breadth of rectangle here :'))

Area = (L*B)
Perimeter = (2*(L*B))

print("Area of rectangle:", Area)
print("Perimeter of rectangle:", Perimeter)
                          

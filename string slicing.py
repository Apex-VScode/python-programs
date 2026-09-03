a = "python programming"
# starting : ending se ek jyada
print(a[0:6])  # prints "python"
print(a[7:18])  # prints "programming"
print(a[7:15])  # prints "programm" 
print(a[-9:-2])  # prints "ogrammi"
print (a[15:7:-1]) # prints "gnimmargorp"

print(a[::-1]) # prints "gnimmargorp nohtyp"
#it means start from end and go to start with step -1
# and representation of string in reverse order
# a[17:-1:-1] will print "gnimmargorp nohty" 
# because it will include 0th index 

print(a[-3:-10:-1]) # prints "immargo"

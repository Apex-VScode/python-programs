# a line of text as input and create a new string by replacing 
# every alphabetic character at given index 0,2,4 with the corresponding 
# uppercase letter , if the string is "welcome all" 
#the output should be "WeLcOmE aLl"
a=input("Enter a line of text: ")
new_a="" # why, to make a new string, 
   #we need to store the new string in a variable
# indexing a gayi to loop wala method use karna hoga
for i in range(len(a)): # always len(a) use karna hoga
                           #it gives the index of each character in the string
    if i%2==0:
        new_a+=a[i].upper()
    else:
        new_a+=a[i]
print(new_a)
    
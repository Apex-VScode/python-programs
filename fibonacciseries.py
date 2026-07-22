#write a program to print first ten numbers of the fibonacci series

# eg 0 and 1 
# so fibanacci series = 0,1,1+0,1+1,3,5,8,13

n = int(input("enter no. of fibannci series:  " ))

f= 0
s= 1
print(f,s,end = " ")

for i in range(0,n-2): 
    # range kaise pata lagae? simple n-2 baar chalana hai n number lane ke liye
    # (2 phele hi aa chuke h).
    T = f + s
    print(T,end = " ")
    f=s
    s=T

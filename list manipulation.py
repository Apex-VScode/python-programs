L = [2, 4.5, "python", 7, "programming", 3.14, "data", 10]

#input/inserting an element at a specific index
L.insert(2, "hello") 
#it removes the element at index 2 and inserts "hello" at that position
print(L)

L.append("world") #it adds "world" at the end of the list
print(L)

N = [1, 2, 3, 3, 3, 4, 5]
#removing an element from the list
N.remove(3) #it removes the first occurrence of 3 from the list
print(N)

#important: if the element is not present in the list, 
# it will raise a ValueError

#important
a= N.pop() #it removes the last element from the list and returns it
print(a)

print(N)

a = N.pop(2) #it removes the element at index 2 and returns it
print(a)

N.reverse() #it reverses the list
print(N)


N.clear() #it removes all the elements from the list
print(N)

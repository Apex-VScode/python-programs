L = [1, 2, 3, 4, 5,78,4,6,7,8,9,10]

print("Sum:", sum(L))# it returns the sum of all elements in the list
print("Max:", max(L))# it returns the maximum element in the list
print("Min:", min(L))# it returns the minimum element in the list
print("Length:", len(L))# it returns the number of elements in the list
print("Average:", sum(L)/len(L))# it returns the average of all elements in the list
print("Sorted List:", sorted(L))# it returns a new list with elements sorted in ascending order
print("Reversed List:", list(reversed(L)))# it returns a new list with elements in reverse order
print("Count of 4:", L.count(4))# it returns the number of occurrences of 4 in the list
print("Index of 7:", L.index(7))# it returns the index of the first occurrence of 7 in the list
print("Is 5 in the list?", 5 in L)# it returns True if 5 is in the list, False otherwise
print("percentage of 4 in the list:", (L.count(4)/len(L))*100, "%")# it returns the percentage of occurrences of 4 in the list

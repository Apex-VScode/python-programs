#write a program to input A LINE OF TEXT AND COUNT 
# AND PRINT NUMBER OF WORDS and words WHICH Contain two or more vowels in it

text = input("Enter a line of text: ")
new_text = text.split() # split the text into words
count = 0
for i in range(len(new_text)):
    vowel_count = 0
    for j in range(len(new_text[i])): 
        if new_text[i][j] in "aeiouAEIOU": 
            vowel_count += 1
    if vowel_count >= 2:
        count += 1
        
        print(new_text[i]) 
print("Number of words with two or more vowels:", count)
 
    
#write a program of that inputs a line of text and print each word in a separte line.
a = "python is very popular programming language"
words = a.split()
print(words)
words = a.split("p")
print(words)
print(type(words))

words = a.split("po")
for word in words:
    print(word)
